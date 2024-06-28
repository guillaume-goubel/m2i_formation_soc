import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

user_credential = "ca8887fad0c242"
user_password = "c5d694d4779fe9"

def send_email(body_message):
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    message = MIMEMultipart()
    message["Subject"] = "threats report"
    message["From"] = sender
    message["To"] = receiver

    message.attach(MIMEText(body_message, "plain"))

    try:
        with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
            server.starttls()
            server.login(user_credential, user_password)
            server.sendmail(sender, receiver, message.as_string())
            print("Email envoyé avec succès!")
    except smtplib.SMTPException as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")