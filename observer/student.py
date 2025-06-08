class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update(self, event):
        print(f"🔔 Email sent to {self.name} ({self.email}) - Reminder: Your event '{event.name}' is coming up on {event.date}!")

# Note
# Class to "update" the student about the event