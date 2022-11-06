def ask_password(p):
    mp = input()
    a = 1
    while mp != p and a <= 3:
        mp = input()
        a+=1
    if mp==p:
        print('Unlocked')
    else:
        print('Blocked')


p = 'qwerty'
ask_password(p)
ss = 123454
