# -*- coding: utf-8 -*-

username = input('Input Username: ')
password = input('Input password: ')

if len(password) < 8:
    print('Password is too short!')
elif username in password:
    print('Password contains Username')
else:
    print('Password for Username {} is set'.format(username))