import logging
import os
from time import sleep
from wechatkeyboardbase import WeChatIputTestBase

logger = logging.getLogger()

class TestClicks(WeChatIputTestBase):
    def test_weixin_clicks(self):
        """Oppo A92 微信聊天框 中文拼音显示"""
        appPackage = 'com.tencent.mm'
        appActivity = '.ui.LauncherUI'
        # 跳转到微信
        self.auto.driver.start_activity(appPackage, appActivity)
        # 切换到微信输入法
        driver = self.auto.enable_WeichatIME()
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
        el_x, el_y = self.auto.switch_to_fullkeyboard()
        while True:
            str = self.auto.generate_str(2)
            for i in range(2):
                if str[i] == 'a':
                    driver.tap([(121, 1905)])
                if str[i] == 'b':
                    driver.tap([(642, 2065)])
                if str[i] == 'c':
                    driver.tap([(432, 2082)])
                if str[i] == 'd':
                    driver.tap([(321, 1905)])
                if str[i] == 'e':
                    driver.tap([(265, 1755)])
                if str[i] == 'f':
                    driver.tap([(437, 1894)])
                if str[i] == 'g':
                    driver.tap([(542, 1910)])
                if str[i] == 'h':
                    driver.tap([(659, 1888)])
                if str[i] == 'i':
                    driver.tap([(797, 1728)])
                if str[i] == 'j':
                    driver.tap([(742, 1905)])
                if str[i] == 'k':
                    driver.tap([(847, 1888)])
                if str[i] == 'l':
                    driver.tap([(980, 1905)])
                if str[i] == 'm':
                    driver.tap([(852, 2060)])
                if str[i] == 'n':
                    driver.tap([(736, 2082)])
                if str[i] == 'o':
                    driver.tap([(930, 1739)])
                if str[i] == 'p':
                    driver.tap([(1008, 1722)])
                if str[i] == 'q':
                    driver.tap([(72, 1722)])
                if str[i] == 'r':
                    driver.tap([(382, 1739)])
                if str[i] == 's':
                    driver.tap([(216, 1888)])
                if str[i] == 't':
                    driver.tap([(487, 1744)])
                if str[i] == 'u':
                    driver.tap([(697, 1739)])
                if str[i] == 'v':
                    driver.tap([(542, 2071)])
                if str[i] == 'w':
                    driver.tap([(166, 1728)])
                if str[i] == 'x':
                    driver.tap([(348, 2088)])
                if str[i] == 'y':
                    driver.tap([(587, 1739)])
                if str[i] == 'z':
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
                if str[i] == 'a':
                    driver.tap([(121, 1905)])
                if str[i] == 'b':
                    driver.tap([(642, 2065)])
                if str[i] == 'c':
                    driver.tap([(432, 2082)])
                if str[i] == 'd':
                    driver.tap([(321, 1905)])
                if str[i] == 'e':
                    driver.tap([(265, 1755)])
                if str[i] == 'f':
                    driver.tap([(437, 1894)])
                if str[i] == 'g':
                    driver.tap([(542, 1910)])
                if str[i] == 'h':
                    driver.tap([(659, 1888)])
                if str[i] == 'i':
                    driver.tap([(797, 1728)])
                if str[i] == 'j':
                    driver.tap([(742, 1905)])
                if str[i] == 'k':
                    driver.tap([(847, 1888)])
                if str[i] == 'l':
                    driver.tap([(980, 1905)])
                if str[i] == 'm':
                    driver.tap([(852, 2060)])
                if str[i] == 'n':
                    driver.tap([(736, 2082)])
                if str[i] == 'o':
                    driver.tap([(930, 1739)])
                if str[i] == 'p':
                    driver.tap([(1008, 1722)])
                if str[i] == 'q':
                    driver.tap([(72, 1722)])
                if str[i] == 'r':
                    driver.tap([(382, 1739)])
                if str[i] == 's':
                    driver.tap([(216, 1888)])
                if str[i] == 't':
                    driver.tap([(487, 1744)])
                if str[i] == 'u':
                    driver.tap([(697, 1739)])
                if str[i] == 'v':
                    driver.tap([(542, 2071)])
                if str[i] == 'w':
                    driver.tap([(166, 1728)])
                if str[i] == 'x':
                    driver.tap([(348, 2088)])
                if str[i] == 'y':
                    driver.tap([(587, 1739)])
                if str[i] == 'z':
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
                if str[i] == 'a':
                    driver.tap([(121, 1905)])
                if str[i] == 'b':
                    driver.tap([(642, 2065)])
                if str[i] == 'c':
                    driver.tap([(432, 2082)])
                if str[i] == 'd':
                    driver.tap([(321, 1905)])
                if str[i] == 'e':
                    driver.tap([(265, 1755)])
                if str[i] == 'f':
                    driver.tap([(437, 1894)])
                if str[i] == 'g':
                    driver.tap([(542, 1910)])
                if str[i] == 'h':
                    driver.tap([(659, 1888)])
                if str[i] == 'i':
                    driver.tap([(797, 1728)])
                if str[i] == 'j':
                    driver.tap([(742, 1905)])
                if str[i] == 'k':
                    driver.tap([(847, 1888)])
                if str[i] == 'l':
                    driver.tap([(980, 1905)])
                if str[i] == 'm':
                    driver.tap([(852, 2060)])
                if str[i] == 'n':
                    driver.tap([(736, 2082)])
                if str[i] == 'o':
                    driver.tap([(930, 1739)])
                if str[i] == 'p':
                    driver.tap([(1008, 1722)])
                if str[i] == 'q':
                    driver.tap([(72, 1722)])
                if str[i] == 'r':
                    driver.tap([(382, 1739)])
                if str[i] == 's':
                    driver.tap([(216, 1888)])
                if str[i] == 't':
                    driver.tap([(487, 1744)])
                if str[i] == 'u':
                    driver.tap([(697, 1739)])
                if str[i] == 'v':
                    driver.tap([(542, 2071)])
                if str[i] == 'w':
                    driver.tap([(166, 1728)])
                if str[i] == 'x':
                    driver.tap([(348, 2088)])
                if str[i] == 'y':
                    driver.tap([(587, 1739)])
                if str[i] == 'z':
                    driver.tap([(232, 2088)])
            # 上屏
            driver.tap([(965, 2265)])
            # 获取输入框内容
            text3 = driver.find_element_by_id(f"{appPackage}:id/chatting_content_et").text
            # 点击发送
            driver.tap([(959, 1421)])

            print(str, text1, text2, text3)
            self.assertEqual(text1, str)
            self.assertEqual(text2, str + str[-1] * 2)
            self.assertEqual(text3, str + str[-1] * 2)

            # try:
            #     self.assertEqual(text1, str)
            # except AssertionError:
            #     break
            # try:
            #     self.assertEqual(text2, str + str[-1]*2)
            # except AssertionError:
            #     break
            # try:
            #     self.assertEqual(text3, str + str[-1] * 2)
            # except AssertionError:
            #     break

        # os.system(f'adb shell am force-stop {appPackage}')