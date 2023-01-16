import win10toast
import schedule 
import time 

noti = win10toast.ToastNotifier()

def water():
    noti.show_toast('Time to drink water!', duration= 10)

def take_break():
    noti.show_toast('You have been working since one hour. Time to take a break', duration= 10)

def work():
    noti.show_toast('Restart your work', duration= 10)

def medicine():
    noti.show_toast('Time to take the medicine', duration= 15)

def backup():
    noti.show_toast('Take backup and end work', duration= 15)

schedule.every().hour.do(water)
schedule.every().hour.do(take_break)
schedule.every(10).to(15).minutes.do(work)
schedule.every().day.at("22:00").do(medicine)
schedule.every().day.at("20:00").do(backup)

while True:
  schedule.run_pending()
  time.sleep(1)
