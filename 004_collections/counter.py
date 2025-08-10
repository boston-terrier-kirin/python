from collections import Counter

device_temps = [13.5, 14.0, 14.5, 14.5, 13.5, 16.0]

temp_counter = Counter(device_temps)

# Counter({13.5: 2, 14.5: 2, 14.0: 1, 16.0: 1})
print(temp_counter)
