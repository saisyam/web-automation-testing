from splinter import Browser
import time
import subprocess
import signal
import sys

url = "https://google.com"

cmd = ['ffmpeg', 
       '-video_size','1920x1080',
       '-f', 'x11grab', 
       '-i', ':0.0', 
       'test_record.mp4'
]

browser = Browser('chrome')
sub = subprocess.Popen(cmd, shell=False)
time.sleep(1)
browser.visit(url)
browser.driver.maximize_window()
time.sleep(5)
assert browser.title == "Google"
browser.quit()
sub.send_signal(signal.SIGINT)