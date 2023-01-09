from db import *
from sun_rise_db import *
from location import *
from nazhigai_calc import *
from time_convert import *
import math
import pandas as pd
from panjangam_filter import *
from vasaram import *
from translate import *

def sankalpam_data(table,city,language):
    data = pnjangam_db_live(city,table)
    n = name_change(data[0])
    name_s = translate_all_db(language,n[0][4])
    #name_p = translate_all(language,n[0][5]) 
    name = translate_all_db(language,data[0])
    start_t = daytime_am_pm(data[1])
    end_t = daytime_am_pm(data[2])
    ans = {
        'name':name,
        'name_s':name_s,
        #'name_p':name_p,
        'start':start_t,
        'end':end_t
    }
    return ans



#print(sankalpam_data('trichy','thithi'))

def sankalpam_vasaram(city,languae):
    data = vasaram_live(city)
    n = name_change(str(data[0]))
    name_s = translate_all_db(languae,n[0][4]) 
    name =  translate_all_db(languae,n[0][3]) 
    start_t = daytime_am_pm(data[1])
    end_t = daytime_am_pm(data[2])
    ans = {
        'name':name,
        'name_s':name_s,
        'start':start_t,
        'end':end_t
    }
    return ans

#print(sankalpam_vasaram('trichy'))



def sankalpam_all(city,languae):
    time_zone = city_timezone(city)
    t = current_datetime_multi(time_zone)
    c_time = daytime_am_pm(t)
    samvathsaram = sankalpam_data('samvathsaram',city,languae)
    ayanam = sankalpam_data('ayanam',city,languae)
    s_ruthu = sankalpam_data('sowra_ruthu',city,languae)
    c_ruthu = sankalpam_data('chandhra_ruthu',city,languae)
    s_month = sankalpam_data('sowra_month',city,languae)
    c_month = sankalpam_data('chandhra_month',city,languae)
    pakhsma = sankalpam_data('paksham',city,languae)
    thithi = sankalpam_data('thithi',city,languae)
    vasaram = sankalpam_vasaram(city,languae)
    nakshathram = sankalpam_data('nakshathram',city,languae)
    yogam = sankalpam_data('yogam',city,languae)
    karanam = sankalpam_data('karanam',city,languae)
    ans = {
        'city':city,
        'time':c_time,
        'samvathsaram':samvathsaram,
        'ayanam': ayanam,
        's_month':s_month,
        'c_month':c_month,
        's_ruthu':s_ruthu,
        'c_ruthu':c_ruthu,
        'paksham':pakhsma,
        'thithi':thithi,
        'vasaram':vasaram,
        'nakshathram':nakshathram,
        'yogam':yogam,
        'karanam':karanam
    }
    return  ans


#a = sankalpam_all('trichy','tamil')
#print(a)

