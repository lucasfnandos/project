import datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar

def custom_calendar():
    current_time = datetime.now()
    date = current_time.date()
    def get_numerator(date):
        if date.day == 1:
            return 'st'
        elif date.day == 2:
            return 'nd'
        elif date.day == 3:
            return 'rd'
        else:
            return 'th'
    weekday = calendar.weekday(date.year, date.month, date.day)
    day_name = calendar.day_name[weekday]
    month_name = calendar.month_name[date.month]
    return f"{day_name} {month_name}, {date.day}{get_numerator(date)} {date.year}"

def current_date():
    current_date = datetime.now()
    date = current_date.date()
    return date

def get_date(year, month, day):
    try:
        datum = datetime(year,month,day)
    except:
        try:
            datum = datetime(year,month,(day-1))
        except:
            try:
                datum = datetime(year,month,(day-2))
            except:
                datum = datetime(year,month,(day-3))
    return datum.date()

def getmonth_name(number):
    month = calendar.month_name[number]
    return month

def get_week_before():
    delta = timedelta(weeks=1)
    week_before = (datetime.now() - delta)
    return week_before.date()

def usd(value):
    if value == None:
        return f"$0.00"
    return f"${value:,.2f}"

def contact(phone):
    return f"({phone[0]}{phone[1]}) "f"{phone[2:6]}-{phone[7:]}"

def comp_id(ident):
    if len(ident) > 11:
        return f"{ident[:2]}.{ident[2:5]}.{ident[5:8]}/{ident[8:12]}-{ident[12:]}"
    else:
        return f"{ident[:3]}.{ident[3:6]}.{ident[6:9]}-{ident[9:]}"
    
def get_age(now, birthdate):
    rdelta = relativedelta(now, birthdate)
    return rdelta.years

def string_format(string):
    stp = string.strip()
    return stp.capitalize()
