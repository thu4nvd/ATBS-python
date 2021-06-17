import smtplib
from email.mime.text import MIMEText
from datetime import date, datetime

SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
SMTP_USERNAME = "tvuduc"
SMTP_PASSWORD = "lsmuzcazpwkozfiu"
EMAIL_FROM = "tvuduc@yahoo.com"
EMAIL_TO = "t.vuduc@bouygues-construction.com"
EMAIL_SUBJECT = "Testing Time: "
today = date.today()
now = datetime.now()

co_msg = """
Testing email externe
----------
[Company]
Where:          [Etown 4 Tân Bình]
Time:           [appointmentTime]
Company URL:    [bouygues-construction.com ]
Email:          [t.vuduc@bouygues-construction.com]
Content:        Interview
"""
def send_email():
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT + today.strftime("%d/%m/%Y") + now.strftime("%H:%M:%S")
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send_email()