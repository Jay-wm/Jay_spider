'''new file, section 7.1'''
import json


person = \
    {
      'basic_info': {
          'name': 'kingname',
          'age': 24,
          'sex': '男',
          'merry': False
      },
      'work_info':{
          'salary': 99999,
          'position': 'engineer',
          'department': None
      }
    }

person_json = json.dumps(person, indent = 4)
print(person_json)