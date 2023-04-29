''' You work at a company that sends daily reports to clients via email. 
The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:'''
import smtplib, ssl
from email.message import EmailMessage
import mimetypes
import os
import schedule

    # Use the smtplib library to connect to the email server and send the emails.
port = 465
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()
sender_email = "hcpieck@gmail.com"
password = input("Enter password: ")

    # Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.
def report():
    message = EmailMessage()
    message["From"] = sender_email
    message["Subject"] = "The subject of this email"
    message.set_content("""This is a Pythonic message.""")
    return message
    
    
message = report()
    
    # Use the os library to access the report files that need to be sent.
directory = "Sessions/0425_B2_session6/email_reports"

def report_message(message):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        attachment_filename = os.path.basename(path)
        if not os.path.isfile(path):
            continue
        ctype, encoding = mimetypes.guess_type(path)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        with open(path, "rb") as attachment:
            message.add_attachment(attachment.read(),
                                   maintype = maintype,
                                   subtype = subtype,
                                   filename=attachment_filename)
    return message


reports_email = report_message(message)
        
    # Use a for loop to iterate through the list of recipients and send the email and attachment.
recipients = ["martijnnieuwland@outlook.com", "martijnnieuwland@me.com", "info@martijn-nieuwland.nl"]

    # Use the schedule library to schedule the script to run daily at a specific time.


    # You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process.

def send_report():
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login("hcpieck@gmail.com", password)
            for receiver in recipients:
                reports_email["To"] = receiver
                server.send_message(reports_email)
                with open("report_log.txt", "a") as log:
                    log.write(f"{reports_email}")
    except Exception as error:
            with open("report_log.txt", "a") as log:
                log.write(f"There was an error: {error}\n")

    
schedule.every().day.at("14:00").do(send_report)

while True:
    schedule.run_pending()
    