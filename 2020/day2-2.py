from passwords import passwords

count = 0

for pwd in passwords:
    splited_pwd = pwd.split(':')
    password = splited_pwd[1].strip()
    policy, letter = splited_pwd[0].split(' ')
    min, max = policy.split('-')
    min, max = int(min) - 1, int(max) - 1
    if password[min] == letter and password[max] != letter:
        count += 1
    elif password[max] == letter and password[min] != letter:
        count += 1

print(count)
