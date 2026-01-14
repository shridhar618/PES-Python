import time
import csv
from pathlib import Path
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

# -------------------------
# CONFIG
# -------------------------
URL = "https://airquality.cpcb.gov.in/AQI_India/"

PROFILE_DIR = Path.cwd() / "chrome_profile_aqi"
DOWNLOAD_DIR = Path.cwd() / "aqi_data"
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------
# START DRIVER
# -------------------------
def start_driver():
    options = Options()
    options.add_argument("--window-size=1500,900")
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")

    # Chrome path for macOS
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    prefs = {
        "download.default_directory": str(DOWNLOAD_DIR.resolve()),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = wd.Chrome(options=options)
    return driver


# -------------------------
# WAIT FOR DOWNLOAD
# -------------------------
def wait_for_downloads(timeout_sec=180):
    t0 = time.time()
    while time.time() - t0 < timeout_sec:
        # wait while chrome is downloading
        if list(DOWNLOAD_DIR.glob("*.crdownload")):
            time.sleep(0.5)
            continue

        files = [p for p in DOWNLOAD_DIR.iterdir() if p.is_file()]
        if files:
            return max(files, key=lambda p: p.stat().st_mtime)

        time.sleep(0.5)

    raise TimeoutError("Download did not complete within time")


# -------------------------
# CLOSE MODAL
# -------------------------
def close_blocking_modal(driver):
    time.sleep(1)
    close_xpaths = [
        '//div[@id="myModal"]//button[@class="close"]',
        '//div[@id="myModal"]//button[contains(.,"Close")]',
        '//div[@id="myModal"]//button[contains(.,"OK")]',
        '//div[@id="myModal"]//button[contains(.,"I Agree")]'
    ]

    for xp in close_xpaths:
        try:
            btn = WDW(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, xp))
            )
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)
            return
        except Exception:
            pass

    # force remove modal if still visible
    driver.execute_script("""
        const m = document.getElementById("myModal");
        if (m) m.style.display = "none";
        const b = document.getElementsByClassName("modal-backdrop");
        if (b.length) b[0].remove();
        document.body.classList.remove("modal-open");
    """)


# -------------------------
# MAIN SCRIPT
# -------------------------
driver = start_driver()

try:
    driver.get(URL)

    WDW(driver, 60).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    repo_link = WDW(driver, 60).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(.,'AQI Data Repository') or "
            "contains(.,'AQI Data Repositary') or "
            "contains(.,'AQI Data') or "
            "contains(.,'Air Quality Data')]"
        ))
    )

    close_blocking_modal(driver)

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", repo_link
    )
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", repo_link)

    # switch to new tab
    WDW(driver, 30).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])

    WDW(driver, 60).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    download_logs = []

    for r in rows[1:]:
        tds = r.find_elements(By.TAG_NAME, "td")
        if len(tds) < 2:
            continue

        year = tds[0].text.strip()
        if not year.isdigit():
            continue

        download_cell = tds[1]
        clickable = None

        links = download_cell.find_elements(By.TAG_NAME, "a")
        if links:
            clickable = links[0]
        else:
            btns = download_cell.find_elements(By.TAG_NAME, "button")
            if btns:
                clickable = btns[0]

        if not clickable:
            continue

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", clickable
        )
        time.sleep(0.3)
        driver.execute_script("arguments[0].click();", clickable)

        downloaded = wait_for_downloads()

        ext = downloaded.suffix.lower()
        target = DOWNLOAD_DIR / f"aqi_data_{year}{ext}"

        if target.exists():
            target.unlink()

        downloaded.rename(target)
        download_logs.append((year, str(target)))

    # save log
    with open(DOWNLOAD_DIR / "download_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Year", "FilePath"])
        writer.writerows(download_logs)

    print(f"✅ Downloaded {len(download_logs)} files.")
    print(f"📁 Folder: {DOWNLOAD_DIR}")

except Exception as e:
    driver.save_screenshot(str(DOWNLOAD_DIR / "error_screenshot.png"))
    print("❌ Error occurred:", e)
    raise

finally:
    driver.quit()
