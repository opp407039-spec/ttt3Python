import colorama
from colorama import Fore, Back, Style

print("Версія:", colorama.__version__)
print("Атрибути та методи:", [n for n in dir(colorama) if not n.startswith("_")])

print("Fore.RED =", repr(Fore.RED))
print("Back.BLUE =", repr(Back.BLUE))
print("Style.BRIGHT =", repr(Style.BRIGHT))

colorama.init(autoreset=True)

print(Fore.RED + "Червоний текст")
print(Fore.GREEN + Style.BRIGHT + "Яскравий зелений текст")
print(Fore.YELLOW + Back.BLUE + "Жовтий текст на синьому фоні")

colorama.deinit()