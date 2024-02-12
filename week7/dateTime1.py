from datetime import *
today = datetime.now()
print(today)

year=today.year
month=today.month
day=today.day
print(f"{year}-{month}-{day}")
print(f"{year}/{month}/{day}")
print(f"{year}:{month}:{day}")
