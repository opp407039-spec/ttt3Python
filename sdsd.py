import logging

logging.basicConfig(level=logging.ERROR,
                    filename="errors.log",
                    filemode="w",
                    format="%(asctime)s:%(levelname)s - %(message)s")


def divide(a, b):
    return a / b


def main():
    try:
        x = int(input("Введіть перше число: "))
        y = int(input("Введіть друге число: "))
        result = divide(x, y)
        print("Результат:", result)
    except ZeroDivisionError as e:
        logging.error(f"Помилка ділення: {e}")
        print("Ділення на нуль неможливе")
    except ValueError as e:
        logging.error(f"Некоректне введення: {e}")
        print("Потрібно ввести ціле число")
    except Exception as e:
        logging.error(f"Невідома помилка: {e}")
        print("Сталася помилка")


if __name__ == "__main__":
    main()