#!/usr/bin/env python
import urllib.request
import smtplib
import time

if __name__ == '__main__':
    while 1:
        time.sleep(30)
        contents = urllib.request.urlopen("https://www.online.net/fr/serveur-dedie/dedibox-xc").read().decode("utf-8")
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
            break
