from db import *
from sun_rise_db import *
from location import *
from nazhigai_calc import *
from time_convert import *
import math
import pandas as pd


def vasaram_india(city):
    ans = []
    vasaram = select_sql('*','vasaram_input')
    for i in vasaram:
        d = day_no_date(i[2])
        name = i[3]
        start = day_start(city,d)
        end = day_end(city,d)
        s_timestamp = datetime_timestamp(str(start))
        e_timestamp = datetime_timestamp(str(end))
        data = [name,str(start),str(end),s_timestamp,e_timestamp]
        ans.append(data)
    return ans

        
"""a = vasaram_india('trichy')
t = current_datetime_india()
t_stamp = datetime_timestamp(str(t))
for i in a:
    if i[3] < t_stamp and i[4] > t_stamp:
        print (i)"""


def vasaram_multi(city):
    mycursor.execute('select * from city where name=?',[city])
    c = mycursor.fetchall()
    time_zone = c[0][4]
    ans = []
    a = vasaram_india(city)
    for i in a:
        name = i[0]
        start = india_time_zone_converter(i[1],time_zone)
        end = india_time_zone_converter(i[2],time_zone)
        s_timestamp = datetime_timestamp(str(start))
        e_timestamp = datetime_timestamp(str(end))
        data = [name,str(start),str(end),s_timestamp,e_timestamp,time_zone]
        ans.append(data)
    return ans


    



"""a = vasaram_multi('trichy')
for i in a:
    print(i)"""

def vasaram_live(city):
    a = vasaram_multi(city)  
    for i in a:
        t = current_datetime_multi(i[5])
        t_stamp  = datetime_timestamp(t)
        if i[3] < t_stamp and i[4] > t_stamp:
            ans = i
            return ans

#vasaram_live('detroit')