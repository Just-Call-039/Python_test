import paramiko
from scp import SCPClient

host = '192.168.1.57'
user = 'glotov'
password = 'MhQqWmvE5zU'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=password)

# # stdin, stdout, stderr = client.exec_command('cd 84.201.164.249')
# stdin, stdout, stderr = client.exec_command('ls')
# print(stdout.readlines())
# client.close()
# ssh = client.invoke_shell()
# print(ssh.sendall('cd 84.201.164.249/10_report'))
# ssh.close()

scp = SCPClient(client.get_transport())
scp.get('/home/glotov/84.201.164.249/10_report/Status.csv', '/Files/')
# scp.put('Test_1.csv', '/home/glotov/84.201.164.249/10_report/')
scp.close()
stdin, stdout, stderr = client.exec_command('rm -f /home/glotov/84.201.164.249/10_report/Status.csv')
client.close()
