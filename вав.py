import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="%(asctime)s:%(levelname)s - %(message)s")


def check_age(age):
    assert age >= 18, "Вам має бути 18 років або більше"
    print("Ви можете використовувати цей сервіс")


try:
    check_age(15)
except AssertionError:
    logging.exception("Помилка перевірки віку")
    print("Вам має бути 18 років або більше")