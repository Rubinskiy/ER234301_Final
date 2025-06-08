from student import Student
from proxy import EventProxy

# Create students
s1 = Student("Bob", is_verified=True)
s2 = Student("Risya", is_verified=False)
s3 = Student("Zhafir", is_verified=False)
s4 = Student("Jawi", is_verified=True)

# Proxy controls access
event_proxy = EventProxy()

event_proxy.create_event(s1, "Software Design Final Project Presentation")
event_proxy.create_event(s2, "Celebrations after final project presentation")
event_proxy.create_event(s3, "Semester holidays")
event_proxy.create_event(s4, "Back to campus for new semester")

# Note
# Create the student objects
# Create the proxy object
# Try to create an event