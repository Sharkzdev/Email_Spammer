from email.message import EmailMessage
import ssl
import smtplib
import time

email_sender = 'email'
password = 'password'
email_receiver = str(input('To email: '))

subject = '1'
body = '1'

email_number = int(input('how many emails: '))

for i in range(email_number):

    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    ctx = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=ctx) as smtp:
        smtp.login(email_sender,password)
        
        smtp.sendmail(email_sender,email_receiver, em.as_string())
        subject = subject + '1'
        time.sleep(0.00000001)
