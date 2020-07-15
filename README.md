# maildesk

Python Library to read email from any email service, just dowload to yout python script folder. 
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
## Examples

### To get latest Unread Message in inbox:

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.inbox()
print mail.unread()
```

### To get latest Unread Message in Junk:

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.junk()
print mail.unread()
```

Use `mail.select(folder)` to switch to folders other than `inbox, `junk`.

### Retrive email element:

```py
print mail.mail_body()
print mail.mail_subject()
print mail.mail_from()
print mail.mail_to()
```

### To send Message:

```py
mail.login('emailaccount@domain.com','yourpassword')
mail.send_email('recipient@email.com','subject','message body')
```