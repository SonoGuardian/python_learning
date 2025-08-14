# 2. Конвертация температуры
# Попроси ввести температуру в градусах Цельсия и переведи её в Фаренгейты по формуле:
# F = C * 9/5 + 32

def convert(celsius):
    try:
        int(celsius)
        far = int(celsius) * 9/5 + 32
        print (f"It will be {far} degrees by Fahrenheit")
    except ValueError:
        print("Not correct data. Please try again")


cel = input("Enter celcius to convert: ")
convert(cel)