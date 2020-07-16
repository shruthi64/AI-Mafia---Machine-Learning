import smtplib
import getpass
from email.mime.text import MIMEText

def send_mail():
    sender_addr="xyz@gmail.com"
    password=getpass.getpass()
    subject="Learn.Inspire.Grow"
    msg='''
    Hello Everyone!
    We are pleased to announce that we are going to start a new batch of AI Mafia, Hope you will join!
    
    Thank you!
    Shruthi  
    '''
    #sever initialisation
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_addr,password)
    recipients = ['xyz@gmail.com','abc@gmail.com']

    #draft my message body
    msg=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=sender_addr
    msg['To']=', '.join(recipients)
    msg.set_param('importance','high value')


    server.sendmail(sender_addr,recipients,msg.as_string())

send_mail()