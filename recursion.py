import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    # Перевірка наявності директорії призначення, і в разі відсутності - створення
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Рекурсивне читання та копіювання файлів
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)

            # Спроба копіювання файлу
            try:
                copy_file(src_path, dest_dir)
            except Exception as e:
                print(f"Помилка копіювання файлу {src_path}: {e}")

def copy_file(src_path, dest_dir):
    # Визначення розширення файлу
    _, file_extension = os.path.splitext(src_path)

    # Створення піддиректорії за розширенням файлу
    subdir = os.path.join(dest_dir, file_extension[1:])
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    # Копіювання файлу у відповідну піддиректорію
    shutil.copy2(src_path, os.path.join(subdir, os.path.basename(src_path)))

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивно копіює файли та сортує їх за розширенням.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням - 'dist')")
    args = parser.parse_args()

    # Виклик функції копіювання файлів
    copy_files(args.src_dir, args.dest_dir)

if __name__ == "__main__":
    main()
