import time


# Функция для очистки строки от лишних символов.
def clear(now):
    now = now.split(":")
    # Цепочка шагов.
    steps = ",".join(i.strip() for i in now[0].strip("()").split(","))
    # Количество положительных и отрицательных завершений.
    # На месте индекса 0 - количество положительных завершений.
    # На месте индекса 1 - количество отрицательных завершений.
    # [+, -]: [good, bad].
    chance = now[1].strip().strip("[]").split(",")
    good = int(chance[0].strip())
    bad = int(chance[1].strip())
    return steps, good, bad


def chance(good, bad):
    # Расчет коэффициента. Вероятность наступления плохого шага.
    # chance = bad / (good + bad)
    chance = round(bad / (good + bad), 2)
    return chance


start_time = time.time()
k = 0

# Создаю один файл для объединения данных последних 2 и 3 шагов.
with open("Total_data.csv", "a") as total:
    total.write("steps;positive;negative;chance;\n")
    with open("data_1.txt") as file:
        for now in file:
            steps, good, bad = clear(now)
            my_chance = chance(good, bad)
            print(steps, "and", good, bad, "and", chance)
            # total.write(f"")
            k += 1
            if k == 30:
                break
    # with open("data_2.txt") as file:
    #   for now in file:
    #       total.write(now)

print(f"Время обработки {k} строк составило: {round(time.time() - start_time, 2)} сек.")
