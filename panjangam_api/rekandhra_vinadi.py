from time_convert import *
from nazhigai_calc import *
import math

# rekamsham = Longitude
# palachayai = latitude


def rk_conveter(Longitude):
    a = math.modf(Longitude)
    lon_calc = (a[0]*.6)+a[1]
    longitude_dms = '%.2f' % lon_calc
    return longitude_dms


#s = 79.25
#i = 78.7046725


#print(rk_conveter(c))

def rk_diff(i_rk,s_rk):
    a = i_rk - s_rk
    diff_100 = rk_conveter(a)
    p_k = math.modf(float(diff_100))
    pagai = p_k[1]*600
    kalai = p_k[0]*1000
    dharparai = pagai + kalai
    rk_vinadi = dharparai/60
    return rk_vinadi

def pl_calc(latitude):
    a = math.tan(math.radians(latitude))
    palachayai = a*12
    return palachayai






"""s = 79.25
i = 80.28
print(pl_calc(13.0827))"""