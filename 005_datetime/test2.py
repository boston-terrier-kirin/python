# datetimeにもdatetimeがある
from datetime import datetime as dt
login_dt = dt(2023, 10, 29, 12, 18, 30)
logout_dt = dt(2023, 10, 29, 19, 43, 12)

result = logout_dt - login_dt

# datetime
print(type(logout_dt))

# timedelta
print(type(result))

print(result)
print(result.days)
print(result.total_seconds())
