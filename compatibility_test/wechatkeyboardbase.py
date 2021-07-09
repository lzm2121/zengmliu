#!/usr/bin/env python3

import logging
import logging.handlers
import os
import unittest
import datetime
import subprocess  # 获取adb命令返回结果
import re  # 使用正则化进行多分隔符划分字符串
import wechat_keyboard
from appium import webdriver

LOG_FORMATTER = '%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(funcName)s %(message)s'
logger = logging.getLogger()

Appium_URL = 'http://localhost:4723/wd/hub'
# 获取连接设备
get_device = "adb devices"
# 获取命令返回结果
(status, deviceName) = subprocess.getstatusoutput(get_device)
deviceName = (re.split('[ \n\t]', deviceName))[4]  # 使用正则化多个分隔符划分
# deviceName = uploadRes.split(' ')[-1].split('\n')[1].split('\t')[0]
# print(deviceName)

# 获取安卓版本
get_version = "adb shell getprop ro.build.version.release"
(status, platformVersion) = subprocess.getstatusoutput(get_version)
# print(platformVersion)
""" 初始化 自动化环境"""
desired_caps = {
    'platformName': 'Android',  # 自动化测试手机的操作系统（Android/iOS）
    'platformVersion': platformVersion,  # 手机安卓版本
    'deviceName': deviceName,  # 设备名，安卓手机可以随意填写
    'appPackage': '',  # 应用程序的包的标识符 启动APP Package名称
    'appActivity': '',  # 应用程序的界面名 启动Activity名称
    'unicodeKeyboard': False,  # 使用自带输入法，输入中文时填True,应该使用微信输入法
    'resetKeyboard': False,  # 执行完程序不恢复原来输入法
    'noReset': True,  # 不要重置App
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
}
print(desired_caps)
# 连接 Appium Server ,初始化自动化环境
driver = webdriver.Remote(Appium_URL, desired_caps)
# 设置最大等待时长，避免因appium server没来得及响应导致页面上没有需要的元素而报错
driver.implicitly_wait(10)

class WeChatIputTestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.auto = cls().auto_input()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     driver.quit()

    def setUp(self) -> None:
        self._setup_log()

    # def tearDown(self) -> None:
        # os.system('adb shell am force-stop com.tencent.mm')

    def auto_input(self):
        # 获取当前分辨率
        el_x = driver.get_window_size()['width']
        el_y = driver.get_window_size()['height']
        return wechat_keyboard.WeChatKeyBoard(driver, el_x, el_y)

    def _setup_log(self):
        log_root = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(log_root):
            os.makedirs(log_root)
        case_log_filename = os.path.join(log_root, f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{self._testMethodName}.log")
        case_log_handler = logging.handlers.RotatingFileHandler(case_log_filename, maxBytes=1024 * 1024)
        formatter = logging.Formatter(LOG_FORMATTER)
        case_log_handler.setFormatter(formatter)
        self._case_log_handler = case_log_handler
        hdlr = logging.StreamHandler()
        hdlr.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(hdlr)
        logger.addHandler(self._case_log_handler)
