import sys
from colorama import Fore, Style, init
from pathlib import Path


init(autoreset=True)


# Рекурсивна функція для виведення структури директорії
def print_dir_structure(path: Path, prefix: str = "") -> None:
    if not path.exists():  # Перевірка на існування шляху
        print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.")
        return

    if not path.is_dir():  # Перевірка на те, чи є шлях директорією
        print(f"{Fore.RED}Помилка: '{path}' не є директорією.")
        return
    try:
        # Сортуємо елементи для більш організованого виведення
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE} {item.name}/")
                print_dir_structure(item, prefix + "    ")
            else:
                print(f"{prefix}{Fore.GREEN} {item.name}")
    except PermissionError:
        print(f"{Fore.RED}Помилка: Немає доступу до директорії '{path}'.")
    except Exception as e:
        print(f"{Fore.RED}Сталася невідома помилка при обробці '{path}': {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED} Вкажіть шлях до директорії як аргумент командного рядка.")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    print(f"\n{Fore.BLUE}{directory_path.name}/")
    print_dir_structure(directory_path, prefix="    ")
