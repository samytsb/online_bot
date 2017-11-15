#!/usr/bin/env python
# coding=utf-8
import urllib2
import smtplib
import os
import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    print "lol"
    while 1:
        time.sleep(30)
        contents = urllib2.urlopen("https://www.online.net/fr/serveur-dedie/dedibox-xc").read().decode("utf-8")
        nb = contents.count("Victime de son succès")
        print("Dispo srv : ", nb)
        if True:
            TO = 'samytsb@gmail.com'
            SUBJECT = 'Serveur Online'
            TEXT = 'Go commander https://www.online.net/fr/serveur-dedie/dedibox-xc.'

            # Gmail Sign In
            gmail_sender = 'mailautosamy@gmail.com'
            gmail_passwd = '8XLdZbZF7W'

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_sender, gmail_passwd)

            BODY = '\r\n'.join(['To: %s' % TO,
                                'From: %s' % gmail_sender,
                                'Subject: %s' % SUBJECT,
                                '', TEXT])

            server.sendmail(gmail_sender, [TO], BODY)
            server.quit()
            return



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
