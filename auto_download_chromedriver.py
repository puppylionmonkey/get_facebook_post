import zipfile
import requests
import os
import json
import logging

from win32com import client as wincom_client

from path_config import project_path


def get_file_version(file_path):
    logging.info('Get file version of [%s]', file_path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("{!r} is not found.".format(file_path))
    wincom_obj = wincom_client.Dispatch('Scripting.FileSystemObject')
    version = wincom_obj.GetFileVersion(file_path)
    logging.info('The file version of [%s] is %s', file_path, version)
    return version.strip()


def write_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


def read_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


# ↑讀取資料夾內所有檔案名稱然後放進all_file_name這個list裡
def get_chrome_driver_major_version(chrome_path):
    chrome_ver = get_file_version(chrome_path)
    chrome_major_ver = chrome_ver.split(".")[0]
    return chrome_major_ver


def get_latest_driver_version(browser_ver):
    latest_api = "{}/LATEST_RELEASE_{}".format(CHROME_DRIVER_BASE_URL, browser_ver)
    resp = requests.get(latest_api)
    lastest_driver_version = resp.text.strip()
    return lastest_driver_version


def download_driver(driver_ver, dest_folder):
    download_api = "{}/{}/chromedriver_win32.zip".format(CHROME_DRIVER_BASE_URL, driver_ver)
    dest_path = os.path.join(dest_folder, os.path.basename(download_api))
    resp = requests.get(download_api, stream=True, timeout=300)
    if resp.status_code == 200:
        with open(dest_path, "wb") as f:
            f.write(resp.content)
        logging.info("Download driver completed")
    else:
        raise Exception("Download chrome driver failed")


def unzip_driver_to_target_path(src_file, dest_path):
    with zipfile.ZipFile(src_file, 'r') as zip_ref:
        zip_ref.extractall(dest_path)
    logging.info("Unzip [{}] -> [{}]".format(src_file, dest_path))


def read_driver_mapping_file():
    driver_mapping_dict = {}
    if os.path.exists(CHROME_DRIVER_MAPPING_FILE):
        driver_mapping_dict = read_json(CHROME_DRIVER_MAPPING_FILE)
    return driver_mapping_dict


def download_browser_driver_available(chrome_path):
    chrome_major_ver = get_chrome_driver_major_version(chrome_path)
    mapping_dict = read_driver_mapping_file()
    driver_ver = get_latest_driver_version(chrome_major_ver)
    if chrome_major_ver not in mapping_dict:
        download_driver(driver_ver, CHROME_DRIVER_FOLDER)
        unzip_driver_to_target_path(CHROME_DRIVER_ZIP, CHROME_DRIVER_FOLDER)


CHROME_DRIVER_BASE_URL = "https://chromedriver.storage.googleapis.com"
CHROME_DRIVER_FOLDER = project_path
CHROME_DRIVER_MAPPING_FILE = r"{}\mapping.json".format(CHROME_DRIVER_FOLDER)
CHROME_DRIVER_EXE = r"{}\chromedriver.exe".format(CHROME_DRIVER_FOLDER)
CHROME_DRIVER_ZIP = r"{}\chromedriver_win32.zip".format(CHROME_DRIVER_FOLDER)

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'