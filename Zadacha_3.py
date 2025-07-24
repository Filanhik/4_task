class BaseConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def convert(self, measurement_unit):
        if measurement_unit.lower() == "kelvin":
            return self.celsius + 273.15
        elif measurement_unit.lower() == "fahrenheit":
            return self.celsius * 9/5 + 32
        else:
            raise ValueError("Неверная единица измерения")


if __name__ == "__main__":
    try:
        celsius = float(input("Введите температуру в градусах Цельсия: "))
        target = input("Единица измерения для конвертирования (Kelvin/Fahrenheit): ")

        converter = BaseConverter(celsius)
        result = converter.convert(target)

        '''
        Округляем до двух знаков после запятой
        и делаем первую букву заглавной
        '''
        print(f"Результат: {result:.2f} {target.capitalize()}")

        '''
        Перехват ошибки для неправильного ввода.
        Например: ввод символов вместо числа
        '''
    except ValueError as e:
        print("Ошибка:", e)