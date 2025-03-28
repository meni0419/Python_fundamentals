"""1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его. При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен". Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке."""

import os
import argparse


def run_script(script_path):
    if os.path.exists(script_path):
        os.system(f"python {script_path}")
        print(f"File {script_path} successfully launched")
    else:
        print(f"File {script_path} does not exist")


parser = argparse.ArgumentParser(description="Run a python script")
parser.add_argument("script", help="enter path to the script", default="./HW26_2.py", nargs="?")
args = parser.parse_args()
run_script(args.script)
