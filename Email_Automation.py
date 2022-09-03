from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'codywatts019@gmail.com'
email_password = 'lnsajzhtdllcmduj'

email_reciver = ''

subject = "Dont forget to respond."
body = """
When you recive an email please respond to it as soon as possible.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
