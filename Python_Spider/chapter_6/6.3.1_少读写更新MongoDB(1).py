import pymongo
import datetime
import random
import time

connection = pymongo.MongoClient()
db = connection.chapter_6_3
handler_1_by_1 = db.Data_1_by_1
handler_bat = db.Data_bat

today = datetime.date.today()

# one by one
start_1_by_1 = time.time()
for i in range(10000):
    delta = datetime.timedelta(days=i)
    fact_date = today - delta
    handler_1_by_1.insert_one({'time': str(fact_date),'data': random.randint(0,10000)})
end_1_by_1 = time.time()

# mul
start_bat = time.time()
insert_list = []
for i in range(10000):
    delta= datetime.timedelta(days = i)
    fact_date = today - delta
    insert_list.append({'time': str(fact_date), 'data': random.randint(0, 10000)})
handler_bat.insert(insert_list)
end_time = time.time()

print(f'the time one by one spend: {end_1_by_1 - start_1_by_1}')
print(f'the time mul spend: {end_time- start_bat}')    
