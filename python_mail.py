import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "sender address"
toaddr = "reciever address"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "message"

body = """ body """



msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
  
s = smtplib.SMTP('smtp.cc.iitk.ac.in', 25) 
s.ehlo()
s.starttls() 
s.login("username", "password") 
 
s.sendmail(fromaddr, toaddr, text) 

s.quit() 
