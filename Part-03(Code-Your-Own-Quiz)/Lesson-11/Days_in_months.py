days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def how_many_days(month_number):
    return days_in_month[month_number-1]
print(how_many_days(12))
print(how_many_days(10))
