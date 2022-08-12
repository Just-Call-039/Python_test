k = 0

with open('farma_8.csv', 'r', encoding='utf-8') as temp, open('new_8.csv', 'w', encoding='utf-8') as new_file:
    for now in temp:
        # k += 1
        now = now.split(';')
        try:
            first = now[-2].strip()
        except IndexError:
            first = 0

        try:
            second = now[-1].strip()
        except IndexError:
            second = 0

        print(f'{first} {second}')
        new_file.write(f'{first} {second}\n')
        # if k == 100:
        #     break
