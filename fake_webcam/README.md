# Testing Web applications with webcam
[flaskapp.py](https://github.com/saisyam/web-automation-testing/blob/master/fake_webcam/flaskapp.py) is a simple flask web application with webcam implementation. [fakewebcam.py](https://github.com/saisyam/web-automation-testing/blob/master/fake_webcam/fakewebcam.py) application will access the flask application using Splinter with Chrome web driver. The chrome options are:

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--use-file-for-fake-video-capture=./salma_hayek.y4m")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_camera": 1
})
```

We provide a fake video (y4m format) to the browser to stream into webcam video component. I have created y4m video format from mp4 using ffmpeg tool. The mp4 video contains only one image which is repeated for few seconds. Keep your mp4 pretty small because y4m is an un-compressed format and the size will be huge after conversion.