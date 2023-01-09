from db import *
from location import *
from nazhigai_calc import *
from time_convert import *
import math
import pandas as pd


# rekamsham = Longitude
# palachayai = latitude


# Longitude to longitude_dms (100 amsham to 60 amsham)
def rk_conveter(Longitude):
    a = math.modf(Longitude)
    lon_calc = (a[0]*.6)+a[1]
    longitude_dms = '%.2f' % lon_calc
    return longitude_dms

#print(rk_conveter(10.7870))


# rekandhra vinadi (input Longitude)
def rk_diff(i_rk,s_rk):
    a = i_rk - s_rk
    diff_100 = rk_conveter(a)
    p_k = math.modf(float(diff_100))
    pagai = p_k[1]*600
    kalai = p_k[0]*1000
    dharparai = pagai + kalai
    rk_vinadi = dharparai/60
    return rk_vinadi

#a = rk_diff(80.2707,79.25)
#print(a)

def pl_calc(latitude):
    a = math.tan(math.radians(latitude))
    palachayai = a*12
    return palachayai

#a = pl_calc(10.7870)
#print(a)



#----------------------------------------------------------
"""swadhesa_palachayai = sp
ishtadesa_palachayai = ip
ishtadesa_rekamsham (rekandhra vinadi)= ir
ahas_nazhigai = an
ahas_vinadi = av
swadhesa_surya_udhayam = ss_h,ss_m,ss_s"""
#-----------------------------------------------------------
class d_samskaram:
    def __init__(ds,sp,ip,ir,an,av,ss_h,ss_m,ss_s):
        ds.sp=float(sp)
        ds.ip=float(ip)
        ds.ir=float(ir)
        ds.an=an
        ds.av=av
        ds.ss_h=int(ss_h)
        ds.ss_m=int(ss_m)
        ds.ss_s=int(ss_s)
    def ds_calc(ds):
        ds.atv=ds.an*60+ds.av-1800                       #(அஹஸ் வித்யாசம்)
        ds.ss_ts=ds.ss_h*3600+ds.ss_m*60+ds.ss_s         #(ஸூர்ய உதயம் நொடியில்)
        ds.ss_v=ds.ss_ts/24                              #(ஸூர்ய உதயம் நொடி to வினாடி)
        ds.iav=ds.atv*ds.ip/ds.sp                        #(இஷ்ட தேச அஹஸ் வித்யாசம்)
        ds.s2=ds.iav-ds.atv
        ds.s3=ds.s2/2
        ds.s4=ds.s3+ds.ir
        ds.s5=-ds.s4
        ds.iss_v=ds.s5+ds.ss_v                           #(இஷ்ட தேச ஸூர்ய உத்யம் வினாடியில்)
        ds.iahs=ds.iav+1800                              #(இஷ்ட தேச அஹஸ் வினாடியில்)
    def i_sunrise(ds):
        return ds.iss_v
    def i_ahas(ds):
        return ds.iahs
#-----------------------------------------------------------

def sun_ahas(date,city_name):
    c = name_loction(city_name)
    s_pl = 2.29 # swadhesa palachayai
    s_rk = 79.25 # swadhesa rekamsham 
    i_rk = rk_diff(c['lon'],s_rk) # ishta dhesha rekandhra vinadi
    i_pl = pl_calc(c['lat']) # ishta dhesha palachayai
    mycursor.execute('select * from day_info_kalam_input where date=?',[date])
    data = mycursor.fetchall()
    for i in data:
        sun_rise = str_time(i[3])
        h = sun_rise.hour
        m = sun_rise.minute
        s = sun_rise.second
        d_s = d_samskaram(s_pl,i_pl,i_rk,i[4],i[5],h,m,s)
        d_s.ds_calc()
        a = nazhigai_timedelta(0,d_s.i_sunrise())
        b = nazhigai_time(0,d_s.i_ahas())
        ans = {
            'sun':a,
            'ahas':b
        }
        return ans

    


#print(sun_ahas('2022-05-10','Melbourne'))

class sun_rise:
    def __init__(self,date,city):
        self.date = date
        self.city = city
        self.s = sun_ahas(self.date,self.city)
        self.sun_24 = self.s['sun']
        self.sun_am = time_am_pm(str(self.sun_24))
        d = date_datetime(date)
        self.s_datetime = d + self.sun_24


#x = sun_rise('2022-10-12','trichy') 
#print(x.sun_am)

class ahas:
    def __init__(self,date,city):
        self.date = date
        self.city = city
        self.s = sun_ahas(self.date,self.city)
        self.ahas = self.s['ahas']


#x = ahas('2022-10-12','trichy') 
#print(x.ahas)


def day_start(city,date):
    ans = sun_rise(date,city)
    return ans.s_datetime

def day_end(city,date):
    d = pd.to_datetime(date) +  pd.DateOffset(days=1)
    d_t = d.date()
    ans = sun_rise(str(d_t),city)
    return ans.s_datetime

#print(day_start('trichy','2022-12-15'))
#print(day_end('trichy','2022-12-15'))


#a = ahas('2022-12-30','Detroit')
#print(a.ahas)


"""a= sun_rise('2022-12-30','Detroit')
for i in range(1,10):
    a= sun_rise('2022-12-30','Detroit')
    print(a.s_datetime)

print(india_time_zone_converter('2022-12-30 18:43:36','US/Michigan'))"""
