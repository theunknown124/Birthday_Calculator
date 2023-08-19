import datetime

# Birthday to check
birthday = datetime.date(1990, 3, 28)

# Get today's date
today = datetime.date.today()

# Calculate yesterday's date
yesterday = today - datetime.timedelta(days=1)

# Calculate yesterday's date in the year of the birthday
birthday_yesterday = datetime.date(yesterday.year, birthday.month, birthday.day)

# Check if the birthday was yesterday
if birthday_yesterday == yesterday:
    print("Yes, the birthday was yesterday!")
else:
    print("No, the birthday was not yesterday.")
