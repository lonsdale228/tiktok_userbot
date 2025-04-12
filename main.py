import time

import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions


def main():
    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = uc.Chrome(headless=False,use_subprocess=False)

    driver.get("https://tiktok.com")
    time.sleep(100)

if __name__ == '__main__':
    main()