#!/usr/bin/env python3

import os
import sys
import unittest
import logging
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

logger = logging.getLogger()

"""
unittest框架执行测试并发送邮件
添加 HTMLTestRunner.py 的搜索目录，
对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append('xxx')：
"""
# 获取 当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取 HTMLTestRunner.py 所在目录
sys.path.append(os.path.join(current_dir, "HTML_Test_Runner"))
# 获取测试用例路径
case_dir = os.path.join(current_dir, "compatibility_test")
from HTML_Test_Runner import HTMLTestRunner
# from fullkeyboardtest import TestFullKeyboard
# 测试报告所在目录
report_dir = os.path.join(current_dir, "report")

def send_email(report_path):
    """
        描述：定义发送邮件:html附件
        to_list:发给谁
        sub:主题
        content:内容
        send_mail("aaa@qq.com","sub","content")
    """
    """第三方SMTP服务"""
    mail_host = 'smtp.qq.com'  # 设置服务器
    mail_port = 25  # 25 为 SMTP 默认端口号，QQ邮箱为加密传输，应使用465端口：是SSL/TLS通讯协议的
    to_list = ['1627958755@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    mail_user = '1627958755@qq.com'  # 用户名
    mail_pass = 'vwzoljxzyzbfdaii'  # 密码：授权码
    sender = "1627958755@qq.com"

    with open(report_path, 'rb') as file:
        mail_body = file.read()
        text = MIMEText(mail_body, 'html', 'utf-8')
    """创建一个带附件的实例"""
    msg = MIMEMultipart('mixed')
    """ 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf - 8设置编码"""
    # msg.attach(MIMEText('Hi！附件是微信键盘自动化测试报告，请查收，自动发送，无需回复~', 'plain', 'utf-8'))
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
    text.add_header("Content-Disposition", "attachment", filename=("utf-8", "", "微信键盘自动化测试报告.html"))
    msg.attach(text)

    msg['Subject'] = u'微信键盘自动化测试报告'  # 邮件的主题，也可以说是标题
    msg['From'] = sender  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = ",".join(to_list)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

    try:
        smtp = smtplib.SMTP(mail_host, mail_port)  # 发件人邮箱中的SMTP服务器，端口
        smtp.login(mail_user, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        smtp.sendmail(sender, to_list, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        smtp.quit()  # 关闭连接
        print("邮件发送成功", to_list)
        return True
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        return False

def new_report(testreport):
    """查找最新的测试报告"""
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new


# # SmallestService.py
# #
# # A sample demonstrating the smallest possible service written in Python.
# import win32serviceutil
# import win32service
# import win32event
# import time
# class SmallestPythonService(win32serviceutil.ServiceFramework):
#     _svc_name_ = "SmallestPythonService"
#     _svc_display_name_ = "The smallest possible Python Service"
#     def __init__(self, args):
#         win32serviceutil.ServiceFramework.__init__(self, args)
#         # Create an event which we will use to wait on.
#         # The "service stop" request will set this event.
#         self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
#     def SvcStop(self):
#         # Before we do anything, tell the SCM we are starting the stop process.
#         self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
#         # And set my event.
#         win32event.SetEvent(self.hWaitStop)
#     def SvcDoRun(self):
#         #what to do#
#         while True:
#             # f= open('c:/a.log', 'a')
#             # f.write('asdf\n')
#             # f.close()
#             # time.sleep(5)
#             # 创建测试套件
#             suite = unittest.TestSuite()
#
#             # # 通过路径加载测试用例
#             loader = unittest.TestLoader()
#             # 加载目录中所有测试用例
#             suite.addTest(loader.discover(case_dir, pattern="*test.py"))
#             # 只加载一个测试用例
#             # suite.addTest(loader.discover(case_dir, pattern="fullkeyboard_clicks.py"))
#             # # 只加载一个测试用例
#             # suite.addTest(TestFullKeyboard("test_weixin_clicks1"))
#
#             # 创建测试报告所在目录
#             if not os.path.exists(report_dir):
#                 os.makedirs(report_dir)
#             # 创建测试报告路径
#             now_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
#             report = os.path.join(report_dir, f'report_{now_time}.html')
#             with open(report, "wb") as outfile:
#                 # 创建测试运行启动器
#                 runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,  # 报告文件
#                                                        verbosity=2,  # 报告信息的详细程度
#                                                        title="微信键盘兼容性测试",  # 报告的标题
#                                                        description="微信键盘在Oppo A92手机上不同app上的兼容性测试",  # 报告中显示的描述信息
#                                                        logger=logger
#                                                        )
#                 # 使用启动器去执行测试套件中的用例
#                 runner.run(suite)
#
#             # new_report = new_report(report_dir)
#             send_email(report)
#         win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

# if __name__=='__main__':
#     win32serviceutil.HandleCommandLine(SmallestPythonService)

if __name__ == "__main__":
    # 创建测试套件
    suite = unittest.TestSuite()

    # # 通过路径加载测试用例
    loader = unittest.TestLoader()
    # 加载目录中所有测试用例
    suite.addTest(loader.discover(case_dir, pattern="*test.py"))
    # 只加载一个测试用例
    # suite.addTest(loader.discover(case_dir, pattern="fullkeyboard_clicks.py"))
    # # 只加载一个测试用例
    # suite.addTest(TestFullKeyboard("test_weixin_clicks1"))

    # 创建测试报告所在目录
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    # 创建测试报告路径
    now_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    report = os.path.join(report_dir, f'report_{now_time}.html')
    with open(report, "wb") as outfile:
        # 创建测试运行启动器
        runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,  # 报告文件
                                               verbosity=2,  # 报告信息的详细程度
                                               title="微信键盘兼容性测试",  # 报告的标题
                                               description="微信键盘在Oppo A92手机上不同app上的兼容性测试",  # 报告中显示的描述信息
                                               logger=logger
                                               )
        # 使用启动器去执行测试套件中的用例
        runner.run(suite)

    # new_report = new_report(report_dir)
    send_email(report)