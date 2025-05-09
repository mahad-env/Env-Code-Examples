def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Example run
data = [72, 55, 101, 90]
average = calculate_average(data)
print("Average:", average)
stations = [
    ['A1', 62],
    ['B2', 97],
    ['C3', 80]
]

# Printing each station on its own line
for station in stations:
    print(f"{station[0]} → {station[1]}")
def report_status(stations, pm25_threshold):
    for station in stations:
        name = station[0]
        pm25 = station[1]
        if pm25 > pm25_threshold:
            status = "High pollution"
        else:
            status = "Normal"
        print(f"{name}: {pm25} → {status}")

# Run the function
report_status(stations, 100)
