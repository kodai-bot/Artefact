import math


# convert latitude and longitude to equatorial coordinates

def to_equatorial(latitude, longitude):
  # Convert latitude and longitude to radians
  lat_rad = math.radians(latitude)
  lon_rad = math.radians(longitude)

  # Calculate the declination using the formula:
  # declination = asin(sin(latitude) * cos(eps) + cos(latitude) * sin(eps) * sin(longitude))
  eps = math.radians(23.4393 - 3.563E-7 * (365.25 * 2000 + 100.0))  # obliquity of the ecliptic
  declination = math.asin(math.sin(lat_rad) * math.cos(eps) + math.cos(lat_rad) * math.sin(eps) * math.sin(lon_rad))
  declination = math.degrees(declination)

  # Calculate the right ascension using the formula:
  # right_ascension = atan2(sin(longitude) * cos(eps) - tan(latitude) * sin(eps), cos(longitude))
  right_ascension = math.atan2(math.sin(lon_rad) * math.cos(eps) - math.tan(lat_rad) * math.sin(eps), math.cos(lon_rad))
  right_ascension = math.degrees(right_ascension)

  # Return the declination and right ascension in degrees
  return declination, right_ascension
