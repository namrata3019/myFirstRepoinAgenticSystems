password=''
while password != 'admin123':
    password = input()
    if password == 'admin123':
        print("Access Granted")
    else:
        continue