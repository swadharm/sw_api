from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import *
import pytz
from dateutil.parser import parse



# str to time

def str_time(str):
    time_str = str
    time_object = datetime.strptime(time_str, '%H:%M:%S').time()
    return time_object

# str to datetime

def str_datetime(str):
    format="%Y-%m-%d %H:%M:%S"
    datetime_object = datetime.strptime(str,format)
    return datetime_object

# time to timedelta

def time_timedelta(time):
    t=time
    timedelta_object = timedelta(hours=t.hour,minutes=t.minute,seconds=t.second)
    return timedelta_object



# date_datetime

def date_datetime(date:str):
    txt = date
    x = txt.split("-")
    y =int(x[0])
    m =int(x[1])
    d =int(x[2])
    ans = datetime(y,m,d)
    return(ans)




# time to am pm

def time_am_pm(time:str):
    date = datetime.strptime(time,"%H:%M:%S")
    t = date.strftime("%I:%M:%S %p")
    return t

def daytime_am_pm(time:str):
    date = datetime.strptime(time,"%Y-%m-%d %H:%M:%S")
    t = date.strftime("%Y-%m-%d %I:%M:%S %p")
    return t

def current_date_india():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    date = now.date()
    return str(date)

def current_time_india():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    t = now.time().strftime("%H:%M:%S")
    time = time_am_pm(t)
    return time

def current_datetime_india():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    d = now.date()
    t = now.time()
    ans = now.strftime("%Y-%m-%d %H:%M:%S")
    return ans

def datetime_timestamp(datetime:str):
    d = str_datetime(datetime)
    timestamp = int(round(d.timestamp()))
    return timestamp


def date_time_split(datetime:str):
    dt = parse(datetime)
    y = dt.year
    mo = dt.month
    d = dt.day
    h = dt.hour
    m = dt.minute
    s = dt.second
    _d = str(y)+'-'+str(mo)+'-'+str(d)
    _t = str(h)+':'+str(m)+':'+str(s)
    ans = [y,mo,d,h,m,s,_d,_t]
    return ans


def india_time_zone_converter(ind_datetime:str,time_zone:str):
    tz_ind = pytz.timezone('Asia/Kolkata') # india time zone
    x = str_datetime(ind_datetime) # str to datetime
    dt_ind = tz_ind.localize(x)
    # Set the timezone for the converted date and time
    tz_convert = pytz.timezone(time_zone) 
    # Localize the original date and time to the new timezone
    ans_datetime = dt_ind.astimezone(tz_convert)
    ans = ans_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return ans

#a = india_time_zone_converter('2022-12-30 17:0:0','US/Michigan')
#print(a)

def current_datetime_multi(timezone):
    now = datetime.now(pytz.timezone(timezone))
    d = now.date()
    t = now.time()
    ans = now.strftime("%Y-%m-%d %H:%M:%S")
    return ans