from datetime import time, timedelta, datetime
import time


# Функция для очистки строк от лишних символов.
def clear(my_str):
    # Разделение исходной строки по разделителю.
    my_str = my_str.split(";")
    # После разделения получаем значения из списка по индексам.
    my_str_id = my_str[0].strip().strip("''").strip('""')
    my_str_time = my_str[1]
    my_str_steps = [i.strip().strip('""') for i in my_str[2].split(",") if i.strip().strip('""').isdigit()]
    # Возврат ид, времени, шагов.
    return my_str_id, my_str_time, my_str_steps


start_time = time.time()

# Открываем (создаем) файл для записи новых данных.
with open("steps_ver_3_clear.csv", "w", encoding="utf-8") as new_file:
    # Открываем файл для чтения исходных данных.
    with open("steps_ver_3.csv", encoding="utf-8") as file:
        # Итерация по строкам.
        for now in file:
            # Запись заголовков.
            if now.split(";")[0] == "id":
                new_file.write(now.replace("route", "event"))
            # Запись значений.
            else:
                now_id, now_time, now_steps = clear(now)
                # Строки с пустыми ид пропускаем.
                if now_id == "":
                    continue
                # Строки с действующими ид берем в работу.
                else:
                    # Коэффициент для разделения шагов для каждого из взятых ид.
                    k = 0
                    for i in now_steps:
                        if k == 0:
                            # Запись первого шага для ид.
                            new_file.write(f"{now_id},{now_time},{now_steps[k]}\n")
                            my_date = tuple(int(i) for i in (now_time.split()[0]).split("-"))
                            my_time = tuple(int(i) for i in (now_time.split()[1]).split(":"))
                            # Запись даты и времени.
                            my_date_time = datetime(my_date[0], my_date[1],
                                                    my_date[2], my_time[0], my_time[1], my_time[2])
                        else:
                            # Ко времени следующего шага прибавляем 1 секунду.
                            my_date_time = my_date_time + timedelta(seconds=1)
                            # Записываем новый шаг для этого же ид.
                            new_file.write(f"{now_id},{my_date_time},{now_steps[k]}\n")
                            # print(my_date_time)
                        k += 1

print(f"Время обработки файла составило: {round(time.time() - start_time, 2)} сек.")
