def next_day(year,month,day):
    """# WARNING: this version incorrectly assumes all months have 30 days!""
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
print(next_day(2012,6,29))
print(next_day(2012,1,30))
print(next_day(2012,12,31))
