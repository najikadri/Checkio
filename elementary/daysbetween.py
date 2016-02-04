import datetime

def days_diff(date1, date2):
    d1 = datetime.date(date1[0],date1[1],date1[2])
    d2 = datetime.date(date2[0],date2[1],date2[2])
    return abs(d1-d2).days
