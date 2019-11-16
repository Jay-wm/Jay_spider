import pymongo
import datetime
import random
import time


connection = pymongo.MongoClient()
db = connection.chapter_6_3
handler_update_insert = db.Date_update_insert_3
handler_bat = db.Data_bat

start_update_insert = time.time()
insert_list = []
for row in handler_bat.find():
	old_date = row['time']
	old_time_datetime = datetime.datetime.strptime(old_date, '%Y-%m-%d')
	one_day = datetime.timedelta(days = 1)
	new_date = old_time_datetime + one_day
	row['time'] = str(new_date.date())
	insert_list.append(row)

handler_update_insert.insert(insert_list)
end_update_insert = time.time()

print(f'insert:{end_update_insert - start_update_insert}')