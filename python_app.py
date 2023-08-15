from email.message import EmailMessage
from multiprocessing import context
import smtplib
import ssl
import smtplib 

email_sender = 'awanishyadav996@gmail.com'
email_passward = 'llfxrcidiwybnadh'  #create a passward for the python form account then insert password

email_reciver = 'awanishyadav0026@gmail.com'

subject = "Subject of Email"
body = """
By hacker
"""


em = EmailMessage()
em['From']=email_sender
em['To'] = email_reciver
em['subject']= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_passward)
    smtp.sendmail(email_sender,email_reciver,em.as_string())



