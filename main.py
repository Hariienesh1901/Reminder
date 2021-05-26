from plyer import notification
import time

reminderTitle = input('What\'s the title of your reminder: ')
reminderBody = input('What\'s your reminder\'s content: ')

while True:
    notification.notify(
        title=reminderTitle,
        message=reminderBody,
        app_icon="Bell.ico",
        timeout=500
    )

    time.sleep(60*60*0.2)
