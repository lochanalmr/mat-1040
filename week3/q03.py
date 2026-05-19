username = input()
password = input()

if username == 'admin' and password == 'python123':
    print('Login successful')
elif username != 'admin':
    print('Wrong username')
elif password != 'python123':
    print('Wrong password')