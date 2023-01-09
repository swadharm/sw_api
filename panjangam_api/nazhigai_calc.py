from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import *
import pytz
from dateutil.parser import parse

# nazigai to vinadi

def nazhigai_timedelta(n,v):
    total_vinadi = n*60+v
    time = timedelta(seconds=int(total_vinadi)*24)
    time_round = timedelta(seconds=time.seconds)
    return time_round

# x = nazhigai_timedelta(4,59)
# print(x)

def nazhigai_time(n,v):
    total_vinadi = n*60+v
    time = timedelta(seconds=total_vinadi*24)
    time_round = timedelta(seconds=time.seconds)
    return time_round

# print(nazhigai_time(1,30))

def vinadi_to_nazhigai(v):
    calc = v/60
    nazhigai = int(calc)
    vinadi = v - nazhigai*60 
    return str(nazhigai)+"-"+str(vinadi)

# print(vinadi_to_nazhigai(138))

def nazhigai_to_vinadi(n,v):
    vinadi = n*60
    return vinadi + v

# print(nazhigai_to_vinadi(2,30))

def time_to_nazhigai(hour,minute,second):
    h_dh = hour*9000
    m_dh = minute*150
    s_dh = second*2.5
    total_dh = h_dh+m_dh+s_dh
    nazhigai = int(total_dh/3600)
    vinadi = int((total_dh - nazhigai*3600)/60)
    dharparai = int(total_dh - (nazhigai*3600+vinadi*60))
    ans = [nazhigai,vinadi,dharparai]
    return ans

#a = time_to_nazhigai(1,0,24)
#print(a[0])