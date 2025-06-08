class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subscribers = []

    def add_subscriber(self, student):
        self.subscribers.append(student)

    def remove_subscriber(self, student):
        self.subscribers.remove(student)

    def notify_subscribers(self):
        for student in self.subscribers:
            student.update(self)

# Note
# Class to create the event object
# with some other functions to add and remove subscribers
# and notify the subscribers