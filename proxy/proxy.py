from event import EventService

class EventProxy:
    def __init__(self):
        self.real_service = EventService()

    def create_event(self, student, title):
        if student.is_verified:
            self.real_service.create_event(student, title)
        else:
            print(f"❌ Access Denied: {student.name} is not verified to create events.")

# Note
# Class to create the proxy object
# If a student wants to create an event, the proxy will check if the student is verified