# notification for windows idk whats the use
# dev : Captain_Etrigan
from plyer import notification
import time

print("entering 4th dimension...")
print("Welcome to windows Notification timer! (A totally useful program)")
print("-" * 50, "/")


def Timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    # --END of timer--

    def NotifyMe(titlee, message, ticker, timing):
        notification.notify(
            title=titlee,
            message=message,
            app_icon="comics-batman_97405.ico", #you can use any icon you want this is just the one i like, heres the link for the website you can download icons form : https://icon-icons.com/
            timeout=timing,
            ticker=ticker
        )

    if __name__ == '__main__':
        NotifyMe(title, desc, "idk what this is", timeoout)


timee = int(input("How much time do you want the timer to be (in seconds)? "))
title = str(input("Title for the notification : "))
desc = str(input("Description for the notification : "))
timeoout = int(input("Timeout for the notification : "))
Timer(int(timee))
