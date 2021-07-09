#!/usr/bin/env python3

import os
import subprocess
import random
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

class WeChatKeyBoard:
    def __init__(self, driver, width, height):
        self.driver = driver
        self.width = width
        self.height = height

    def enable_WeichatIME(self):
        """切换 微信键盘 为当前输入法"""
        weichatIME = 'adb shell ime set com.tencent.mm/.plugin.hld.WxHldService'
        # os.system(weichatIME)
        adb = subprocess.Popen(weichatIME, shell=True, stdout=subprocess.PIPE)
        # print(adb.stdout.read())
        driver = self.driver
        return driver

    def enable_SougouIME(self):
        """切换 搜狗 为当前输入法"""
        sougouIME = 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'
        # os.system(sougouIME)
        adb = subprocess.Popen(sougouIME, shell=True, stdout=subprocess.PIPE)
        # print(adb.stdout.read())
        driver = self.driver
        return driver

    def switch_to_ninekeyboard(self):
        """切换为九宫格键盘"""
        driver = self.driver
        el_x = self.width
        el_y = self.height
        # 长按微信键盘
        driver.tap([((137 / 1080) * el_x, (1540 / 2288) * el_y)], duration=8)
        # 选择九宫格
        driver.tap([((381 / 1080) * el_x, (1747 / 2288) * el_y)], duration=0)
        # <
        driver.tap([((55 / 1080) * el_x, (1585 / 2288) * el_y)], duration=0)
        # # 初始化自动化环境 打开微信
        # appPackage = 'com.tencent.mm'
        # appActivity = '.ui.LauncherUI'
        # driver.start_activity(appPackage, appActivity)
        # # 切换微信输入
        # self.enable_WeichatIME()
        # # 点击“我”
        # driver.find_elements_by_id("com.tencent.mm:id/icon_iv")[3].click()
        # sleep(1)
        # # 点击“设置”
        # driver.find_elements_by_id("com.tencent.mm:id/image_iv")[4].click()
        # # 点击“插件”
        # driver.find_element_by_id("com.tencent.mm:id/text_prospect").click()
        # # 点击“微信键盘”
        # driver.find_element_by_id("com.tencent.mm:id/content").click()
        # # 点击“键盘设置”
        # driver.find_element_by_id("com.tencent.mm:id/account_arrow_iv").click()
        # # 点击“输入设置”
        # driver.find_elements_by_id("android:id/title")[0].click()
        # # driver.find_elements_by_id("com.tencent.mm:id/content")[0].click()
        # # 点击“九宫格键盘”
        # driver.find_element_by_id("com.tencent.mm:id/content").click()
        # # 点击“完成”
        # driver.find_element_by_id("com.tencent.mm:id/action_option_btn").click()
        return el_x, el_y

    def switch_to_fullkeyboard(self):
        """切换为全键盘"""
        driver = self.driver
        el_x = self.width
        el_y = self.height
        # 长按微信键盘
        driver.tap([((137 / 1080) * el_x, (1540 / 2288) * el_y)], duration=8)
        # 选择全键盘
        driver.tap([((528 / 1080) * el_x, (1935 / 2288) * el_y)], duration=0)
        # <
        driver.tap([((55 / 1080) * el_x, (1585 / 2288) * el_y)], duration=0)
        # driver = self.driver
        # # 初始化自动化环境 打开微信
        # appPackage = "com.tencent.mm"
        # appActivity = ".ui.LauncherUI"
        # driver.start_activity(appPackage, appActivity)
        # # 切换微信输入
        # self.enable_WeichatIME()
        # # 点击“我”
        # driver.find_elements_by_id("com.tencent.mm:id/icon_iv")[3].click()
        # sleep(1)
        # # 点击“设置”
        # driver.find_elements_by_id("com.tencent.mm:id/image_iv")[4].click()
        # # 点击“插件”
        # driver.find_element_by_id("com.tencent.mm:id/text_prospect").click()
        # # 点击“微信键盘”
        # driver.find_element_by_id("com.tencent.mm:id/content").click()
        # # 点击“键盘设置”
        # driver.find_element_by_id("com.tencent.mm:id/account_arrow_iv").click()
        # # 点击“输入设置”
        # driver.find_elements_by_id("android:id/title")[0].click()
        # # 点击“全键盘”
        # driver.find_elements_by_id("com.tencent.mm:id/content")[1].click()
        # # 点击“完成”
        # driver.find_element_by_id("com.tencent.mm:id/action_option_btn").click()
        return el_x, el_y

    def note_press_letters(self):
        """便签 英文长按测试"""
        appPackage = 'com.coloros.note'
        appActivity = 'com.nearme.note.view.AllNoteActivity'
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到便签
        driver.start_activity(appPackage, appActivity)
        # 新建笔记
        driver.find_element_by_id(f"{appPackage}:id/color_floating_button_main_fab").click()
        sleep(2)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        # 中英文切换，触发后为英文
        driver.tap([((772/1080)*el_x, (2264/2288)*el_y)], 0)
        # 长按
        action = TouchAction(driver)
        action.long_press(x=(232/1080)*el_x, y=(2088/2288)*el_y).release().perform()  # z ""
        action.long_press(x=(348/1080)*el_x, y=(2088/2288)*el_y).release().perform()  # x 、
        action.long_press(x=(432/1080)*el_x, y=(2082/2288)*el_y).release().perform()  # c ~
        action.long_press(x=(542/1080)*el_x, y=(2071/2288)*el_y).release().perform()  # v :
        action.long_press(x=(642/1080)*el_x, y=(2065/2288)*el_y).release().perform()  # b ;
        action.long_press(x=(736/1080)*el_x, y=(2082/2288)*el_y).release().perform()  # n ?
        action.long_press(x=(852/1080)*el_x, y=(2060/2288)*el_y).release().perform()  # m !
        action.long_press(x=(345/1080)*el_x, y=(2254/2288)*el_y).release().perform()  # @ #
        action.long_press(x=(663/1080)*el_x, y=(2240/2288)*el_y).release().perform()  # , .
        # 获取上屏内容
        text = driver.find_element_by_id(f"{appPackage}:id/text").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def weixin_press(self):
        """微信app 聊天框长按测试"""
        appPackage = 'com.tencent.mm'
        appActivity = ".ui.LauncherUI"
        # 跳转到微信
        self.driver.start_activity(appPackage, appActivity)
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # # 获取当前分辨率
        # el_x = driver.get_window_size()['width']
        # el_y = driver.get_window_size()['height']
        # # 点击"<"
        # driver.tap([((45/1080)*el_x, (179/2288)*el_y)])
        # # 点击“去聊天使用”
        # driver.find_element_by_id(f"{appPackage}:id/go_main_btn").click()
        # 点击“我”
        driver.find_elements_by_id("com.tencent.mm:id/icon_iv")[3].click()
        # 获取微信名
        name = driver.find_element_by_id("com.tencent.mm:id/nick_name_tv").text
        # 点击通讯录
        driver.find_elements_by_id(f"{appPackage}:id/icon_iv")[1].click()
        # 点击聊天对象
        driver.find_element_by_xpath(f"//android.view.View[@text='{name}']").click()
        # 点击发消息
        driver.find_element_by_id(f"{appPackage}:id/text").click()
        # 点击输入框
        driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").click()
        # 等待输入法弹出
        sleep(2)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        # 触发长按操作
        action = TouchAction(driver)
        # 1
        action.long_press(x=(321/1080)*el_x, y=(1739/2288)*el_y, duration=0).move_to(x=(210/1080)*el_x, y=(1611/2288)*el_y).release().perform()
        # @
        action.long_press(x=(321/1080)*el_x, y=(1739/2288)*el_y, duration=0).move_to(x=(332/1080)*el_x, y=(1617/2288)*el_y).release().perform()
        # #
        action.long_press(x=(321/1080)*el_x, y=(1739/2288)*el_y, duration=0).move_to(x=(437/1080)*el_x, y=(1611/2288)*el_y).release().perform()
        # 2
        action.long_press(x=(537/1080)*el_x, y=(1744/2288)*el_y).release().perform()
        # 3
        action.long_press(x=(786/1080)*el_x, y=(1739/2288)*el_y).release().perform()
        # 4
        action.long_press(x=(293/1080)*el_x, y=(1894/2288)*el_y).release().perform()
        # 5
        action.long_press(x=(570/1080)*el_x, y=(1910/2288)*el_y).release().perform()
        # 6
        action.long_press(x=(764/1080)*el_x, y=(1916/2288)*el_y).release().perform()
        # 7
        action.long_press(x=(304/1080)*el_x, y=(2071/2288)*el_y).release().perform()
        # 8
        action.long_press(x=(509/1080)*el_x, y=(2076/2288)*el_y).release().perform()
        # 9
        action.long_press(x=(769/1080)*el_x, y=(2082/2288)*el_y).release().perform()

        # 获取上屏内容
        text = driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def bili_chinese_words(self):
        """B站app 中文词汇测试"""
        appPackage = "tv.danmaku.bili"
        appActivity = ".MainActivityV2"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到B站
        driver.start_activity(appPackage, appActivity)
        # 如果有”青少年模式“， 则点击”我知道了“
        try:
            iknow = driver.find_element_by_id("tv.danmaku.bili:id/text3")
        except NoSuchElementException:
            print("没有‘青少年模式’界面!")
        else:
            iknow.click()
        # 如果有登录界面， 则点击”x“
        try:
            driver.find_element_by_id("tv.danmaku.bili:id/dialog_container")
        except NoSuchElementException:
            print("没有登陆界面!")
        else:
            driver.find_element_by_id(f"{appPackage}:id/close").click()
        # 点击搜索框
        driver.find_element_by_id(f"{appPackage}:id/expand_search").click()
        sleep(2)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        driver.tap([((769/1080)*el_x, (2082/2288)*el_y), ((786/1080)*el_x, (1739/2288)*el_y)], 0)  # we
        driver.tap([((293/1080)*el_x, (1894/2288)*el_y), ((769/1080)*el_x, (2082/2288)*el_y)], 0)  # ix
        driver.tap([((293/1080)*el_x, (1894/2288)*el_y), ((764/1080)*el_x, (1916/2288)*el_y)], 0)  # in
        # 选择待选框的第一个词
        driver.tap([((101/1080)*el_x, (1613/2288)*el_y)], 0)
        # 获取上屏内容
        text = driver.find_element_by_id(f"{appPackage}:id/search_src_text").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def douyin_letters_26(self):
        """抖音app 26字母测试"""
        appPackage = "com.ss.android.ugc.aweme"
        appActivity = ".splash.SplashActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到抖音
        driver.start_activity(appPackage, appActivity)
        # 如果有”青少年模式“， 则点击”我知道了“
        try:
            iknow = driver.find_element_by_id("com.ss.android.ugc.aweme:id/+a")
        except NoSuchElementException:
            print("没有‘青少年模式’界面!")
        else:
            iknow.click()
        # 如果有上滑提示，则上滑
        driver.swipe(start_x=533, start_y=2096, end_x=533, end_y=1096)
        # 如果有登陆界面， 则点击”X“
        try:
            iknow = driver.find_element_by_id("com.ss.android.ugc.aweme:id/close")
        except NoSuchElementException:
            print("没有登录界面!")
        else:
            iknow.click()
        # 获取当前分辨率
        el_x = driver.get_window_size()['width']
        el_y = driver.get_window_size()['height']
        # 点击搜索
        driver.tap([((975/1080)*el_x, (178/2288)*el_y)])
        sleep(1)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        # 中英文切换，触发后为英文
        driver.tap([((772/1080)*el_x, (2264/2288)*el_y)], 0)
        # 26字母 根据坐标找到键盘对应键, 注意坐标不要忘记括号（）
        driver.tap([((72/1080)*el_x, (1722/2288)*el_y), ((166/1080)*el_x, (1728/2288)*el_y), ((265/1080)*el_x, (1755/2288)*el_y), ((382/1080)*el_x, (1739/2288)*el_y), ((487/1080)*el_x, (1744/2288)*el_y)], 0)  # qwert
        driver.tap([((587/1080)*el_x, (1739/2288)*el_y), ((697/1080)*el_x, (1739/2288)*el_y), ((797/1080)*el_x, (1728/2288)*el_y), ((930/1080)*el_x, (1739/2288)*el_y), ((1008/1080)*el_x, (1722/2288)*el_y)], 0)  # yuiop
        driver.tap([((121/1080)*el_x, (1905/2288)*el_y), ((216/1080)*el_x, (1888/2288)*el_y), ((321/1080)*el_x, (1905/2288)*el_y), ((437/1080)*el_x, (1894/2288)*el_y), ((542/1080)*el_x, (1910/2288)*el_y)], 0)  # asdfg
        driver.tap([((659/1080)*el_x, (1888/2288)*el_y), ((742/1080)*el_x, (1905/2288)*el_y), ((847/1080)*el_x, (1888/2288)*el_y), ((980/1080)*el_x, (1905/2288)*el_y), ((232/1080)*el_x, (2088/2288)*el_y)], 0)  # hjklz
        driver.tap([((348/1080)*el_x, (2088/2288)*el_y), ((432/1080)*el_x, (2082/2288)*el_y), ((542/1080)*el_x, (2071/2288)*el_y), ((642/1080)*el_x, (2065/2288)*el_y), ((736/1080)*el_x, (2082/2288)*el_y)], 0)  # xcvbn
        driver.tap([((852/1080)*el_x, (2060/2288)*el_y)], 0)  # qwert
        # 获取搜索框中的内容
        text = driver.find_element_by_id("com.ss.android.ugc.aweme:id/et_search_kw").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def qq_number(self):
        """QQ登录界面 9宫格数字"""
        appPackage = "com.tencent.mobileqq"
        appActivity = ".activity.SplashActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到QQ
        driver.start_activity(appPackage, appActivity)
        try:
            # 如果有服务协议和隐私政策界面
            agree = driver.find_element_by_id(f"{appPackage}:id/dialogRightBtn")
        except NoSuchElementException:
            print("没有‘服务协议和隐私政策’界面!")
        else:
            agree.click()
        # 登录界面，选择登录
        driver.find_element_by_id(f"{appPackage}:id/btn_login").click()
        # 点击账号框
        driver.find_element_by_class_name("android.widget.EditText").click()
        sleep(1)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        driver.tap([((294/1080)*el_x, (2243/2288)*el_y)], 0)  # 触发切换数字元素
        driver.tap([((310/1080)*el_x, (1739/2288)*el_y), ((537/1080)*el_x, (1744/2288)*el_y)], 0)  # 12
        driver.tap([((786/1080)*el_x, (1739/2288)*el_y), ((293/1080)*el_x, (1894/2288)*el_y)], 0)  # 34
        driver.tap([((570/1080)*el_x, (1910/2288)*el_y), ((764/1080)*el_x, (1916/2288)*el_y)], 0)  # 56
        driver.tap([((970/1080)*el_x, (1917/2288)*el_y), ((304/1080)*el_x, (2071/2288)*el_y)], 0)  # 空格7
        driver.tap([((509/1080)*el_x, (2076/2288)*el_y), ((769/1080)*el_x, (2082/2288)*el_y)], 0)  # 89
        driver.tap([((979/1080)*el_x, (2119/2288)*el_y), ((537/1080)*el_x, (2254/2288)*el_y)], 0)  # @0
        driver.tap([((758/1080)*el_x, (2239/2288)*el_y)], 0)  # .

        # 获取以上输入，判断是否正确
        text = driver.find_element_by_class_name("android.widget.EditText").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def qq_symbol(self):
        """QQ登录界面 9宫格符号"""
        appPackage = "com.tencent.mobileqq"
        appActivity = ".activity.SplashActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到QQ
        driver.start_activity(appPackage, appActivity)
        try:
            # 如果有服务协议和隐私政策界面
            agree = driver.find_element_by_id(f"{appPackage}:id/dialogRightBtn")
        except NoSuchElementException:
            print("没有‘服务协议和隐私政策’界面!")
        else:
            agree.click()
        # 登录界面，选择登录
        driver.find_element_by_id(f"{appPackage}:id/btn_login").click()
        # 点击密码框
        driver.find_elements_by_class_name("android.widget.EditText")[1].click()
        # 点击隐藏密码
        driver.find_element_by_id("com.tencent.mobileqq:id/fiu")
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        # 数字
        driver.tap([((335/1080)*el_x, (1733/2288)*el_y)], 0)  # 1
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((556/1080)*el_x, (1747/2288)*el_y)], 0)  # 2
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((749/1080)*el_x, (1747/2288)*el_y)], 0)  # 3
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((960/1080)*el_x, (1733/2288)*el_y)], 0)  # 4
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((321/1080)*el_x, (1889/2288)*el_y)], 0)  # 5
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((528/1080)*el_x, (1894/2288)*el_y)], 0)  # 6
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((758/1080)*el_x, (1885/2288)*el_y)], 0)  # 空格
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((956/1080)*el_x, (1889/2288)*el_y)], 0)  # 7
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((326/1080)*el_x, (2022/2288)*el_y)], 0)  # 8
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((542/1080)*el_x, (2013/2288)*el_y)], 0)  # 9
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((749/1080)*el_x, (2022/2288)*el_y)], 0)  # @
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((974/1080)*el_x, (2018/2288)*el_y)], 0)  # 0
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((335/1080)*el_x, (2142/2288)*el_y)], 0)  # .
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((547/1080)*el_x, (2147/2288)*el_y)], 0)  # 7
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((772/1080)*el_x, (2137/2288)*el_y)], 0)  # 8
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((979/1080)*el_x, (2042/2288)*el_y)], 0)  # 9
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((335/1080)*el_x, (2257/2288)*el_y)], 0)  # @
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((524/1080)*el_x, (2248/2288)*el_y)], 0)  # 0
        driver.tap([((110/1080)*el_x, (2234/2288)*el_y)], 0)  # 触发切换符号元素
        sleep(0.5)
        driver.tap([((758/1080)*el_x, (2248/2288)*el_y)], 0)  # .

        # 获取以上输入，判断是否正确
        text = driver.find_elements_by_class_name("android.widget.EditText")[1].text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def taobao_chinese_words(self):
        """Oppo A92 淘宝非登录界面 9宫格中文词汇"""
        appPackage = "com.taobao.taobao"
        appActivity = "com.taobao.tao.TBMainActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到淘宝
        driver.start_activity(appPackage, appActivity)
        # 点击搜索框
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]").click()
        sleep(1)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        # 输入 “连衣裙”
        driver.tap([((570/1080)*el_x, (1910/2288)*el_y), ((293/1080)*el_x, (1894/2288)*el_y)], 0)  # li
        driver.tap([((537/1080)*el_x, (1744/2288)*el_y), ((764/1080)*el_x, (1916/2288)*el_y)], 0)  # an
        driver.tap([((769/1080)*el_x, (2082/2288)*el_y), ((293/1080)*el_x, (1894/2288)*el_y)], 0)  # yi
        driver.tap([((304/1080)*el_x, (2071/2288)*el_y), ((509/1080)*el_x, (2076/2288)*el_y)], 0)  # qu
        driver.tap([((764/1080)*el_x, (1916/2288)*el_y)], 0)  # mno
        driver.tap([((101/1080)*el_x, (1613/2288)*el_y)], 0)  # 选择待选框的第一个词

        # 获取上屏内容
        text = driver.find_element_by_id(f"{appPackage}:id/searchEdit").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def cloudmusic_letters(self):
        """Oppo A92 网易云 9宫格英文大小写"""
        appPackage = "com.netease.cloudmusic"
        appActivity = ".activity.LoadingActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到QQ音乐
        driver.start_activity(appPackage, appActivity)
        # try:
        #     # 如果有红包界面， 点击关闭
        #     close = driver.find_element_by_id("com.jingdong.app.mall:id/mj")
        # except NoSuchElementException:
        #     print("没有红包界面!")
        # else:
        #     close.click()
        # 获取当前分辨率
        el_x = driver.get_window_size()['width']
        el_y = driver.get_window_size()['height']
        # 点击搜索框
        driver.find_element_by_id("com.netease.cloudmusic:id/searchBar").click()
        sleep(1)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        # 中英文切换，触发后为英文
        driver.tap([((772 / 1080) * el_x, (2264 / 2288) * el_y)], 0)
        # 切换为大写
        driver.tap([((64 / 1080) * el_x, (2107 / 2288) * el_y)], 0)
        driver.tap([((110 / 1080) * el_x, (1944 / 2288) * el_y), ((736 / 1080) * el_x, (2082 / 2288) * el_y)], 0)  # An
        driver.tap([((542 / 1080) * el_x, (1910 / 2288) * el_y), ((265 / 1080) * el_x, (1755 / 2288) * el_y)], 0)  # ge
        driver.tap([((980 / 1080) * el_x, (1905 / 2288) * el_y), ((216 / 1080) * el_x, (1888 / 2288) * el_y)], 0)  # ls

        # 获取上屏内容
        text = driver.find_element_by_id("com.netease.cloudmusic:id/search_src_text").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def weixin_9input(self):
        """微信app 9宫格聊天框多次键入测试"""
        appPackage = 'com.tencent.mm'
        appActivity = ".ui.LauncherUI"
        # 跳转到微信
        self.driver.start_activity(appPackage, appActivity)
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # # 获取当前分辨率
        # el_x = driver.get_window_size()['width']
        # el_y = driver.get_window_size()['height']
        # # 点击"<"
        # driver.tap([((45 / 1080) * el_x, (179 / 2288) * el_y)])
        # # 点击“去聊天使用”
        # driver.find_element_by_id(f"{appPackage}:id/go_main_btn").click()
        # 点击“我”
        driver.find_elements_by_id("com.tencent.mm:id/icon_iv")[3].click()
        # 获取微信名
        name = driver.find_element_by_id("com.tencent.mm:id/nick_name_tv").text
        # 点击通讯录
        driver.find_elements_by_id(f"{appPackage}:id/icon_iv")[1].click()
        # 点击聊天对象
        driver.find_element_by_xpath(f"//android.view.View[@text='{name}']").click()
        # 点击发消息
        driver.find_element_by_id(f"{appPackage}:id/text").click()
        # 点击输入框
        driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").click()
        # 等待输入法弹出
        sleep(2)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        # 切换为英文模式
        driver.tap([((799 / 1080) * el_x, (2253 / 2288) * el_y)])
        # 多次键入某个字母
        getstr = self.generate_str(1)
        for i in range(65):
            if getstr == 'a':
                driver.tap([(121, 1905)])
            if getstr == 'b':
                driver.tap([(642, 2065)])
            if getstr == 'c':
                driver.tap([(432, 2082)])
            if getstr == 'd':
                driver.tap([(321, 1905)])
            if getstr == 'e':
                driver.tap([(265, 1755)])
            if getstr == 'f':
                driver.tap([(437, 1894)])
            if getstr == 'g':
                driver.tap([(542, 1910)])
            if getstr == 'h':
                driver.tap([(659, 1888)])
            if getstr == 'i':
                driver.tap([(797, 1728)])
            if getstr == 'j':
                driver.tap([(742, 1905)])
            if getstr == 'k':
                driver.tap([(847, 1888)])
            if getstr == 'l':
                driver.tap([(980, 1905)])
            if getstr == 'm':
                driver.tap([(852, 2060)])
            if getstr == 'n':
                driver.tap([(736, 2082)])
            if getstr == 'o':
                driver.tap([(930, 1739)])
            if getstr == 'p':
                driver.tap([(1008, 1722)])
            if getstr == 'q':
                driver.tap([(72, 1722)])
            if getstr == 'r':
                driver.tap([(382, 1739)])
            if getstr == 's':
                driver.tap([(216, 1888)])
            if getstr == 't':
                driver.tap([(487, 1744)])
            if getstr == 'u':
                driver.tap([(697, 1739)])
            if getstr == 'v':
                driver.tap([(542, 2071)])
            if getstr == 'w':
                driver.tap([(166, 1728)])
            if getstr == 'x':
                driver.tap([(348, 2088)])
            if getstr == 'y':
                driver.tap([(587, 1739)])
            if getstr == 'z':
                driver.tap([(232, 2088)])
        # 获取上屏内容
        text = driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").text
        os.system(f'adb shell am force-stop {appPackage}')
        return getstr, text

    def article_words(self):
        """Oppo A92 九宫格 今日头条 搜索框 中文词汇"""
        appPackage = "com.ss.android.article.news"
        appActivity = ".activity.MainActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到今日头条
        driver.start_activity(appPackage, appActivity)
        # 点击“搜索框”
        driver.find_element_by_id("com.ss.android.article.news:id/e5o").click()
        sleep(1)
        # 切换到九宫格键盘
        el_x, el_y = self.switch_to_ninekeyboard()
        driver.tap([((769 / 1080) * el_x, (2082 / 2288) * el_y), ((786 / 1080) * el_x, (1739 / 2288) * el_y)], 0)  # we
        driver.tap([((293 / 1080) * el_x, (1894 / 2288) * el_y), ((769 / 1080) * el_x, (2082 / 2288) * el_y)], 0)  # ix
        driver.tap([((293 / 1080) * el_x, (1894 / 2288) * el_y), ((764 / 1080) * el_x, (1916 / 2288) * el_y)], 0)  # in
        driver.tap([((570 / 1080) * el_x, (1910 / 2288) * el_y), ((293 / 1080) * el_x, (1894 / 2288) * el_y)], 0)  # ji
        driver.tap([((537 / 1080) * el_x, (1744 / 2288) * el_y), ((764 / 1080) * el_x, (1916 / 2288) * el_y)], 0)  # an
        driver.tap([((304 / 1080) * el_x, (2071 / 2288) * el_y), ((537 / 1080) * el_x, (1744 / 2288) * el_y)], 0)  # pa
        driver.tap([((764 / 1080) * el_x, (1916 / 2288) * el_y)], 0)  # n
        # 选择待选框的第一个词
        driver.tap([((101 / 1080) * el_x, (1613 / 2288) * el_y)], 0)
        # 获取搜索框内容
        text = driver.find_element_by_id("com.ss.android.article.news:id/e6p").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def weixin_letters(self):
        """Oppo A92 全键盘 微信搜索框 英文大小写"""
        appPackage = 'com.tencent.mm'
        appActivity = ".ui.LauncherUI"
        # 跳转到微信
        self.driver.start_activity(appPackage, appActivity)
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # # 获取当前分辨率
        # el_x = driver.get_window_size()['width']
        # el_y = driver.get_window_size()['height']
        # # 点击"<"
        # driver.tap([((45/1080)*el_x, (179/2288)*el_y)])
        # # 点击“去聊天使用”
        # driver.find_element_by_id(f"{appPackage}:id/go_main_btn").click()
        # 点击搜索框
        driver.find_element_by_id(f"{appPackage}:id/search_icon").click()
        sleep(1)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        # 切换为英文模式
        driver.tap([((799/1080)*el_x, (2253/2288)*el_y)], 0)
        # 切换为大写
        driver.tap([((64/1080)*el_x, (2107/2288)*el_y)], 0)
        driver.tap([((321/1080)*el_x, (2113/2288)*el_y), ((805/1080)*el_x, (1774/2288)*el_y)], 0)  # Xi
        driver.tap([((110/1080)*el_x, (1944/2288)*el_y), ((893/1080)*el_x, (1757/2288)*el_y)], 0)  # ao
        # 切换为大写
        driver.tap([((64/1080)*el_x, (2107/2288)*el_y)], 0)
        driver.tap([((974/1080)*el_x, (1949/2288)*el_y), ((817/1080)*el_x, (1774/2288)*el_y)], 0)  # Li
        driver.tap([((700/1080)*el_x, (1786/2288)*el_y)], 0)  # u

        # 获取搜索框内容
        text = driver.find_element_by_id(f"{appPackage}:id/edittext").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def weixin_emoji(self):
        """Oppo A92 全键盘 微信朋友圈 表情符号"""
        appPackage = 'com.tencent.mm'
        appActivity = ".ui.LauncherUI"
        # 跳转到微信
        self.driver.start_activity(appPackage, appActivity)
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 获取当前分辨率
        el_x = driver.get_window_size()['width']
        el_y = driver.get_window_size()['height']
        # # 点击"<"
        # driver.tap([((45/1080)*el_x, (179/2288)*el_y)])
        # # 点击“去聊天使用”
        # driver.find_element_by_id(f"{appPackage}:id/go_main_btn").click()
        # 点击”发现“
        driver.find_elements_by_id(f"{appPackage}:id/icon_iv")[2].click()
        # 点击朋友圈
        driver.find_element_by_id("com.tencent.mm:id/image_iv").click()
        # 长按”相机“图标
        driver.tap([((1007/1080)*el_x, (183/2288)*el_y)], 5)
        # 点击文本框
        driver.find_element_by_id("com.tencent.mm:id/sns_desc_tv").click()
        sleep(1)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        # 点击”符“
        driver.tap([((79/1080)*el_x, (2244/2288)*el_y)], 0)
        # 点击表情符号
        driver.tap([((110/1080)*el_x, (1866/2288)*el_y)], 0)
        # 点击“情绪”
        driver.tap([((456/1080)*el_x, (1725/2288)*el_y)], 0)
        # 点击emoji
        driver.tap([((304/1080)*el_x, (1856/2288)*el_y), ((535/1080)*el_x, (2008/2288)*el_y)])
        driver.tap([((760/1080)*el_x, (2018/2288)*el_y), ((419/1080)*el_x, (2155/2288)*el_y)])
        driver.tap([((765/1080)*el_x, (2181/2288)*el_y), ((309/1080)*el_x, (2176/2288)*el_y)])
        # 点击“肢体”
        driver.tap([((592/1080)*el_x, (1730/2288)*el_y)], 0)
        # 点击emoji
        driver.tap([((425/1080)*el_x, (1872/2288)*el_y), ((645/1080)*el_x, (1861/2288)*el_y)])
        driver.tap([((535/1080)*el_x, (2024/2288)*el_y), ((881/1080)*el_x, (2018/2288)*el_y)])
        driver.tap([((650/1080)*el_x, (2186/2288)*el_y), ((1001/1080)*el_x, (2170/2288)*el_y)])
        # 点击“人物”
        driver.tap([((729/1080)*el_x, (1730/2288)*el_y)], 0)
        # 点击emoji
        driver.tap([((425/1080)*el_x, (2317/2288)*el_y), ((991/1080)*el_x, (2018/2288)*el_y)])
        driver.tap([((530/1080)*el_x, (1866/2288)*el_y), ((299/1080)*el_x, (2029/2288)*el_y)])
        driver.tap([((991/1080)*el_x, (1866/2288)*el_y), ((540/1080)*el_x, (2024/2288)*el_y)])
        # 点击“动物”
        driver.tap([((870/1080)*el_x, (1741/2288)*el_y)], 0)
        # 点击emoji
        driver.tap([((304/1080)*el_x, (1861/2288)*el_y), ((540/1080)*el_x, (2165/2288)*el_y)])
        driver.tap([((650/1080)*el_x, (2323/2288)*el_y), ((771/1080)*el_x, (2070/2288)*el_y)])
        driver.tap([((876/1080)*el_x, (1872/2288)*el_y), ((545/1080)*el_x, (2018/2288)*el_y)])
        # 截图
        driver.get_screenshot_as_file("D:\wechatkeyboard-compatibility-test\Screenshots\emoji.png")
        # 点击”返回“
        driver.tap([((58/1080)*el_x, (189/2288)*el_y)])
        # 点击”不保留“
        driver.find_element_by_id("com.tencent.mm:id/mm_alert_cancel_btn").click()
        os.system(f'adb shell am force-stop {appPackage}')
        return

    def qiyi_chinese_words(self):
        """Oppo A92 全键盘 爱奇艺 中文词汇"""
        appPackage = "com.qiyi.video"
        appActivity = ".WelcomeActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到爱奇艺视频
        driver.start_activity(appPackage, appActivity)
        # 如果有广告界面，点击”关闭“
        try:
            close = driver.find_element_by_id(f"{appPackage}:id/unused_res_a")
        except NoSuchElementException:
            print("没有广告界面!")
        else:
            close.click()
        try:
            close = driver.find_element_by_id("com.qiyi.video:id/cancel_btn")
        except NoSuchElementException:
            print("没有'版本升级'界面!")
        else:
            close.click()
        # 如果有'青少年模式'界面，点击”我知道了“
        try:
            close = driver.find_element_by_id(f"{appPackage}:id/confirm_btn")
        except NoSuchElementException:
            print("没有'青少年模式'界面!")
        else:
            close.click()
        sleep(1)
        # # 如果有定位界面，点击”允许“
        # try:
        #     allow = driver.find_element_by_id("com.qiyi.video:id/confirm_btn") # com.qiyi.video:id/cancel_btn
        # except NoSuchElementException:
        #     print("No such element!")
        # else:
        #     allow.click()
        #     # 点击使用时允许
        #     driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
        # 获取当前分辨率
        el_x = driver.get_window_size()['width']
        el_y = driver.get_window_size()['height']
        # 点击搜索框
        driver.tap([((550/1080)*el_x, (178/2288)*el_y)])
        sleep(2)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        driver.tap([((742/1080)*el_x, (1905/2288)*el_y), ((697/1080)*el_x, (1739/2288)*el_y)], 0)  # ju
        driver.tap([((265/1080)*el_x, (1755/2288)*el_y), ((348/1080)*el_x, (2088/2288)*el_y)], 0)  # ex
        driver.tap([((797/1080)*el_x, (1728/2288)*el_y), ((736/1080)*el_x, (2082/2288)*el_y)], 0)  # in
        driver.tap([((542/1080)*el_x, (1910/2288)*el_y), ((736/1080)*el_x, (2082/2288)*el_y)], 0)  # gn
        driver.tap([((797/1080)*el_x, (1728/2288)*el_y), ((121/1080)*el_x, (1905/2288)*el_y)], 0)  # ia
        driver.tap([((736/1080)*el_x, (2082/2288)*el_y), ((321/1080)*el_x, (1905/2288)*el_y)], 0)  # nd
        driver.tap([((121/1080)*el_x, (1905/2288)*el_y), ((797/1080)*el_x, (1728/2288)*el_y)], 0)  # ai
        # 点击待选框中的第一个词汇
        driver.tap([((79/1080)*el_x, (1625/2288)*el_y)])
        sleep(1)
        # 获取搜索框内容
        text = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText').text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def kmusic_letters(self):
        """Oppo A92 全键盘 全民K歌 英文大小写"""
        appPackage = "com.tencent.karaoke"
        appActivity = ".module.splash.ui.SplashBaseActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到全民K歌app
        driver.start_activity(appPackage, appActivity)
        # 获取当前分辨率
        el_x = driver.get_window_size()['width']
        el_y = driver.get_window_size()['height']
        # 点击搜索按钮
        # driver.find_element_by_id(f"{appPackage}:id/bqv").click()
        driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="关注"]/android.widget.TextView')
        driver.tap([((986 / 1080) * el_x, (189 / 2288) * el_y)])
        sleep(1)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        # 切换为英文模式
        driver.tap([((799/1080)*el_x, (2253/2288)*el_y)], 0)
        # 切换为大写
        driver.tap([((64/1080)*el_x, (2107/2288)*el_y)], 0)
        driver.tap([((110/1080)*el_x, (1944/2288)*el_y), ((736/1080)*el_x, (2082/2288)*el_y)], 0)  # An
        driver.tap([((542/1080)*el_x, (1910/2288)*el_y), ((265/1080)*el_x, (1755/2288)*el_y)], 0)  # ge
        driver.tap([((980/1080)*el_x, (1905/2288)*el_y), ((216/1080)*el_x, (1888/2288)*el_y)], 0)  # ls
        # 获取搜索框内容
        text = driver.find_element_by_id("com.tencent.karaoke:id/ao3").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def zhifubao_number(self):
        """Oppo A92 全键盘 支付宝登陆界面 数字"""
        appPackage = "com.eg.android.AlipayGphone"
        appActivity = ".AlipayLogin"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到支付宝app
        driver.start_activity(appPackage, appActivity)
        # 如果有“仅充电“界面， 点击”忽略“
        try:
            ignore = driver.find_element_by_id("android:id/button2")
        except NoSuchElementException:
            print("没有‘仅充电’界面!")
        else:
            ignore.click()
        # 如果有“风险“界面， 点击”信任此连接“
        try:
            belive = driver.find_element_by_id("android:id/button2")
        except NoSuchElementException:
            print("没有‘风险’提示界面!")
        else:
            belive.click()
        # 点击手机号输入框
        driver.find_element_by_class_name("android.widget.EditText").click()
        sleep(2)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        # 切换到“123”
        driver.tap([((220/1080)*el_x, (2265/2288)*el_y)])
        driver.tap([((310/1080)*el_x, (1739/2288)*el_y), ((537/1080)*el_x, (1744/2288)*el_y), ((786/1080)*el_x, (1739/2288)*el_y), ((293/1080)*el_x, (1894/2288)*el_y), ((570/1080)*el_x, (1910/2288)*el_y)], 0)  # 12345
        driver.tap([((764/1080)*el_x, (1916/2288)*el_y), ((304/1080)*el_x, (2071/2288)*el_y), ((509/1080)*el_x, (2076/2288)*el_y), ((769/1080)*el_x, (2082/2288)*el_y), ((537/1080)*el_x, (2254/2288)*el_y)], 0)  # 67890

        # 获取输入框内容
        text = driver.find_element_by_class_name("android.widget.EditText").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def weibo_chinese_words(self):
        """Oppo A92 全键盘 微博 中文词汇"""
        appPackage = "com.sina.weibo"
        appActivity = ".SplashActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到微博
        driver.start_activity(appPackage, appActivity)
         # 点击"发现"
        driver.find_element_by_accessibility_id("发现").click()  # 通过 content_desc 属性定位元素
        # 点击“搜索框”
        driver.find_element_by_id(f"{appPackage}:id/ly_left").click()
        sleep(1)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        driver.tap([((166/1080)*el_x, (1728/2288)*el_y), ((265/1080)*el_x, (1755/2288)*el_y), ((797/1080)*el_x, (1728/2288)*el_y), ((348/1080)*el_x, (2088/2288)*el_y), ((797/1080)*el_x, (1728/2288)*el_y)], 0)  # weixi
        driver.tap([((736/1080)*el_x, (2082/2288)*el_y), ((742/1080)*el_x, (1905/2288)*el_y), ((797/1080)*el_x, (1728/2288)*el_y), ((121/1080)*el_x, (1905/2288)*el_y), ((736/1080)*el_x, (2082/2288)*el_y)], 0)  # njian
        driver.tap([((1002/1080)*el_x, (1770/2288)*el_y)], 0)  # p
        driver.tap([((121/1080)*el_x, (1905/2288)*el_y), ((736/1080)*el_x, (2082/2288)*el_y)], 0)  # an

        # 待选框第一个元素
        driver.tap([((165/1080)*el_x, (1632/2288)*el_y)])
        # 获取搜索框内容
        text = driver.find_element_by_id(f"{appPackage}:id/tv_search_keyword").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def baidu_chinese_words(self):
        """Oppo A92 全键盘 百度 中文词汇"""
        appPackage = "com.baidu.searchbox"
        appActivity = "com.baidu.searchbox.MainActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到百度
        driver.start_activity(appPackage, appActivity)
        # # 获取当前分辨率
        # el_x = driver.get_window_size()['width']
        # el_y = driver.get_window_size()['height']
        # 如果有登陆界面，点击跳过
        try:
            skip = driver.find_element_by_id("com.baidu.searchbox:id/skip")
        except NoSuchElementException:
            print("没有登录界面！")
        else:
            skip.click()
        # 如果有版本界面，点击”关闭“
        try:
            close = driver.find_element_by_accessibility_id("关闭")
        except NoSuchElementException:
            print("没有’版本升级‘界面!")
        else:
            close.click()
        # 如果有"位置信息"界面，点击关闭
        try:
            skip = driver.find_element_by_id("com.baidu.searchbox:id/bd_btn_text")
        except NoSuchElementException:
            print("没有'位置信息'界面！")
        else:
            skip.click()
        # 如果有红包界面，点击”关闭“
        try:
            skip = driver.find_element_by_id(f"{appPackage}:id/bottom_close_bt")
        except NoSuchElementException:
            print("没有红包界面!")
        else:
            skip.click()

        # 点击搜索框
        driver.find_element_by_id(f"{appPackage}:id/baidu_searchbox").click()
        sleep(1)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        driver.tap([((216/1080)*el_x, (1888/2288)*el_y), ((659/1080)*el_x, (1888/2288)*el_y)], 0)  # sh
        driver.tap([((797/1080)*el_x, (1728/2288)*el_y), ((232/1080)*el_x, (2088/2288)*el_y)], 0)  # iz
        driver.tap([((659/1080)*el_x, (1888/2288)*el_y), ((265/1080)*el_x, (1755/2288)*el_y)], 0)  # he
        driver.tap([((736/1080)*el_x, (2082/2288)*el_y), ((321/1080)*el_x, (1905/2288)*el_y)], 0)  # nd
        driver.tap([((265/1080)*el_x, (1755/2288)*el_y), ((847/1080)*el_x, (1888/2288)*el_y)], 0)  # ek
        driver.tap([((121/1080)*el_x, (1905/2288)*el_y)], 0)  # a
        # 点击待选框中的第一个词汇
        driver.tap([((79/1080)*el_x, (1625/2288)*el_y)])
        sleep(1)
        # 获取搜索框内容
        text = driver.find_element_by_id(f"{appPackage}:id/SearchTextInput").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def meituan_clicks(self):
        """Oppo A92 全键盘 美团 英文快速点击"""
        appPackage = "com.sankuai.meituan"
        appActivity = "com.meituan.android.pt.homepage.activity.MainActivity"
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # 跳转到美团app
        driver.start_activity(appPackage, appActivity)
        # 获取当前分辨率
        el_x = driver.get_window_size()['width']
        el_y = driver.get_window_size()['height']
        print(el_x)
        print(el_y)
        # 如果有温馨提示界面，点击同意
        try:
            allow = driver.find_element_by_class_name("com.sankuai.meituan:id/permission_agree_btn")
        except NoSuchElementException:
            print("没有’温馨提示‘界面!")
        else:
            allow.click()
        # 如果有“红包界面”，点击返回
        try:
            driver.find_element_by_class_name("android.widget.ImageView")
        except NoSuchElementException:
            print("没有红包界面!")
        else:
            driver.tap([((68/1080)*el_x, (189/2288)*el_y)])
        # 点击搜索框 (545, 1845)
        driver.find_element_by_id(f"{appPackage}:id/search_icon").click()
        driver.find_element_by_id(f"{appPackage}:id/search_edit").click()
        sleep(1)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        # 切换为英文模式
        driver.tap([((799/1080)*el_x, (2253/2288)*el_y)])
        driver.tap([((596/1080)*el_x, (1766/2288)*el_y), ((493/1080)*el_x, (1761/2288)*el_y), ((330/1080)*el_x, (1933/2288)*el_y), ((853/1080)*el_x, (1933/2288)*el_y), ((441/1080)*el_x, (2096/2288)*el_y)])  # ytdkc
        # 获取搜索框内容
        text = driver.find_element_by_id(f"{appPackage}:id/search_edit").text
        os.system(f'adb shell am force-stop {appPackage}')
        return text

    def weixin_input(self):
        """微信app 聊天框多次键入测试"""
        appPackage = 'com.tencent.mm'
        appActivity = '.ui.LauncherUI'
        # 跳转到微信
        self.driver.start_activity(appPackage, appActivity)
        # 切换微信输入
        driver = self.enable_WeichatIME()
        # # 获取当前分辨率
        # el_x = driver.get_window_size()['width']
        # el_y = driver.get_window_size()['height']
        # # 点击"<"
        # driver.tap([((45/1080)*el_x, (179/2288)*el_y)])
        # # 点击“去聊天使用”
        # driver.find_element_by_id(f"{appPackage}:id/go_main_btn").click()
        # 点击“我”
        driver.find_elements_by_id("com.tencent.mm:id/icon_iv")[3].click()
        # 获取微信名
        name = driver.find_element_by_id("com.tencent.mm:id/nick_name_tv").text
        # 点击通讯录
        driver.find_elements_by_id(f"{appPackage}:id/icon_iv")[1].click()
        # 点击聊天对象
        driver.find_element_by_xpath(f"//android.view.View[@text='{name}']").click()
        # 点击发消息
        driver.find_element_by_id(f"{appPackage}:id/text").click()
        # 点击输入框
        driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").click()
        # 等待输入法弹出
        sleep(2)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        # 切换为英文模式
        driver.tap([((799/1080)*el_x, (2253/2288)*el_y)])
        # 多次键入某个字母
        getstr = self.generate_str(1)
        for i in range(65):
            if getstr == 'a':
                driver.tap([(121, 1905)])
            if getstr == 'b':
                driver.tap([(642, 2065)])
            if getstr == 'c':
                driver.tap([(432, 2082)])
            if getstr == 'd':
                driver.tap([(321, 1905)])
            if getstr == 'e':
                driver.tap([(265, 1755)])
            if getstr == 'f':
                driver.tap([(437, 1894)])
            if getstr == 'g':
                driver.tap([(542, 1910)])
            if getstr == 'h':
                driver.tap([(659, 1888)])
            if getstr == 'i':
                driver.tap([(797, 1728)])
            if getstr == 'j':
                driver.tap([(742, 1905)])
            if getstr == 'k':
                driver.tap([(847, 1888)])
            if getstr == 'l':
                driver.tap([(980, 1905)])
            if getstr == 'm':
                driver.tap([(852, 2060)])
            if getstr == 'n':
                driver.tap([(736, 2082)])
            if getstr == 'o':
                driver.tap([(930, 1739)])
            if getstr == 'p':
                driver.tap([(1008, 1722)])
            if getstr == 'q':
                driver.tap([(72, 1722)])
            if getstr == 'r':
                driver.tap([(382, 1739)])
            if getstr == 's':
                driver.tap([(216, 1888)])
            if getstr == 't':
                driver.tap([(487, 1744)])
            if getstr == 'u':
                driver.tap([(697, 1739)])
            if getstr == 'v':
                driver.tap([(542, 2071)])
            if getstr == 'w':
                driver.tap([(166, 1728)])
            if getstr == 'x':
                driver.tap([(348, 2088)])
            if getstr == 'y':
                driver.tap([(587, 1739)])
            if getstr == 'z':
                driver.tap([(232, 2088)])
        # 获取上屏内容
        text = driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").text
        os.system(f'adb shell am force-stop {appPackage}')
        return getstr, text

    def generate_str(self, randomlength):
        """随机生成包含两个字符的字符串"""
        base_str = 'abcdefghijklmnopqrstuvwxyz'
        str_list = random.sample(base_str, randomlength)
        randomstr = ''.join(str_list)
        return randomstr

    def weixin_clicks(self):
        """Oppo A92 微信聊天框 中文拼音显示"""
        appPackage = 'com.tencent.mm'
        appActivity = '.ui.LauncherUI'
        # 跳转到微信
        self.driver.start_activity(appPackage, appActivity)
        # 切换到微信输入法
        driver = self.enable_WeichatIME()
        # 点击“我”
        driver.find_elements_by_id("com.tencent.mm:id/icon_iv")[3].click()
        # 获取微信名
        name = driver.find_element_by_id("com.tencent.mm:id/nick_name_tv").text
        # 点击通讯录
        driver.find_elements_by_id(f"{appPackage}:id/icon_iv")[1].click()
        # 点击聊天对象
        driver.find_element_by_xpath(f"//android.view.View[@text='{name}']").click()
        # 点击发消息
        driver.find_element_by_id(f"{appPackage}:id/text").click()
        # 点击输入框
        driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").click()
        # 等待输入法弹出
        sleep(2)
        # 切换到全键盘
        el_x, el_y = self.switch_to_fullkeyboard()
        getstr = self.generate_str(2)
        for i in range(2):
            if getstr[i] == 'a':
                driver.tap([(121, 1905)])
            if getstr[i] == 'b':
                driver.tap([(642, 2065)])
            if getstr[i] == 'c':
                driver.tap([(432, 2082)])
            if getstr[i] == 'd':
                driver.tap([(321, 1905)])
            if getstr[i] == 'e':
                driver.tap([(265, 1755)])
            if getstr[i] == 'f':
                driver.tap([(437, 1894)])
            if getstr[i] == 'g':
                driver.tap([(542, 1910)])
            if getstr[i] == 'h':
                driver.tap([(659, 1888)])
            if getstr[i] == 'i':
                driver.tap([(797, 1728)])
            if getstr[i] == 'j':
                driver.tap([(742, 1905)])
            if getstr[i] == 'k':
                driver.tap([(847, 1888)])
            if getstr[i] == 'l':
                driver.tap([(980, 1905)])
            if getstr[i] == 'm':
                driver.tap([(852, 2060)])
            if getstr[i] == 'n':
                driver.tap([(736, 2082)])
            if getstr[i] == 'o':
                driver.tap([(930, 1739)])
            if getstr[i] == 'p':
                driver.tap([(1008, 1722)])
            if getstr[i] == 'q':
                driver.tap([(72, 1722)])
            if getstr[i] == 'r':
                driver.tap([(382, 1739)])
            if getstr[i] == 's':
                driver.tap([(216, 1888)])
            if getstr[i] == 't':
                driver.tap([(487, 1744)])
            if getstr[i] == 'u':
                driver.tap([(697, 1739)])
            if getstr[i] == 'v':
                driver.tap([(542, 2071)])
            if getstr[i] == 'w':
                driver.tap([(166, 1728)])
            if getstr[i] == 'x':
                driver.tap([(348, 2088)])
            if getstr[i] == 'y':
                driver.tap([(587, 1739)])
            if getstr[i] == 'z':
                driver.tap([(232, 2088)])
        # 上屏
        driver.tap([(965, 2265)])
        # 获取输入框内容
        text1 = driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").text
        # 点击发送
        driver.tap([(959, 1421)])
        for i in range(3):
            if i == 2:
                i -= 1
            if getstr[i] == 'a':
                driver.tap([(121, 1905)])
            if getstr[i] == 'b':
                driver.tap([(642, 2065)])
            if getstr[i] == 'c':
                driver.tap([(432, 2082)])
            if getstr[i] == 'd':
                driver.tap([(321, 1905)])
            if getstr[i] == 'e':
                driver.tap([(265, 1755)])
            if getstr[i] == 'f':
                driver.tap([(437, 1894)])
            if getstr[i] == 'g':
                driver.tap([(542, 1910)])
            if getstr[i] == 'h':
                driver.tap([(659, 1888)])
            if getstr[i] == 'i':
                driver.tap([(797, 1728)])
            if getstr[i] == 'j':
                driver.tap([(742, 1905)])
            if getstr[i] == 'k':
                driver.tap([(847, 1888)])
            if getstr[i] == 'l':
                driver.tap([(980, 1905)])
            if getstr[i] == 'm':
                driver.tap([(852, 2060)])
            if getstr[i] == 'n':
                driver.tap([(736, 2082)])
            if getstr[i] == 'o':
                driver.tap([(930, 1739)])
            if getstr[i] == 'p':
                driver.tap([(1008, 1722)])
            if getstr[i] == 'q':
                driver.tap([(72, 1722)])
            if getstr[i] == 'r':
                driver.tap([(382, 1739)])
            if getstr[i] == 's':
                driver.tap([(216, 1888)])
            if getstr[i] == 't':
                driver.tap([(487, 1744)])
            if getstr[i] == 'u':
                driver.tap([(697, 1739)])
            if getstr[i] == 'v':
                driver.tap([(542, 2071)])
            if getstr[i] == 'w':
                driver.tap([(166, 1728)])
            if getstr[i] == 'x':
                driver.tap([(348, 2088)])
            if getstr[i] == 'y':
                driver.tap([(587, 1739)])
            if getstr[i] == 'z':
                driver.tap([(232, 2088)])
        # 上屏
        driver.tap([(965, 2265)])
        # 获取输入框内容
        text2 = driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").text
        # 点击发送
        driver.tap([(959, 1421)])
        for i in range(4):
            if i == 2:
                i -= 1
            elif i == 3:
                i -= 2
            if getstr[i] == 'a':
                driver.tap([(121, 1905)])
            if getstr[i] == 'b':
                driver.tap([(642, 2065)])
            if getstr[i] == 'c':
                driver.tap([(432, 2082)])
            if getstr[i] == 'd':
                driver.tap([(321, 1905)])
            if getstr[i] == 'e':
                driver.tap([(265, 1755)])
            if getstr[i] == 'f':
                driver.tap([(437, 1894)])
            if getstr[i] == 'g':
                driver.tap([(542, 1910)])
            if getstr[i] == 'h':
                driver.tap([(659, 1888)])
            if getstr[i] == 'i':
                driver.tap([(797, 1728)])
            if getstr[i] == 'j':
                driver.tap([(742, 1905)])
            if getstr[i] == 'k':
                driver.tap([(847, 1888)])
            if getstr[i] == 'l':
                driver.tap([(980, 1905)])
            if getstr[i] == 'm':
                driver.tap([(852, 2060)])
            if getstr[i] == 'n':
                driver.tap([(736, 2082)])
            if getstr[i] == 'o':
                driver.tap([(930, 1739)])
            if getstr[i] == 'p':
                driver.tap([(1008, 1722)])
            if getstr[i] == 'q':
                driver.tap([(72, 1722)])
            if getstr[i] == 'r':
                driver.tap([(382, 1739)])
            if getstr[i] == 's':
                driver.tap([(216, 1888)])
            if getstr[i] == 't':
                driver.tap([(487, 1744)])
            if getstr[i] == 'u':
                driver.tap([(697, 1739)])
            if getstr[i] == 'v':
                driver.tap([(542, 2071)])
            if getstr[i] == 'w':
                driver.tap([(166, 1728)])
            if getstr[i] == 'x':
                driver.tap([(348, 2088)])
            if getstr[i] == 'y':
                driver.tap([(587, 1739)])
            if getstr[i] == 'z':
                driver.tap([(232, 2088)])
        # 上屏
        driver.tap([(965, 2265)])
        # 获取输入框内容
        text3 = driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").text
        # 点击发送
        driver.tap([(959, 1421)])
        os.system(f'adb shell am force-stop {appPackage}')
        return getstr, text1, text2, text3

