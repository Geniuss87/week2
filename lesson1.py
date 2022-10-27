temperature = float(input('Введите температуру в Цельсиях '))
if temperature < -273.15:
    print('Температура ниже абсолютного нуля')
elif temperature == -273.15:
    print('Температура равна абсолютному нулю')
elif temperature > -273.15 and temperature < 0:
    print('Температура ниже точки замерзания')
elif temperature == 0:
    print('Температура находится в точке замерзания')
elif temperature > 0 and temperature < 100:
    print('Температура находится в нормальном диапазоне')
elif temperature == 100:
    print('Температура находится в точке кипения')
elif temperature > 100:
    print('Температура выше точки кипения')


