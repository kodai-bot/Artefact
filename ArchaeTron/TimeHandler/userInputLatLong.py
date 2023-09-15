
while True:
  # Get latitude and longitude input from the user
  latitude = input("Enter the latitude: ")
  longitude = input("Enter the longitude: ")

  # Validate the input to ensure that it is a valid latitude and longitude
  try:
    latitude = float(latitude)
    longitude = float(longitude)
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
      break
    else:
      print("Invalid latitude or longitude. Please enter a valid value.")
  except ValueError:
    print("Invalid input. Please enter a valid latitude and longitude.")

# Now that we have valid latitude and longitude values, we can do something with them
# print(f"Latitude: {latitude}")
# print(f"Longitude: {longitude}")
