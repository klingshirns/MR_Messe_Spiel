import json

f = open ('quiz.json')
data = json.load (f)
f.close

p = data['Quiz']

name = p['headline']
print(p['headline'])

name = p['name2']
print(p['name2'])

q = data['Questions']

quest1 = q['no']
print(q['no'])


name4 = p['name4']
print(p['name4'])