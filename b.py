import json
import pymssql
import cryptography
import bcrypt
from faker import Faker
import random
import pandas as pd

conn = pymssql.connect(server='localhost', user='SA', password='1q2w3e4r@@', port='12000', database='restaurant_service', charset='utf8')
cursor = conn.cursor()

fake = Faker('ko_KR')
Faker.seed()

for i in range(10000):
    name = fake.name()
    email = fake.free_email()
    phone = '010-' + str(random.randint(1, 9999)).zfill(4) + '-' + str(random.randint(1, 9999)).zfill(4)
    user_id = fake.user_name()
    password = fake.password()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    dic = {'id': user_id, 'pw': hashed_pw, 'name': name, 'email': email, 'phone': phone}
    print(dic)
    
    # USERS_ID 중복 체크
    check_sql = "SELECT COUNT(*) FROM users WHERE USERS_ID = %s"
    cursor.execute(check_sql, (dic['id'],))
    result = cursor.fetchone()[0]

    if result == 0:
        # 중복이 없으면 데이터베이스에 레코드 추가
        insert_sql = "INSERT INTO users (USERS_ID, USERS_PW, USERS_NAME, USERS_EMAIL, USERS_PHONE) VALUES (%s, %s, %s, %s, %s)"
        values = (dic['id'], dic['pw'], dic['name'], dic['email'], dic['phone'])
        cursor.execute(insert_sql, values)
        conn.commit()
    else:
        print(f"중복된 USERS_ID 발견: {dic['id']}")