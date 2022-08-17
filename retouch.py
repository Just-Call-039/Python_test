import pandas as pd

from tqdm import tqdm

tqdm.pandas()

ptv_1 = '^{}^'
ptv_2 = '^{}_21^'
ptv_3 = '^{}_20^'
ptv_4 = '^{}_19^'
ptv_5 = '^{}_18^'
ptv_6 = '^{}_17^'
ptv_7 = '^{}_16^'
ptv_8 = '^{}_15^'

list_ptv = ('', '_21', '_20', '_19', '_18', '_17', '_16', '_15')

ptv_reg_1 = '{}_nasha'
ptv_reg_2 = '{}_sput'
ptv_reg_3 = '{}_telecom'
ptv_reg_4 = '{}_50'
ptv_reg_5 = '{}_50_40'
ptv_reg_6 = '{}_40_30'
ptv_reg_7 = '{}_30_20'
ptv_reg_8 = '{}_20_0'

list_ptv_reg = ('_nasha', '_sput', '_telecom', '_50', '_50_40', '_40_30', '_30_20', '_20_0')

bln = 10
mts = 11
nbn = 19
dom = 3
rtk = 5
ttk = 6

list_project = (10, 11, 19, 3, 5, 6)
list_project_reg = ('bln', 'mts', 'nbn', 'dom', 'rtk', 'ttk')

patch_df = r'\\10.88.22.128\dbs\bson\contacts.csv'
df = pd.read_csv(patch_df, encoding='utf-8', low_memory=False, chunksize=20000)

index = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
columns = ['phone_work', 'stoplist_c', 'ptv_c', 'region_c', 'network_provider_c', 'base_source_c', 'town_c', 'city_c',
           'priority1', 'priority2', 'last_project', 'next_project', 'last_call']
flag = False
chunks = []

for chunk in df:
    i = 0
    for now in list_project:
        for position in range(len(list_ptv)):
            column_2 = f'{now}{list_ptv_reg[position]}'
            column = f'{list_project_reg[i]}{list_ptv_reg[position]}'
            phrase = f'^{now}{list_ptv[position]}^'
            chunk[column] = chunk['ptv_c'].progress_apply(lambda x: 1 if phrase in str(x) else 0)
        i += 1
    if not flag:
        new_df = chunk
        flag = True
    else:
        chunks.append(chunk)

new_df = pd.concat(chunks, axis=0, ignore_index=True, keys=columns, join='outer')
print(new_df.head(60))

new_df.to_csv(r'\\10.88.22.128\dbs\bson\my_test.csv', sep=';', encoding='utf-8', index=False)
