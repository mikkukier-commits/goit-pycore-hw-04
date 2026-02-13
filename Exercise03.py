import sys
from colorama import Fore, Style, init
from pathlib import Path


init(autoreset=True)


# Рекурсивна функція для виведення структури директорії
def print_dir_structure(path: Path, prefix: str = "") -> None:
    if not Path(path).exists():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.")
        return

    if not Path(path).is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не є директорією.")
        return

    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE} {item.name}/")
            print_dir_structure(item, prefix + "    ")
        else:
            print(f"{prefix}{Fore.GREEN} {item.name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED} Вкажіть шлях до директорії як аргумент командного рядка.")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    print(f"{Fore.BLUE}{directory_path.name}/")
    print_dir_structure(directory_path, prefix="    ")
