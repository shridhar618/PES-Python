import sys
# temporarily remove current-directory entry from sys.path to avoid importing a local random.py that shadows the stdlib module
cwd_marker = ''
if cwd_marker in sys.path:
    sys.path.remove(cwd_marker)
import importlib
r = importlib.import_module('random')
# restore current-directory entry
sys.path.insert(0, cwd_marker)

# seed()
r.seed(10)
print(f"random integer value in a given range is: {r.randint(10,10000)}")

c=['apple','banana','cherry','fig']
print(f"random choice from the list is: {r.choice(c)}")

print(f"Random choices of 3 from the list is: {r.choices(c, k=3)}")

print(f"random sample from the list is: {r.sample(c, k=2)}")


from datetime import datetime, date, time, timedelta 

print(f"the currect date and time {datetime.now()}")

print(f"future date after 7 days is {datetime.now()+timedelta(days=7)}")

print(f"future date after 5 days and 10 hours is{datetime.now()+timedelta(days=5, hours=10)}")

c_d=date.today()
c_t=time(hour=10, minute=45, second=7)
print(f"combined date time is {datetime.combine(c_d, c_t)}")

# print(f"the current week numbver is {datetime.now()}")


