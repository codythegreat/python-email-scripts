#!/usr/bin/env python3
# call in the following manner to send your arguments as an email
# send-arg-as-email.py subject 'body'
import sys
import yagmail

receiver = 'put a receiving email here'

# send the email using yag
yag = yagmail.SMTP('put your email here').send(
    to=receiver,
    subject=sys.argv[-2],
    contents=sys.argv[-1]
)