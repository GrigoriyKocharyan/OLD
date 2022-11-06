code = input()
if 'print("' in code:
    if code[-3]=='"' and code[-2]==')'and code[-1]==';':
        for i in range(7,len(code)-3,1):
            print(code[i],end='')
else:
    print('Syntax error = no command with this name')
