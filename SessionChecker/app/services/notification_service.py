import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

def send_email(to_email, text_email, subject_email):
    load_dotenv()


    from_email = os.getenv("EMAIL_USER")
    code = os.getenv("PASSWORD_USER")

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject_email  

    message.attach(MIMEText(text_email, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)  
    session.starttls()  
    session.login(from_email, code)
    text = message.as_string()
    session.sendmail(from_email, to_email, text)
    session.quit()