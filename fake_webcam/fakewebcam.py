from splinter import Browser
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--use-file-for-fake-video-capture=./salma_hayek.y4m")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_camera": 1
})
browser = Browser('chrome', options=chrome_options)
browser.visit("http://127.0.0.1:5000/")
time.sleep(10)
browser.quit()