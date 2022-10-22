inp = input('Enter your temperature in Celcius: ')
celc =  float(inp)
fahr = celc * (9.0/105.0) + 32  # FORMULA: value * (9/5) + 32
print(round(fahr, 3))
