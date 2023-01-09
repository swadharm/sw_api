# -------------database_conn python--------------------------
import sqlite3
global conn,cursor
conn=sqlite3.connect('panjangam.db')#check_same_thread=False
mycursor=conn.cursor()
# ------------------------------------------------------
import pandas as pd

# select 
def select_sql(column,table):
    mycursor.execute('select {} from {}'.format(column,table))
    data = mycursor.fetchall()
    return data

# day number
def day_no(date):
    mycursor.execute('select * from day_info_kalam_input where date = ?',[date])
    data = mycursor.fetchall()
    for i in data:
        return i[0]

# day number
def day_no_date(d_n):
    mycursor.execute('select * from day_info_kalam_input where day_no = ?',[d_n])
    data = mycursor.fetchall()
    for i in data:
        return i[2]

# print(day_no('2022-04-24'))

# print(select_sql('*','ayanam'))

# live data 




def city_name(cityname):
    mycursor.execute('select * from city_input where city_name=?'.format(cityname))
    data = mycursor.fetchall()
    ans = []
    for i  in data:
        ans.append(i)
    return ans

def city_code(citycode):
    mycursor.execute('select * from city_input where city_code=?',[citycode])
    data = mycursor.fetchall()
    ans = []
    for i  in data:
        ans.append(i)
    return ans

# data base to csv
"""a = pd.read_sql_query('select * from thithi',conn)
df = pd.DataFrame(a)
df.to_csv(r'/home/swadharmaa/Documents/GitHub/sankalpam_live/sankalpam_live_app/test.csv')"""