# maildesk

Python Library to read email from any email service.
You can just dowload to yout python script folder or install it with pip. 
This library using Imaplib python to read email with IMAP protocol.

## Usage

```sh
pip install --user maildesk
```
 
 ```py
 import maildesk

# imap_server = "imap-mail.outlook.com"
# imap_port = 993
# smtp_server = "smtp-mail.outlook.com"
# smtp_port = 587
# imap_server = "outlook.office365.com"
# imap_port = 993
# smtp_server = "smtp.office365.com"
# smtp_port = 587
imap_server = "imap.gmail.com"
imap_port = 993
smtp_server = "smtp.gmail.com"
smtp_port = 587
max_retry_attempts = 5

 mail = maildesk.Client(imap_server,imap_port,smtp_server,smtp_port,max_retry_attempts)
 ```

[Complete list of functions](https://github.com/khezen/maildesk/blob/master/pkg/client.py)


## Examples

### send email

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.send_email('recipient@email.com','subject','message body')

```

### latest unread email in inbox

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.inbox()
print mail.latest_unread()
```

Use `mail.select(folder)` to switch to folders other than `inbox`, `junk`.

### latest unread email in inbox today

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.inbox()
print mail.latest_unread_today()
```

### latest read message in inbox

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.inbox()
print mail.latest_read()
```

### email content

```py
email_message = mail.latest_unread_today()
print mail.mail_body(email_message)
print mail.mail_subject(email_message)
print mail.mail_from(email_message)
print mail.mail_to(email_message)
print mail.mail_attachments(email_message)
```
