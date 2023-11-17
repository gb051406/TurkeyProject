month = int(input("What # month is it? 1-12 "))
day = int(input("What day is it? 1-31 "))
















output = ""
num = 1
while True:
    print(str(month) + "/" + str(day) + " greatfulness entries: ")
    output += (str(month) + "/" + str(day) + ": ")
    for i in range(3):
        x = input(str(num) + ": ")
        output += (x + ", ") 
        num += 1
    num = 1
    show = input("Would you like to show past entries? ")
    if show == "yes":
        print(output)
    day += 1
    if month <= 7 and month%2!=0 and day > 31:
        month += 1
        day = 1
    elif month <= 7 and month%2==0 and day > 30 and month != 2:
        month += 1
        day = 1
    elif month == 2 and day > 28:
        month += 1
        day = 1
    elif month > 7 and month%2 == 0 and day > 31:
        month += 1
        day = 1
    elif month > 7 and month%2 != 0 and day > 30:
        month += 1
        day = 1
    if month > 12:
        month = 1