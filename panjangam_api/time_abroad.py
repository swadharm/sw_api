from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import *
import pytz
from time_convert import *

# Set the timezone for the original date and time
tz_ind = pytz.timezone('Asia/Kolkata')

# Create a datetime object for the original date and time
dt_ind = tz_ind.localize(datetime(2022, 12, 30, 0, 6, 0))

# Print the original date and time
print(dt_ind)  # Output: 2020-01-01 12:00:00-05:00

# Set the timezone for the converted date and time
tz_LA = pytz.timezone('Australia/Sydney')

# Localize the original date and time to the new timezone
dt_LA = dt_ind.astimezone(tz_LA)

# Print the converted date and time
print(dt_LA)  # Output: 2020-01-01 09:00:00-08:00

a = pytz.all_timezones
for i in a:
    print(i)