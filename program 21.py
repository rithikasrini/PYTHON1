def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def create_temperature_table():
    print("Celsius\t\tFahrenheit")
    for celsius in range(0, 101, 10):
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}\t\t{fahrenheit:.1f}")


create_temperature_table()
