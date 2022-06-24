#lets create a fuction to say say days to ur birthdate
import datetime


def monthIandV(month, year, date):
    checkMonth31 = [1, 3, 5, 7, 8, 10, 12]
    loopfactor = True
    while loopfactor:
        if month in checkMonth31:
            if year > 1900:
                if date < 31:
                    loopfactor = False
                else:
                    print("invalid date")
            else:
                print("invalid year")

        elif month<13:
            if year > 1900:
                if date < 30:
                    loopfactor = False
        else:
            print("invalid input retry")
            x = int(input("enter the year you were born:\n"))
            z = int(input("enter the date you were born:\n"))
            y = int(input("what is the index number value of the month u were born?: \n"))
            monthIandV(y, x, z)


def date_validation(day, month, year):
    isValidDate = True

    try:
        datetime.datetime(int(year),
                          int(month), int(day))

    except ValueError:
        isValidDate = False

    if (isValidDate):
        print("Yes")
    else:
        print("No")

# This code is contributed by ajay0007


def input_date():
    x = int(input("enter the year you were born:\n"))
    z = int(input("enter the date you were born:\n"))
    y = int(input("what is the index number value of the month u were born?: \n"))

    date_validation(z, y, x)
    #monthIandV(y, x, z)
    #bday = datetime.date(x, y, z)
    #return bday


def past_date(daysTo):
    if daysTo < 0:
        print("ooops you birthday passed wait for next year,...\n")
    else:
        print("will have to wait for {} days to your birthday,... age gracefully".format(daysTo))
def day_to_birthday():
    tday = datetime.date.today()
    bday = input_date()
    to_birthday =tday - bday
    print(tday)
    print(bday)

#day_to_birthday()
input_date()
