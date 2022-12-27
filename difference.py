import pandas as pd

df_1 = pd.read_csv(r'\\10.88.22.128\dbs\4_report\Files\main_folder\2022_06.csv', sep=';', low_memory=False)
df_2 = pd.read_csv(r'C:\Users\Supervisor031\2022_06.csv', sep=';', low_memory=False)

# df_3 = df_1.merge(df_2, indicator=True, how='left', left_on='my_phone_work', right_on='my_phone_work').loc[
#     lambda x: x['_merge'] != 'both']
df_3 = df_1.merge(df_2, on='id', how='outer', suffixes=['', '_'], indicator=True)

# print(df_1.head())
print(df_1.info)
# print(df_2.head())
print(df_2.info)
print('-' * 50)
print(df_3[df_3['_merge'] != 'both'])
print('-' * 50)
print(df_3.info)
print('-' * 50)
