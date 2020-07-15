import email
import imaplib
import smtplib
import datetime
import email.mime.multipart
import base64
import sys

class Client():
    def __init__(self, imap_server, imap_port, smtp_server, smtp_port, max_retry_attempts):
        self.imap_server = imap_server
        self.imap_port = imap_port
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.max_retry_attempts = max_retry_attempts

    def login(self, username, password):
        self.username = username
        self.password = password
        login_attempts = 0
        while True:
            try:
                self.imap = imaplib.IMAP4_SSL(self.imap_server,self.imap_port)
                r, d = self.imap.login(username, password)
                assert r == 'OK', 'login failed: %s' % str (r)
                print(" > Signed in as %s" % self.username, d)
                return
            except Exception as err:
                login_attempts = login_attempts + 1
                if login_attempts < self.max_retry_attempts:
                    continue
                raise Exception("Error: login: %s" %str(err))

    def send_email_MIME(self, recipient, subject, message):
        msg = email.mime.multipart.MIMEMultipart()
        msg['to'] = recipient
        msg['from'] = self.username
        msg['subject'] = subject
        msg.add_header('reply-to', self.username)
        attempts = 0
        while True:
            try:
                self.smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
                self.smtp.ehlo()
                self.smtp.starttls()
                self.smtp.login(self.username, self.password)
                self.smtp.sendmail(msg['from'], [msg['to']], msg.as_string())
                print("email replied")
            except Exception as err:
                attempts = attempts + 1
                if attempts < self.max_retry_attempts:
                    continue
                raise Exception("Error: send_email_MIME: %s" %str(err))

    def send_email(self, recipient, subject, message):
        headers = "\r\n".join([
            "from: " + self.username,
            "subject: " + subject,
            "to: " + recipient,
            "mime-version: 1.0",
            "content-type: text/html"
        ])
        content = headers + "\r\n\r\n" + message
        attempts = 0
        while True:
            try:
                self.smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
                self.smtp.ehlo()
                self.smtp.starttls()
                self.smtp.login(self.username, self.password)
                self.smtp.sendmail(self.username, recipient, content)
                print("email sent")
                return
            except Exception as err:
                attempts = attempts + 1
                if attempts < self.max_retry_attempts:
                    continue
                raise Exception("Error: send_email: %s" %str(err))

    def list(self):
        return self.imap.list()

    def select(self, folder):
        return self.imap.select(folder)

    def logout(self):
        return self.imap.logout()

    def __format_date(self, date):
        return date.strftime("%d-%b-%Y")

    def all_ids_since(self, date):
        _, d = self.imap.search(None, '(SINCE "'+self.__format_date(date)+'")', 'ALL')
        list = d[0].split(' ')
        return list

    def read_ids_since(self, date):
        _, d = self.imap.search(None, '(SINCE "'+self.__format_date(date)+'")', 'SEEN')
        list = d[0].split(' ')
        return list

    def unread_ids_since(self, date):
        _, d = self.imap.search(None, '(SINCE "'+self.__format_date(date)+'")', 'UNSEEN')
        list = d[0].split(' ')
        return list

    def lates_id_since(self,date):
        list = self.all_ids_since(date)
        latest_id = list[-1]
        return latest_id

    def latest_unread_id_since(self,date):
        list = self.unread_ids_since(date)
        latest_id = list[-1]
        return latest_id

    def latest_read_id_since(self,date):
        list = self.read_ids_since(date)
        latest_id = list[-1]
        return self.get_email(latest_id)

    def get_raw_email(self,id):
        _, d = self.imap.fetch(id, "(RFC822)")
        raw_email = d[0][1]
        return raw_email

    def get_email(self, id):
        raw_email = self.get_raw_email(id)
        email_message = email.message_from_string(raw_email)
        return email_message

    def mail_body(self,email_message):
        if email_message.is_multipart():
            for payload in email_message.get_payload():
                # if payload.is_multipart(): ...
                body = (
                    payload.get_payload()
                    .split(email_message['from'])[0]
                    .split('\r\n\r\n2015')[0]
                )
                return body
        else:
            body = (
                email_message.get_payload()
                .split(email_message['from'])[0]
                .split('\r\n\r\n2015')[0]
            )
            return body
    
    def mail_attachments(self, email_message):
        attachments = {}
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if bool(filename):
                attachments[filename] = part.get_payload(decode=True)
        return attachments

    def mail_subject(self, email_message):
        return email_message['Subject']

    def mail_from(self,email_message):
        return email_message['from']

    def mail_to(self,email_message):
        return email_message['to']

    def mail_date(self,email_message):
        return email_message['date']

    def mail_return_path(self,email_message):
        return email_message['Return-Path']

    def mail_reply_to(self,email_message):
        return email_message['Reply-To']

    def mail_body_decoded(self,email_message):
        return base64.urlsafe_b64decode(self.mail_body(email_message))
    
    def set_read_only(self, folder):
        return self.imap.select(folder, readonly=True)

    def enable_write(self, folder):
        return self.imap.select(folder, readonly=False)
