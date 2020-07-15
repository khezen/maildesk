# maildesk

Python Library to read email from any email service, just dowload to yout python script folder. 
This library using Imaplib python to read email with IMAP protocol.

## Usage
 
## Examples

### To get latest Unread Message in inbox:

```py
import emaildesk
mail = emaildesk.Client()
mail.login('emailaccount@domain.com','yourpassword')
mail.inbox()
print mail.unread()
```

### To get latest Unread Message in Junk:

```py
import emaildesk
mail = emaildesk.Client()
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
import emaildesk
mail = emaildesk.Client()
mail.login('emailaccount@domain.com','yourpassword')
mail.send_email('recipient@email.com','subject','message body')
```

### To check Credentials:

```py
import emaildesk
mail = emaildesk.Client()
mail.checkLogin()
```