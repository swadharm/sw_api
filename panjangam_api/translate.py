from aksharamukha import transliterate
from db import *



#a = transliterate.process('autodetect', 'Tamil', 'विषयः')


def translate_tamil(text):
    ans = transliterate.process('autodetect', 'Tamil', text,False,post_options=['RetainTamilDanda'])
    return ans

def translate_devanadari(text):
    ans = transliterate.process('autodetect', 'Devanagari', text)
    return ans

def translate_telugu(text):
    ans = transliterate.process('autodetect', 'Telugu', text,False,post_options=['RetainTeluguDanda'])
    return ans

def translate_malayalam(text):
    ans = transliterate.process('autodetect', 'Malayalam', text,False,post_options=['RetainMalayalamDanda'])
    return ans

def translate_kannada(text):
    ans = transliterate.process('autodetect', 'Kannada', text,False,post_options=['RetainKannadaDanda'])
    return ans

def translate_grantha(text):
    ans = transliterate.process('autodetect', 'Grantha', text)
    return ans

def translate_english(text):
    ans = transliterate.process('autodetect','Roman(ITRANS)', text)
    return ans

def translate_all(language,text):
    if language == 'tamil':
        ans = translate_tamil(text)
    elif language == 'devanagari':
        ans = translate_devanadari(text)
    elif language == 'grantham':
        ans = translate_grantha(text)
    elif language == 'malayalam':
        ans = translate_malayalam(text)
    elif language == 'kannada':
        ans = translate_kannada(text)
    elif language == 'telugu':
        ans = translate_telugu(text)
    return ans

#a = translate_all('tamil','prasanna')
#print(a)


def translate_create(table):
        mycursor.execute(
        """
        CREATE TABLE {}
        (id INTEGER auto_increment primary key,
        name_db text,
        name_output text,
        category text
        )""".format(table))

#translate_create('panjangam_translate')

def translate_create_data(name_db,name_output,category):
        mycursor.execute("""INSERT INTO panjangam_translate
        (name_db,name_output,category) VALUES (?,?,?)""",[name_db,name_output,category])
        conn.commit()
        print(mycursor.rowcount, "record inserted.")

def updata_translate(language):
    count = 0
    data = select_sql("*",'name_input')
    for i in data:
        db_name = i[4]
        name_output = translate_all(language,db_name)
        translate_create_data(db_name,name_output,language)
        count = count + 1
        print(count)

# tamil
#la = ['tamil','devanagari','grantham','malayalam','kannada','telugu']
#for i in la:
    #updata_translate(i)

def translate_all_db(language,text):
    mycursor.execute('select name_output from panjangam_translate where name_db=? and category=?',[text,language])
    data = mycursor.fetchall()
    for i in data:
        ans = i
    return ans
    
#print(translate_all_db('tamil','दक्षिणायनम्'))