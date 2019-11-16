import pymongo
import datetime
import random
import time


connection = pymongo.MongoClient()
db = connection.chapter_6_3
handler_bat = db.Date_bat

start_1_by_1 = time.time()
for row in handler_bat.find():
	old_date = row['time']
	old_time_datatime = datetime.datetime.stroptime(old_date, '%Y-%m-%d')
	one_day = datetime.timedelta(days = 1)
	new_date = old_time_datatime + one_day
	hanler_bat.update({'_id': row['_id']}, {'$set': {'time': str(new_date.date())}}, upsert = False)
end_1_by_1 = time.time()

print(f'one by one:{end_1_by_1 - start_1_by_1}')