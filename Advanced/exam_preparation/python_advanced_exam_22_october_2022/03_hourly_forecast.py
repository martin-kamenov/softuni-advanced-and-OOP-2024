# 90%
def forecast(*weather_data):
    weather_order = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    for location, weather in weather_data:
        weather_order[weather].append(location)

    result = []

    for curr_weather, curr_locations in weather_order.items():
        sorted_curr_locations = sorted(curr_locations, key=lambda x: x[0])

        for curr_location_ in sorted_curr_locations:
            result.append(f'{curr_location_} - {curr_weather}')

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

