import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

#get password from environment
pw = ""
with open(".env", "r") as file:
    pw = file.readline()

def sendEmailTo(email):

    sender_email = "vedt1145@gmail.com"
    rec_email = email
    password = pw
    subject = "Email with Attachment"
    body = "Hey, this email has an attachment."

    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = rec_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach the file
    attachment_path = "/Users/vedtiwari/Desktop/Zywa Project/static/output.pdf"  # Replace with the actual path to your attachment
    attachment = open(attachment_path, "rb").read()

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename=output.pdf")
    message.attach(part)

# Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success")
        server.sendmail(sender_email, rec_email, message.as_bytes())
        print("Email with attachment has been sent to", rec_email)
    except Exception as e:
        print("Error:", e)
    finally:
        server.quit()
