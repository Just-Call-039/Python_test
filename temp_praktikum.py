with open('dataset_48784_9.txt') as temp:
    # for now in temp.readlines():
    #     print(*[i[0] for i in now.split()])
    temp = temp.readlines()
    # print(len(temp))
    print(*[i.lower() for i in temp])
    # print(*[i.strip() for i in temp], sep='\n')
    # print(*[i[0] for i in temp])
