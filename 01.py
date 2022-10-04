import datetime


from datetime import datetime, timezone

from datetime import datetime, timedelta, timezone
a = datetime.now().isoformat()
b = datetime.utcnow().isoformat()

print(a)
print(b)

a = datetime.now().replace(tzinfo=timezone(timedelta(hours=8))).isoformat()
b = datetime.utcnow().replace(tzinfo=timezone(timedelta(hours=8))).isoformat()

print(a)
print(b)


from datetime import datetime, timezone, timedelta

