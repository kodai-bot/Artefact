import math

def to_cartesian(right_ascension, declination, distance):
    # Convert the right ascension and declination to radians
    right_ascension_rad = math.radians(right_ascension)
    declination_rad = math.radians(declination)

    # Calculate the Cartesian coordinates using the formulas:
    # x = distance * cos(declination) * cos(right_ascension)
    # y = distance * cos(declination) * sin(right_ascension)
    # z = distance * sin(declination)
    x = distance * math.cos(declination_rad) * math.cos(right_ascension_rad)
    y = distance * math.cos(declination_rad) * math.sin(right_ascension_rad)
    z = distance * math.sin(declination_rad)

  return (x, y, z)      




