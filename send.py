from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

class Send():
    def __init__(self):
        self.email_from = "2245575170@qq.com"  # 改为自己的发送邮箱
        self.email_to = ""  # 接收邮箱
        self.hostname = "smtp.qq.com"  # 不变，QQ邮箱的smtp服务器地址
        self.login = ""  # 发送邮箱的用户名
        self.password = "ngrfdmypxyeaeahc"  # 发送邮箱的密码，即开启smtp服务得到的授权码。注：不是QQ密码。
        self.subject = "python+smtp"  # 邮件主题
    
    def sendEmail(self,con,email_to,item,email_from):
        smtp = SMTP_SSL(self.hostname)  # SMTP_SSL默认使用465端口
        smtp.login(self.login, self.password)
        self.email_to = email_to
        self.msg = MIMEText(con, "plain", "utf-8")
        self.msg["Subject"] = Header(item, "utf-8")  #邮件主题
        self.msg["from"] = email_from
        self.msg["to"] = self.email_to

        smtp.sendmail(self.email_from, self.email_to, self.msg.as_string())
        smtp.quit()
