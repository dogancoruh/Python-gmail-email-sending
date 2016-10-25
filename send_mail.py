##############################################
#                                            #
#   MikroKit                                 #
#   Python Gmail Mail Sending       		 #
#   29.10.2014                               #
#   Dogan Coruh                              #
#                                            #
##############################################

# importing mail library
import smtplib

# importing multipart and text libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# defining sender and destination email addresses
sender = "enter_sender_email_address" # sender     ex: sender@address.net
to = "enter_recepient_email_address" # recepient ex: recepient@address.net

# defining username and password to send mail
server_username = 'gmail_account_username' # ex: sender@gmail.com
server_password = 'gmail_account_password' # ex: 12345678

# fixed gmail smtp server address and port
server_address = "smtp.gmail.com"
server_port = 587

# defining mail content
message = MIMEMultipart('alternative')
message['Subject'] = "Email from Raspberry Pi!"
message['From'] = sender
message["To"] = to

# if you want to send plain text, use this block
text = "This is a plain text that has been sent from Raspberry Pi!"
part1 = MIMEText(text, 'plain')
message.attach(part1)

# if you want to send html content, use this
html = "<html><head></head><body><p>Hi!</p><br/>This is an html content that has been sent from Raspberry Pi!</b>!</body></html>"
part2 = MIMEText(html, 'html')
message.attach(part2)

# sending mail
smtp = smtplib.SMTP(server_address, server_port)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(server_username, server_password)
smtp.sendmail(sender, to, message.as_string())
smtp.quit()
