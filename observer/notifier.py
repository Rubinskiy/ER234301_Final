import time

class Notifier:
    def __init__(self, event):
        self.event = event

    def trigger_reminders(self):
        print("⏳ Sending reminders to subscribers...")
        time.sleep(2)
        self.event.notify_subscribers()

# Note
# Class to send the reminder to the subscribers