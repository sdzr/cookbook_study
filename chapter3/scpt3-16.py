# 处理涉及到时区的日期问题
from datetime import datetime
from pytz import timezone
import pytz
d = datetime.now()
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)