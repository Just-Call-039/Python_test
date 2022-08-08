import pandas as pd

res = pd.read_csv('Result_94.csv', sep=';')
transcript_projects = pd.read_excel('transcript_projects.xlsx', 0)
my_request = pd.read_csv('My_request.csv', sep=';')
all_users_clear = pd.read_csv('All_users_clear.csv', sep=';')

print(res.head())
print(transcript_projects.head())
print(my_request.head())
print(all_users_clear.head())

print('---------------------')

all_users_clear.rename(columns={'status': 'clear_status'}, inplace=True)

test = pd.merge(res, all_users_clear, left_on='id_user', right_on='id', how='left')
# result = pd.merge(left, right, left_on=['ochered', 'last_step'], right_on=['ochered', 'last_step'], how='left')
# res['status'].fillna(0, inplace=True)
# print(res['status'] != all_users_clear['status'])

print(test)
print(test[['id_user', 'status', 'clear_status']])
# print(test[['id_user', 'id', 'status', 'status_clear']])

# print(test.filter(test['status'] != test['clear_status']))
# test.to_csv('test_now.csv', sep=';')

us_reg = pd.merge(res, my_request, left_on='id_user', right_on='assigned_user_id', how='left')
us_reg.to_csv('us_reg.csv', sep=';')
