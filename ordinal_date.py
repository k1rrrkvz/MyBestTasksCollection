# простейший код нахождения порядковой даты

def ordinalDate(day, month, year):
    ordinal = 0 
    for a in range(1, month):
        ordinal += DniMonth(a, year)
    ordinal += day
    return ordinal

def DniMonth(month, year):
    if month == 2: 
        if year % 400 == 0 or year % 100 == 0 or year % 4 == 0:
            return 29
        else:
            return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31
        
day = int(input("Введите день: ")) 
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

ordinal = ordinalDate(day, month, year)
print("Порядковая дата -", ordinal)