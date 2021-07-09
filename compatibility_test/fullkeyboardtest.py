#!/usr/bin/env python3
"""
全键盘测试
"""
import logging
import wechatkeyboardbase

"""
(72, 1722)  # q
(166, 1728)  # w
(265, 1755)  # e
(382, 1739)  # r
(487, 1744)  # t
(587, 1739)  # y
(697, 1739)  # u
(797, 1728)  # i
(930, 1739)  # o
(1008, 1722)  # p
(121, 1905)  # a
(216, 1888)  # s
(321, 1905)  # d
(437, 1894)  # f
(542, 1910)  # g
(659, 1888)  # h
(742, 1905)  # j
(847, 1888)  # k
(980, 1905)  # l
(232, 2088)  # z
(348, 2088)  # x
(432, 2082)  # c
(542, 2071)  # v
(642, 2065)  # b
(736, 2082)  # n
(852, 2060)  # m
"""

logger = logging.getLogger()

class TestFullKeyboard(wechatkeyboardbase.WeChatIputTestBase):
    def test_weixin_letters(self):
        """Oppo A92 微信搜索框 英文大小写"""
        text = self.auto.weixin_letters()
        print(text)
        self.assertEqual(text, "XiaoLiu")

    def test_meituan_clicks(self):
        """Oppo A92 美团 英文快速点击"""
        text = self.auto.meituan_clicks()
        print(text)
        self.assertEqual(text, "ytdkc")

    def test_Kmusic_letters(self):
        """Oppo A92 全民K歌 搜索框 英文大小写"""
        text = self.auto.kmusic_letters()
        print(text)
        self.assertEqual(text, "Angels")

    def test_zhifubao_number(self):
        """Oppo A92 支付宝登陆界面 数字"""
        text = self.auto.zhifubao_number()
        print(text)
        self.assertEqual(text, "123 4567 890")

    def test_weibo_chinese_words(self):
        """Oppo A92 微博 中文词汇"""
        text = self.auto.weibo_chinese_words()
        print(text)
        self.assertEqual(text, "微信键盘")

    def test_qiyi_chinese_words(self):
        """Oppo A92 爱奇艺 中文词汇"""
        text = self.auto.qiyi_chinese_words()
        print(text)
        self.assertEqual(text, "觉醒年代")

    def test_weixin_emoji(self):
        """Oppo A92 微信朋友圈 表情符号"""
        self.auto.weixin_emoji()

    def test_baidu_chinese_words(self):
        """Oppo A92 百度 中文词汇"""
        text = self.auto.baidu_chinese_words()
        print(text)
        self.assertEqual(text, "是真的卡")

    def test_weixin_input(self):
        """Oppo A92 微信聊天框 多次键入"""
        getstr, text = self.auto.weixin_input()
        print(text)
        length = len(text)
        self.assertEqual(text, getstr * 65)
        self.assertEqual(length, 65)

    def test_weixin_clicks(self):
        """Oppo A92 微信聊天框 中文拼音显示"""
        getstr, text1, text2, text3 = self.auto.weixin_clicks()
        print(str, text1, text2, text3)
        self.assertEqual(text1, getstr)
        self.assertEqual(text2, getstr + getstr[-1])
        self.assertEqual(text3, getstr + getstr[-1] * 2)
