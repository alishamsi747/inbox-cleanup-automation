import imaplib
import email
from email.header import decode_header

# replace "email" and "password" values
username = "email"
password = "password"

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)

imap.select("INBOX")
imap.list()

status, messages = imap.search(None, 'BEFORE "01-JAN-2023"')

messages = messages [0].split(b' ')

count = 0

for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")
    imap.store(mail, "+FLAGS", "\\Deleted")
    count += 1
    print(count)


input(f"confirm deletion of {count} emails")
imap.expunge()
print(f"{count} emails deleted")
imap.close()
imap.logout()
