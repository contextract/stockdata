from datetime import timedelta
from datetime import date
from genericpath import exists
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
import time
import os
import shutil
import glob
import sys
from pathlib import Path

interval = 2

dir = os.path.dirname(__file__)
webdriver_options = webdriver.ChromeOptions()
#webdriver_options.add_argument('headless')
webdriver_options.add_argument("--no-sandbox")
webdriver_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome('%s/driver/chromedriver' %
                          (dir), options=webdriver_options)


if len(sys.argv) < 2:
    print('Usage: %s [Destination]' % (sys.argv[0]))
    sys.exit()

out = sys.argv[1]

if os.path.exists(out) and not os.path.isdir(out):
    print('destination %s is not directory' % (out))
    sys.exit()


def copy_data_file(dst_file):
    home = str(Path.home())
    for file in glob.glob('%s/Downloads/data_*.csv' % (home)):
        print(file)
        shutil.move(file, '%s/%s' % (out, dst_file))


def get_kr_sub(driver, url, dst_file):

    print(url)
    driver.get(url)
    time.sleep(interval)
    #remove_popup(driver)
    time.sleep(interval)
    button = driver.find_element_by_xpath(
        '/html/body/div[2]/section[2]/section/section/div/div/form/div[2]/div/p[2]/button[2]')
    button.click()
    time.sleep(interval)
    csv_button = driver.find_element_by_xpath(
        '/html/body/div[2]/section[2]/section/section/div/div/form/div[2]/div[2]/div[2]/div/div[2]/a')
    csv_button.click()
    time.sleep(interval)
    copy_data_file(dst_file)


def get_kr(driver):
    get_kr_sub(
        driver, 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201', 'stock.csv')
    get_kr_sub(
        driver, 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201030104', 'etf.csv')
    get_kr_sub(
        driver, 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201030204', 'etn.csv')


def remove_popup(driver):
    main = driver.window_handles
    for handle in main:
        if handle != main[0]:
            driver.switch_to_window(handle)
            driver.close()
    driver.switch_to_window(driver.window_handles[0])


get_kr(driver)
driver.close()
