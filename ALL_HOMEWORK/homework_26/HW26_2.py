"""2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории и выводит список всех файлов и поддиректорий внутри этой директории. Для этой задачи используйте модуль os и его функцию walk. Программа должна выводить полный путь к каждому файлу и директории."""

import os
import argparse


def list_directory(path):
    for root, dirs, files in os.walk(path):
        dirs.sort()  # Sort directories alphabetically in ascending order
        level = root.replace(path, '').count(os.sep) # counts the number of directory separators, thus giving depth level)
        indent = '    ' * level
        print(f"{indent}[DIR]      {os.path.basename(root)}/")
        sub_indent = '    ' * (level + 1)
        for file in sorted(files):  # Sort files alphabetically in ascending order
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            print(f"{sub_indent}[FILE]       {size:>10} B  {file}")


parser = argparse.ArgumentParser(description="List directory contents.")
parser.add_argument("path", nargs="?", default="./",
                    help="Path to the directory to list.\nExample usage:\npython w1.py ./"
)
args = parser.parse_args()

list_directory(args.path)