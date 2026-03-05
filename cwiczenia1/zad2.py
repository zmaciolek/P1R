import numpy as np
masa = float(input("Podaj masę ciała (w kilogramach): "))
wzrost = float(input("Podaj wzrost (w metrach): "))
BMI = masa/wzrost**2
txt = ""
if BMI < 18.5:
    txt = "Niedowaga."
elif BMI < 25:
    txt = "Waga prawidłowa."
elif BMI < 30:
    txt = "Nadwaga."
elif BMI >= 30:
    txt = "Otylosc."
print(f"BMI = {BMI}")
print(txt)
