def to_fahrenheit(in_celsius):
    return (in_celsius * 1.8) + 32

def to_celsius(in_fahrenheit):
    return  (in_fahrenheit -32 ) /1.8


grados_celsius = 40
print(f"Temperatura en celsius: {grados_celsius} -> Fahrenheit = {to_fahrenheit(grados_celsius):.2f}")

grados_fahrenheit = 104
print(f"Temperatura en Fahrenheit: {grados_fahrenheit} -> Celsius = {to_celsius(grados_fahrenheit):.2f}")


# Print Output:
# Temperatura en celsius: 40 -> Fahrenheit = 104.00
# Temperatura en Fahrenheit: 104 -> Celsius = 40.00