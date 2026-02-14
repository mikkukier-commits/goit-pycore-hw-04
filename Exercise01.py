def total_salary(path: str) -> tuple[float, float]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []

            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                name, salary = line.split(',')
                salaries.append(float(salary))

            if not salaries:
                return 0, 0  # Return 0 if there are no salaries

            total = sum(salaries)
            average = total / len(salaries)

            return total, average

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Файл пошкоджено або виникла помилка: {e}")
        return None, None


if __name__ == "__main__":
    total, average = total_salary('salaries.txt')
    print(
        f"Загальна сума заробітної плати: {total:.0f}, Середня заробітна плата: {average:.0f}")
