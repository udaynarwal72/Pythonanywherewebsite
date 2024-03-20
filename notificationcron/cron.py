import schedule
import time
from index import sendNoti
def job():
    sendNoti()
    
# Schedule the job to run at 8:30 AM and 9:25 AM every day
schedule.every().day.at("08:00").do(job)
schedule.every().day.at("08:55").do(job)
schedule.every().day.at("10:10").do(job)
schedule.every().day.at("11:05").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("13:15").do(job)
schedule.every().day.at("14:10").do(job)
schedule.every().day.at("15:05").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("16:55").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)