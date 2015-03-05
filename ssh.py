# ZenithTao
# this is the python script to send my assignments using pysftp to the school sever
import pysftp

host_name = "xxxxxxx"
user_name = "XXXXX"
user_password = "xxxxxxxxx"

with pysftp.Connection('host_name', username = user_name, password = user_password) as sftp:
    with sftp.cd('/home/ltao5/Documents/') :
        sftp.put('/Users/ZenithTao/Desktop/Python/xxxx.c')