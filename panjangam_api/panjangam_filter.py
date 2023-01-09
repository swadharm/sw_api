from db import *
from sun_rise_db import *
from location import *
from nazhigai_calc import *
from time_convert import *
import math
import pandas as pd

def name_change(db_name):
    mycursor.execute('select * from name_input where db=?',[db_name])
    data = mycursor.fetchall()
    ans = []
    for i in data:
        ans.append(i)
    return ans

#a = name_change('कन्यामासः')
#print(a[0][4])

def city_timezone(city):
    mycursor.execute('select * from city where name=?',[city])
    c = mycursor.fetchall()
    time_zone = c[0][4]
    return time_zone

def panjangam_db_multi(table,city):
    time_zone = city_timezone(city)
    ans = []
    data = select_sql('*',table)
    for i in data:
        name = i[4]
        start = india_time_zone_converter(i[17],time_zone)
        end = india_time_zone_converter(i[18],time_zone)
        s_timestamp = datetime_timestamp(str(start))
        e_timestamp = datetime_timestamp(str(end))
        data = [name,str(start),str(end),s_timestamp,e_timestamp]
        ans.append(data)
    return ans


#a = panjangam_db_multi('thithi','detroit')
#print(a)

def pnjangam_db_live(city,table):
    time_zone = city_timezone(city)
    t = current_datetime_multi(time_zone)
    t_stamp = datetime_timestamp(str(t))
    data = panjangam_db_multi(table,city)
    for i in data:
        if i[3] < t_stamp and i[4] > t_stamp:
            ans = i
    return ans



#print(pnjangam_db_live('trichy','karanam'))

def pnjangam_db_find_time(city,table,datetime:str):
    time_zone = city_timezone(city)
    t = india_time_zone_converter(datetime,time_zone)
    t_stamp = datetime_timestamp(str(t))
    data = panjangam_db_multi(table,city)
    for i in data:
        if i[3] < t_stamp and i[4] > t_stamp:
            ans = i
    return ans

#print(pnjangam_db_find_time('trichy','thithi','2022-12-10 6:10:12'))