#Documentacion https://docs.python.org/3.7/library/smtplib.html
"""Si esta activada la doble autenticacion en gmail, hay que habilitar 
   una contraseña de autenticacion para poder hacer login de forma correcta
   https://support.google.com/mail/answer/185833?hl=es  """

import smtplib
import argparse

user = "yourmail@gmail.com"
password = "yourpassword"

def gmail_send(From, to, subject, body):
    gmail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    gmail_server.ehlo()
    gmail_server.login(user, password)
    gmail_server.sendmail(From, to, subject, body)
    gmail_server.quit()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='send mail from gmail',
                                     epilog="Example: python3 sendgmail.py -f frommail@gmail.com -t examplemail@server.com -s 'subject' -m 'text body'")

    parser.add_argument('-f', '--From', help='-f address', type=str)
    parser.add_argument('-t', '--to', help='-t address', type=str)
    parser.add_argument('-s', '--subject', help='"text subject"', type=str)
    parser.add_argument('-m', '--body', help='"text msg"', type=str)

    args = parser.parse_args()
    
    gmail_send(args.From, args.to, args.subject, args.body)
    