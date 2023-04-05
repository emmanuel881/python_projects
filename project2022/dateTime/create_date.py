import datetime
date_brth = datetime.date(2016, 9, 24)
date_today = datetime.date.today()
days_to = date_today - date_brth 
print("i was born on {}".format(date_brth))
print("Date today is {}".format(date_today))
print("This makes {} days to my birthday".format(days_to.days))

