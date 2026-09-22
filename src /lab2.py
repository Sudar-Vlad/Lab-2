# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: 5 варіант (впишіть свій варіант)
# ПІБ: Міщенко Владислав (впишіть своє ПІБ)

from functools import reduce

# Звичайні функції: додає спортсмена та показує рещультат
def add_athlete(athletes, name, time):
    athletes.append({
        "name": name,
        "time": time
    })

def show_athletes(athletes):
    if not athletes:
        print("Немає результатів.")
        return

    for athlete in athletes:
        print(f"{athlete['name']} — {athlete['time']} с")

# Функція з параметром за замовчуванням
def calculate_average_time(athletes, extra_time=0):
    if not athletes:
        return 0

    total = sum(athlete["time"] for athlete in athletes)
    return (total + extra_time) / len(athletes)

# Функція зі змінною кількістю аргументів
def find_best_time(*times):
    return min(times)

# Рекурсивна функція: пошук найкращого часу
def recursive_best_time(athletes, index=0):
    if index == len(athletes) - 1:
        return athletes[index]["time"]

    next_best = recursive_best_time(athletes, index + 1)
    return min(athletes[index]["time"], next_best)

# Власне сортування: від меншого часу до більшого
def custom_sort(athletes):
    result = athletes.copy()

    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if result[j]["time"] > result[j + 1]["time"]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

def main():
    athletes = []

    while True:
        print("\n--- РЕЗУЛЬТАТИ З БІГУ ---")
        print("1. Додати спортсмена")
        print("2. Показати результати")
        print("3. Середній час")
        print("4. Найкращий час рекурсією")
        print("5. Сортувати результати")
        print("6. map, filter, reduce")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            try:
                name = input("Ім'я спортсмена: ").strip()
                time = float(input("Час у секундах: "))

                if not name or time <= 0:
                    print("Некоректні дані.")
                else:
                    add_athlete(athletes, name, time)
                    print("Результат додано.")

            except ValueError:
                print("Час повинен бути числом.")

        elif choice == "2":
            show_athletes(athletes)

        elif choice == "3":
            average = calculate_average_time(athletes)
            print(f"Середній час: {average:.2f} с")

        elif choice == "4":
            if athletes:
                best = recursive_best_time(athletes)
                print(f"Найкращий час: {best:.2f} с")
            else:
                print("Немає результатів.")

        elif choice == "5":
            show_athletes(custom_sort(athletes))

        elif choice == "6":
            if not athletes:
                print("Немає результатів.")
                continue

            # map: отримує всі результати часу
            times = list(map(lambda athlete: athlete["time"], athletes))

            # filter: спортсмени, які пробігли швидше 15 секунд
            fast_athletes = list(
                filter(lambda athlete: athlete["time"] < 15, athletes)
            )

            # reduce: сума всіх результатів часу
            total_time = reduce(lambda x, y: x + y, times, 0)

            print("Усі часи:", times)
            print("Кількість спортсменів швидше 15 с:", len(fast_athletes))
            print(f"Сума всіх результатів: {total_time:.2f} с")

        elif choice == "0":
            print("На все добре!")
            break

        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()

# Не забувайте форматувати вивід та додавати коментарі!
