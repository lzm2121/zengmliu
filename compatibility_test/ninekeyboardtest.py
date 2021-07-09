#!/usr/bin/env python3
"""
九宫格键盘测试
"""
import logging
import wechatkeyboardbase

logger = logging.getLogger()

"""
(537, 1744) # abc
(786, 1739) # def
(293, 1894) # ghi
(570, 1910) # jkl
(764, 1916) # mno
(304, 2071) # pqrs
(509, 2076) # tuv
(769, 2082) # wxyz
"""

class TestNineKeyboard(wechatkeyboardbase.WeChatIputTestBase):
    def test_note_press_letters(self):
        """Oppo A92便签 9宫格英文长按"""
        text = self.auto.note_press_letters()
        print(text)
        self.assertEqual(text, "\"、~:;?!#.\"")

    def test_weixin_press(self):
        """Oppo A92 微信聊天框 9宫格长按"""
        text = self.auto.weixin_press()
        print(text)
        self.assertEqual(text, '1@#23456789')

    def test_douyin_letters_26(self):
        """Oppo A92 抖音 9宫格26字母"""
        text = self.auto.douyin_letters_26()
        print(text)
        self.assertEqual(text, "qwertyuiopasdfghjklzxcvbnm")

    def test_bili_chinese_words(self):
        """Oppo A92 哔哩哔哩 非登录界面 9宫格中文词汇"""
        text = self.auto.bili_chinese_words()
        print(text)
        self.assertEqual(text, "微信")

    def test_qq_number(self):
        """Oppo A92 QQ登录界面 账号框 9宫格数字"""
        text = self.auto.qq_number()
        print(text)
        self.assertEqual(text, "123456空格789@0.")
        # 备注：在真机上输入为"123456 789@0."，但测试时为”123456空格789@0.“

    def test_qq_symbol(self):
        """Oppo A92 QQ登录界面 密码框 9宫格符号"""
        text = self.auto.qq_symbol()
        print(text)
        # 符号每次出现的位置不一样，无法判断
        # self.assertEqual(text, "@.#，？'\"！?。、~;:/+*!-\"")

    def test_taobao_chinese_words(self):
        """Oppo A92 淘宝非登录界面 9宫格中文词汇"""
        text = self.auto.taobao_chinese_words()
        print(text)
        self.assertEqual(text, "连衣裙")

    def test_cloudmusic_letters(self):
        """Oppo A92 网易云 9宫格英文大小写"""
        text = self.auto.cloudmusic_letters()
        print(text)
        self.assertEqual(text, "Angels")

    def test_weixin_9input(self):
        """Oppo A92 微信聊天框 9宫格多次键入"""
        getstr, text = self.auto.weixin_9input()
        print(text)
        length = len(text)
        self.assertEqual(text, getstr * 65)
        self.assertEqual(length, 65)

    def test_article_words(self):
        """Oppo A92 今日头条 搜索框 9宫格中文词汇"""
        text = self.auto.article_words()
        print(text)
        self.assertEqual(text, "微信键盘")