"""
This was a step by step workshop(51 steps) on building an email simulator
This project used many concepts that I have learned up until this point in the
freecodecamp python cert. prep curriculum.(classes, functions,conditionals,loops)
this was my first project using the datetime module in python(seen something similar in c++)

"""



import datetime

class Email:
    #initializing all my attributes for this class
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        #datetime module was  imported to display date/time
        self.timestamp = datetime.datetime.now()
        self.read = False
    # returns a bool value True to mark email as read
    def mark_as_read(self) -> bool:
        self.read = True

    # I used fstrings to display full email in required format
    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')
    # this str method will check if the email is read then display email info 
    # in required format with f string
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class Inbox:
    #inbox initializes as a list of emails
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)
     
    # list_emails will first check if the email list is empty if not 
    # it will loop through the list of emails displaying them starting at 1
    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    #read_email checks if inbox is empty and checks if a valid index is provided
    #if all that is good it will display the email at the given index
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    #same logic as read email but just deletes at the given index instead
    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
        
class User:
    #user is constructed with a name and inbox made on instantiation
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()
    #method that sends email from self to the receiver with subject and body
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')
    
    # displays users name (name's Inbox) and lists all emails
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)
# test calls and i am also using the main() convention to seperate my definitions
# and executions
def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()

if __name__ == "__main__":
    main()
