import zipfile
import re
import pandas as pd

from clickhouse_driver import Client


def my_c(phone):
    try:
        phone = re.sub(r'[ _-]', '', str(phone))
        if phone[0] == '7' and len(phone) == 11:
            phone = '8' + phone[1:]
        elif phone[0] == '8' and len(phone) == 11:
            phone = phone
        elif phone[0] == '9' and len(phone) == 10:
            phone = '8' + phone
        elif phone[0] == '8' and len(phone) > 11:
            phone = phone[0:11]
        elif phone[0] == '7' and len(phone) > 11:
            phone = '8' + phone[1:11]
        elif phone[0] == '9' and len(phone) >= 11:
            phone = '8' + phone[0:10]
        elif phone[0:2] == '+7' and len(phone) >= 12:
            phone = '8' + phone[2:12]
        elif phone[0:2] == '+8' and len(phone) >= 12:
            phone = '8' + phone[2:12]
        elif len(phone) == 0:
            phone = 0
        else:
            phone = 0

    except:
        phone = 0

    finally:
        if str(phone).isdigit():
            pass
        else:
            phone = 0

        return str(phone)


# archive = zipfile.ZipFile(r'E:\2022-03-24\cdek.zip', 'r')
# txt_data = archive.open('base.txt')
#
# k = 0
# for now in txt_data:
#     if k > 100000:
#         print(now.decode("utf-8"))
#     if k == 150000:
#         break
#     k += 1
#
# txt_data.close()

client = Client(host='192.168.1.99', port='9000', user='default', password='jdfwl6812hwe',
                database='suitecrm_robot_ch', settings={'use_numpy': True})

# archive = zipfile.ZipFile(r'E:\2022-03-24\cdek.zip', 'r')
# txt_data = archive.open('numbers.txt')
#
# k = 0
# with open(r'E:\2022-03-24\phone_num.csv', 'w', encoding='utf-8') as file:
#     for now in txt_data:
#         # if k > 100000:
#         now = now.decode("utf-8")
#         try:
#             number = now.split()[1]
#             number = re.split(r'[,; /]', number)
#             for step in number:
#                 step = my_c(step)
#                 if step:
#                     k += 1
#                     print(step)
#                     file.write(f'{step}\n')
#         except:
#             continue
#         # if k == 150000:
#         #     break
#
# print(k)
#
# txt_data.close()
#


#
# archive = zipfile.ZipFile(r'E:\2022-03-24\cdek.zip', 'r')
# txt_data = archive.open('numbers.txt')
#
# for now in txt_data:
#     now = now.decode("utf-8")
#     try:
#         number = now.split()[1]
#         number = re.split(r'[,; /]', number)
#         for step in number:
#             step = my_c(step)
#             if step:
#                 step = pd.DataFrame([step])
#                 print(step.to_sring(index=False))
#                 # client.insert_dataframe(f'INSERT INTO suitecrm_robot_ch.test_phone VALUES {step}')
#     except:
#         continue
#
# txt_data.close()

# my_df = pd.read_csv(r'E:\2022-03-24\phone_num.csv')
# print(my_df.head())
k = 0

# names = ['phone']
chunksize = 10000
marker = '66111100'
with pd.read_csv(r'C:\Users\Supervisor031\Python\Phone_test.csv', chunksize=chunksize, header=0) as reader:
    for chunk in reader:
        chunk['clear_phone'] = chunk['tel1'].apply(my_c)
        chunk['marker'] = marker
        chunk.rename(columns={'tel1': 'phone'}, inplace=True)

        # chunk['clear_phone'] = chunk['clear_phone'].astype('string')
        # chunk['phone'] = chunk['phone'].astype('string')
        # chunk['marker'] = chunk['marker'].astype('string')

        # chunk['clear_phone'] = chunk['clear_phone'].astype('int128')
        # chunk['phone'] = chunk['phone'].astype('int128')
        # chunk['marker'] = chunk['marker'].astype('int128')

        # k += 1
        try:
            client.insert_dataframe('INSERT INTO suitecrm_robot_ch.clear_phone_2 VALUES',
                                    chunk[['phone', 'clear_phone', 'marker']])
            print(chunk)
        except:
            print('NO')
            print(chunk)
            continue
