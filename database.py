import pymysql
import json
import pandas as pd

'''
数据库操作
'''
DB_HOST = "localhost"
DB_USERNAME = "lhs"
DB_PASSWORD = "abc123456"
DB_DATABASE = "lhs"


def get_data():
    '''
    从数据库中读取数据并返回
    params:None
    return:data(json)
    '''
    db = pymysql.connect(host=DB_HOST,user=DB_USERNAME,password=DB_PASSWORD,database=DB_DATABASE,charset='utf8')
    cursor = db.cursor()
    select_sql = """
                SELECT
                    *
                FROM
                    image
                WHERE
                    image.img_code IS NOT NULL
                ORDER BY
                    image.time DESC
    """
    cursor.execute(select_sql)
    data = cursor.fetchall()
    db.close()
    #List转换DataFrame
    data = pd.DataFrame(data,columns=['img_code','img_url','label_img_url','loc_lat','loc_lng','time','building','green','sky','score','advice'])
    
    return data.to_json(orient='records')

def write_data(data):
    '''
    数据写入
    params:data(list)
    return:(bool)
    '''
    db = pymysql.connect(host=DB_HOST,user=DB_USERNAME,password=DB_PASSWORD,database=DB_DATABASE,charset='utf8')
    cursor = db.cursor()
    if len(data)<11:
        print('数据输入错误')
        return False
    write_sql = """
                INSERT INTO 
                `image` 
                (`img_code`, `img_url`, `label_img_url`,`loc_lat`, `loc_lng`, `time`, `building`, `green`, `sky`, `score`, `advice`) 
                VALUES 
                ('{0[0]}', '{0[1]}', '{0[2]}', '{0[3]}', '{0[4]}', '{0[5]}', '{0[6]}', '{0[7]}', '{0[8]}', '{0[9]}','{0[10]}')
    """.format(data)
    cursor.execute(write_sql)
    db.commit()
    db.close()
    return True

def del_data(img_code):
    '''
    数据删除
    params:img_code
    return:(bool)
    '''
    pass