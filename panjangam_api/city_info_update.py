from db import *
#from location import *
import pytz

def city_create(table):
        mycursor.execute(
        """
        CREATE TABLE {}
        (id INTEGER auto_increment primary key,
        name text,
        latitude text,
        longitude text,
        time_zone
        )""".format(table))

#city_create('city')


def upadte_lat_long(name,lat,lon,time_zone):
        mycursor.execute("""INSERT INTO city 
        (name,latitude,longitude,time_zone) VALUES (?,?,?,?)""",[name,lat,lon,time_zone])
        conn.commit()
        print(mycursor.rowcount, "record inserted.")


def city_update(name,lat,lon,time_zone):
    ans = ''
    data = select_sql('*','city')
    for i in data:
        if i[1] == name:
            ans = 'yes'
    if ans != 'yes':
        upadte_lat_long(name,lat,lon,time_zone)
        print('ok')

#city_update('varagur',10.7905,78.7047,'Asia/Kolkata')


def timezone_table(table):
        mycursor.execute(
        """
        CREATE TABLE {}
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        time_zone text
        )""".format(table))

#timezone_table('time_zone')

def upadte_timezone():
        a = pytz.all_timezones
        for i in a:
                mycursor.execute("""INSERT INTO time_zone 
                (time_zone) VALUES (?)""",[i])
                conn.commit()
                print(mycursor.rowcount, "record inserted.")

#upadte_timezone()


"""def update_latlon():
        data = select_sql('*','city')
        for i in data:
                c_data = name_loction(i[1])
                c_lat = c_data['lat']
                c_lon = c_data['lon']
                mycursor.execute('update city set latitude=?, longitude=? where name=? and id > 600',[c_lat,c_lon,i[1]])
                conn.commit()
                print(mycursor.rowcount, "record inserted.")


update_latlon()"""

def update_india_city():
        data = select_sql("*","in_city_input")
        for i in data:
                upadte_lat_long(i[0],i[1],i[2],"Asia/Kolkata")

#update_india_city()