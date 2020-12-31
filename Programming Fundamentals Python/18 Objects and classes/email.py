class Email:
    def __init__(self, sender, receiver, content, is_send=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send

    def send(self):
        self.is_send = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}'


emails = []

while True:
    line = input()
    if line == 'Stop':
        break
    sender, receiver, content = line.split()
    email = Email(sender, receiver, content)
    emails.append(email)


sent_emails = [int(x) for x in (input().split(', '))]

for x in sent_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())