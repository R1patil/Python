import datetime 
# Getting today's date 
today = datetime.date.today() 
print(f"Today's date: {today}") 


today = datetime.date.today() 
formatted_date = today.strftime("%Y-%m-%d and the Day is %A") 
print(f"Formatted date: {formatted_date}") 


now = datetime.datetime.now() 
current_time = now.time() 
print(f"Current time: {current_time}") 


now = datetime.datetime.now() 
current_time = now.time() 
print(f"Current time: {current_time}") 
# Output: Current time: 22:33:52.630966 
# 12-hour format 
time_12h_format = now.strftime("%I:%M:%S %p") 
# %I for 12-hour format, %p for AM/PM 
print("Current time (12-hour format):", time_12h_format) 
#Output: Current time (12-hour format): 10:55:44 PM


now = datetime.datetime.now() 
print(f"Current datetime: {now}") 
# Output: Current datetime: 2024-06-01 23:04:33.243942 
now = datetime.datetime.now() 
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S") 
print(f"Formatted datetime: {formatted_datetime}") 


now = datetime.datetime.now() 
print(now) 
#Output: 2024-06-01 23:12:44.091486 
addedTime = datetime.timedelta(days=10, hours=5, minutes=30) 
future_date = now + addedTime 
print(f"Future date and time: {future_date}") 