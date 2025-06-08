from student import Student
from event import Event
from notifier import Notifier

# Create students
s1 = Student("Bob", "bob@student.its.ac.id")
s2 = Student("Risya", "risya@student.its.ac.id")
s3 = Student("Zhafir", "zhafir@student.its.ac.id")

# Create event
study_event = Event("Software Design Final Project Presentation", "2025-06-16")

# Students register for the event
study_event.add_subscriber(s1)
study_event.add_subscriber(s2)
study_event.add_subscriber(s3)

# Send reminder
notifier = Notifier(study_event)
notifier.trigger_reminders()

# Note
# Create the student objects
# then create the event object
# add subscribers to that event as if they registered
# then send the reminder to the subscribers after creating the notifier object