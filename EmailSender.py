from email.message import EmailMessage
import ssl 
import smtplib

#Start Set Email and Password
 
Email_Sender   = "kfnvfkbknb@gmail.com" # you should change it
Email_Password = "rrknrknr" #you should change it

#Finish Set Email and Password
 
# Start Set Subject and Body


Email_reciver = "saxiyoj697@hapincy.com" # you should change it

Subject = "This text forr Subject"

body  = """This Text for body of this email """


# Finish Set Subject and Body 

em = EmailMessage()
em["From"]    = Email_Sender
em["To"]      = Email_reciver
em["Subject"] = Subject
em.set_content(body)

Context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp@gmail.com",465, context=Context) as smtp  :
    smtp.login(Email_Sender,Email_Password)
    smtp.sendmail(Email_Sender , Email_reciver , em.as_string())