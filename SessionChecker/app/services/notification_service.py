import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()


text_email =   'Confira as novas fotos em...'

from_mail = os.getenv("EMAIL_USER")
code = os.getenv("PASSWORD_USER")
to_mail = 'rodrigolorensimarques@protonmail.com'


message = MIMEMultipart()
message['From'] = from_mail
message['To'] = to_mail
message['Subject'] = 'Novas fotos'   

message.attach(MIMEText(text_email, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587)  
session.starttls()  
session.login(from_mail, code)
text = message.as_string()
session.sendmail(from_mail, to_mail, text)
session.quit()