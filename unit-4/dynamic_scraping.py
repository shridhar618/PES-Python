import time
import csv
import shutil
import zipfile

from pathlib import Path
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDC
from selenium.webdriver.support import expected_conditions as EC

#define the endpoints
URL="https://airquality.cpcb.gov.in/AQI_India/"

PROFILE_DIR=str(Path.cwd()/ "chrome_profile_aqi")
DOWNLOAD_DIR=str(Path.cwd()/ "aqi_data")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

#create a chrome option object
def start_driver():
    options = Options()
    options.add_argument(f"--window-size=1500,900")
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_argument(f"--disable-gpu")
    options.add_argument('--log-level=3')
    prefs = {"download.default_directory": str(DOWNLOAD_DIR.resolve()),
             "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }
    options.add_experimental_option("prefs", prefs)
    driver = wd.Chrome(options=options)
    return wd.Chrome(options=options)


#define the methods for downloading files
def wait_for_downloads(download_path, timeout=60):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        for fname in Path(download_path).glob('*.crdownload'):
            dl_wait = True
        seconds += 1
    return seconds
