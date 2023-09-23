
import time
from astropy.time import Time


def years_from_epoch(d):
  # Convert the date object to a time object
  t = d.timetuple()

  # Calculate the number of seconds between the time and the Unix epoch
  seconds_from_epoch = time.mktime(t)

  # Convert the number of seconds to years by dividing by the number of seconds in a year
  seconds_in_year = 365.24 * 24 * 60 * 60
  years_from_epoch = seconds_from_epoch / seconds_in_year

  return years_from_epoch


# accept time object and convert to years from Unix epoch



import datetime

# Create a date object for January 1, 2000
d = datetime.date(1902, 1, 1)

# Calculate the number of years from the date to the Unix epoch
years = years_from_epoch(d)
print(f"Years from epoch: {years}")


def to_light_years(years):
    # Convert the number of years to light years by multiplying by the speed of light
    light_years = years * 299792458  # speed of light in meters per second

    return light_years

# Convert 1 year to light years
# years = 1
light_years = to_light_years(years)

print(f"{years} years = {light_years} meters")


