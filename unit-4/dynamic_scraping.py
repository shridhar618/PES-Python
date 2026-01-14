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
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = wd.Chrome(options=options)
    return driver