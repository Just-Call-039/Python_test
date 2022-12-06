n = int(input())
my_str = input()

for i in my_str:
    temp = (ord(i) + n) % 25
    now = 122 - temp
    print(chr(now), end='')
