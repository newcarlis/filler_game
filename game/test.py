from os import system
import keyboard
import sys

import time

uni = "\u27A4"
print("hello")
print("hello")
print("hello")
print()

time.sleep(5)
# system("cls")
for i in range(2):
    # sys.stdout.write("\033[F")
    # print("\033[F")
    sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")
print(uni)

time.sleep(5)
for i in range(1):
    # sys.stdout.write("\033[F")
    # print("\033[F")
    sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")
# print("hola")
sys.stdout.write("a")
print("\033[A")

