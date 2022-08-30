from email.message import EmailMessage
from password import Password
import ssl
import smtplib

sender = 'xplosive.virus@gmail.com'
password = Password.hidden_password         # Put app password generated after enabling 2-factor verification.
                                            # I have imported plain text from other file for privacy.

receiver = ['2019nishant.pathare@ves.ac.in', 'nishant.pathare.21@gmail.com']

subject = 'Request to give all your money to me. Not a SCAM'
body = """
Dear Sir/Ma'am,
Hope you are having a wonderful day. Kindly transfer all your details to my
bank account immediately. This is not a scam. Just a good old fashioned robbery.
Hope you have a wonderful day.

Yours truly,
Rob
"""

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, em.as_string())

print("Email sent successfully")
