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

 mail = maildesk.Client(imap_server,imap_port,smtp_server,smtp_port)
 ```

[Complete list of functions](https://github.com/khezen/maildesk/blob/master/pkg/client.py)


## Examples

### send email

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.send_email('recipient@email.com','subject','message body')
```

### select folder

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.select('Inbox')
```

### email ID

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.select('Inbox')
date = datetime.date(1970, 1, 1)

all_ids = mail.all_ids_since(date)
unread_ids = mail.unread_ids_since(date)
read_ids = mail.read_ids_since(date)
latest_id = mail.latest_id_since(date)
latest_unread_id = mail.latest_unread_id_since(date)
latest_read_id = mail.latest_read_id_since(date)
```

### email content

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.select('Inbox')
date = datetime.date(1970, 1, 1)
id = mail.latest_unread_id_since(date)

email_message = mail.get_email(id)
print mail.mail_body(email_message)
print mail.mail_subject(email_message)
print mail.mail_from(email_message)
print mail.mail_to(email_message)
attachments = mail.mail_attachments(email_message)
for key,value in attachments.items():
    file_name = key
    file_bytes = value
```
