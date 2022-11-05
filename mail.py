from email.mime.text import MIMEText
from email.header import Header
import smtplib
def mail(smtp_server,from_email,password,to_email,Subject,message):
    #print('正在初始化')
    msg = MIMEText(message,'plain','utf-8')

    msg['Subject'] = Header(Subject,'utf-8')
    msg['From'] = Header(from_email)
    msg['To'] = Header(to_email,'utf-8')

    from_addr = from_email
    to_addr = to_email


    try:
        server = smtplib.SMTP(smtp_server,587)
        server.starttls()
        #print('开始登录')
        server.login(from_addr,password)
        #print('登录成功')
        #print("邮件开始发送")
        server.sendmail(from_addr,to_addr,msg.as_string())
        server.quit()
        #print("邮件发送成功")
        return 0
    except smtplib.SMTPException as e:
        return "send mail erorr:"+e


