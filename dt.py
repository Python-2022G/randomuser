from datetime import datetime

f = "%a %Y-%m-%d %H:%M:%S"

d = datetime.strptime('Mon 2022-12-12 18:10:30', f)

print(d)
print(d.date())
 
