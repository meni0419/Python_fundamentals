"""1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его. При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен". Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке."""

import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Run a python script")
parser.add_argument("script", help="enter path to the script")
args = parser.parse_args()
if os.path.exists(args.script):
    os.system(f"python {args.script}")
else:
    print(f"File {args.script} does not exist")