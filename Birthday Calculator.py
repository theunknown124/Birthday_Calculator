from datetime import date, datetime, timedelta

def get_name():
    name = input("Enter name: ")
    return name


def get_birthday():
    birth_date_str = input("Enter birthday (MM/DD/YY): ")
    birth_date = datetime.strptime(birth_date_str, "%m/%d/%y")

    # if necessary add 100 to fix birth year
    if birth_date.year > datetime.now().year:
        fixed_birth_year = birth_date.year - 100
        birth_date = birth_date.replace(year=fixed_birth_year)
    elif birth_date.year < 1900:
        fixed_birth_year = birth_date.year + 100
        birth_date = birth_date.replace(year=fixed_birth_year)

    # calculate age after adjusting the birth year
    age = datetime.now().year - birth_date.year
    if birth_date.month > datetime.now().month or (
            birth_date.month == datetime.now().month and birth_date.day > datetime.now().day):
        age -= 1

    return birth_date.date(), age


def main():
    today = date.today()
    yesterday = today - timedelta(days=1)

    formatted_today = today.strftime("%A, %B %d, %Y")
    print("Birthday Calculator\n")
    while True:
        userName = get_name()
        userbirthDay, age = get_birthday()
        #print(userbirthDay)
        #print(today)
        #print(yesterday)
        birthday_yesterday = date(yesterday.year,userbirthDay.month, userbirthDay.day)

        birthDayInletterForm = userbirthDay.strftime("%A, %B %d, %Y")
        print("Birthday: ", birthDayInletterForm)
        print("Today: ", formatted_today)

        print(userName + " is " + str(age) + " years old")

        # calculate number of days until next birthday
        next_birthday_year = today.year
        if userbirthDay.month < today.month or (userbirthDay.month == today.month and userbirthDay.day < today.day):
            next_birthday_year += 1

        next_birthday = date(next_birthday_year, userbirthDay.month, userbirthDay.day)
        days_until_next_birthday = (next_birthday - today).days

        if days_until_next_birthday == 0:
            print(userName + "'s birthday is today!")
        elif days_until_next_birthday == 1:
            print(userName + "'s birthday is tomorrow!")
        elif birthday_yesterday == yesterday:
            print(userName + "'s birthday was yesterday!")
        else:
            print(userName + "'s birthday is in " + str(days_until_next_birthday) + " days.")

        #CHECK WHETHER THE USER WANTS TO CONTINUE
        result = input("\ncontinue? (y/n): ")
        print()
        if result.lower() != "y":
            print("bye")
            break


if __name__ == "__main__":
    main()
