from email.message import EmailMessage
import ssl
import smtplib

email_sender = "akashmajumdar1997@gmail.com"
email_password = "jsls eliu upyx pbau"
email_reciever = "divyasinghdivi9@gmail.com"
subject = "Motapa"
body = """
Thoda Exercise karle mote
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context  = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())


# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def send_email(sender_email, password, receiver_email, subject, message):
#     # Configure the email content
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(message, 'plain'))

#     # Connect to the SMTP server
#     try:
#         server = smtplib.SMTP('smtp.yourprovider.com', 587)  # Example SMTP server
#         server.starttls()  # Secure the connection
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())
#         print('Email sent successfully!')
#     except Exception as e:
#         print(f'Something went wrong... {e}')
#     finally:
#         server.quit()

# # Example usage
# # send_email('your_email@gmail.com', 'your_password', 'recipient@example.com', 'Test Email', 'This is a test message.')
# send_email('akashmajumdar1997@gmail.com', '97akashmaj97', 'akashmajumdar.cse16@nituk.ac.in', 'Test Email', 'This is a test message.')
