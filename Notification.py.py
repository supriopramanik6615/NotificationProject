# "Take a Break" Notification system in Python


from plyer import notification  #pip install plyer
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Suprio pramanik\\Downloads\\Ampeross-Qetto-2-Timer.ico", #http://www.iconarchive.com/show/qetto-2-icons-by-ampeross/timer-icon.html
        timeout = 10,
    )


if __name__ == '__main__':
    while True:
        notifyMe("Hey User, take a break now !!", "You should follow the 20-20-20 rule to keep your eyes healthy")
        time.sleep(1200)