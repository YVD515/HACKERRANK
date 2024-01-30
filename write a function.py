def is_leap(year):
    if year >= 1900 and year <= 10**5:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        elif year % 4 == 0:
            return True
        else:
            return False
    else:
        return "Invalid Input"

year = int(input())
print(is_leap(year))
