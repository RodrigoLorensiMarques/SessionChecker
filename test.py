from datetime import datetime

date_today = datetime.now()

print(date_today)


date_today_ptbr = date_today.strftime("%d/%m/%Y")

print(date_today_ptbr)
