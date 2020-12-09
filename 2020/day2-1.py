from passwords import passwords

count = 0

for pwd in passwords:
    splited_pwd = pwd.split(':')
    password = splited_pwd[1].strip()
    policy, letter = splited_pwd[0].split(' ')
    min, max = policy.split('-')
    if password.count(letter) in range(int(min), int(max) + 1):
        count += 1

print(count)
