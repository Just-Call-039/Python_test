def numerics(n):
    return list(map(int, str(n)))


def kaprekar_check(n):
    if len(str(n)) in (3, 4, 6) and n not in (100, 1_000, 100_000) and len(set(str(n))) != 1:
        return True
    else:
        return False


def kaprekar_step(l):
    a = ''.join(str(i) for i in sorted(l))
    b = ''.join(str(i) for i in sorted(l, reverse=True))
    return abs(int(a) - int(b))


def kaprekar_loop(n, my_l=[]):
    if len(my_l) == 0:
        my_l.append(n)

    if kaprekar_check(n):
        if n != 6174 and n != 495 and n != 549945 and n != 631764:
            new = kaprekar_step(numerics(n))
            my_l.append(new)
            return kaprekar_loop(new, my_l=my_l)

        if n in my_l:
            print(*[i for i in my_l[:-1]], sep='\n')
            print(f'Следующее число - {my_l[-1]}, кажется процесс зациклился...')
        #    return [i for i in my_l[:-1]]
         #   return f'Следующее число - {my_l[-1]}, кажется процесс зациклился...'
        else:
          #  return [i for i in my_l]
            print(*[i for i in my_l], sep='\n')
    else:
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')


kaprekar_loop(103303)
