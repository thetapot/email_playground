from pathlib import Path
from string import Template
import smtplib
from email.message import EmailMessage

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '.'
email['to'] = 'receiver@gmail.com'
email['subject'] = 'My Last Email of the Day'

email.set_content(html.substitute(name='JOJO'),'html')




with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('send@gmail.com', 'email app password')
    smtp.send_message(email)
    print('Email Sent!')