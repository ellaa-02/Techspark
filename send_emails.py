# a builtin module and a third-party module
# a builtin it comes with python 
# third-party module 

from smtplib import SMTP

# constant
# USERNAME = "odulajaphilip@gmail.com"
# PASSWORD = "pjxu rsny ypna vtqx"

USERNAME='oluwasegunprosperity@gmail.com'
PASSWORD='ayms bvpl jwbe ylxm'

# Create an SMTP object and establish a connection to the SMTP server
smtpObj = SMTP("smtp.gmail.com", 587)

# Secure the SMTP connection
smtpObj.starttls()

# Login to the server (if required)
smtpObj.login(USERNAME, PASSWORD)

# Send an email
from_address = USERNAME
to_address = 'emmanuellatanimowo@gmail.com'
message = """\
Subject: minecraft 

Go play minecraft with me
"""

smtpObj.sendmail(from_address, to_address, message)

# Quit the SMTP session
smtpObj.quit()