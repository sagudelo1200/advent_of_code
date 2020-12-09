import re

valids = 0


def check_passport(passport: str) -> bool:
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = {}

    key_val_pairs = passport.split(' ')

    for key_val in key_val_pairs:
        key_val = key_val.split(':')
        key, val = key_val[0], key_val[1]
        if key == 'byr':
            if int(val) not in range(1920, 2003):
                print(f'{key} invalid: {val}')
                return False
        elif key == 'iyr':
            if int(val) not in range(2010, 2021):
                print(f'{key} invalid: {val}')
                return False
        elif key == 'eyr':
            if int(val) not in range(2020, 2031):
                print(f'{key} invalid: {val}')
                return False
        elif key == 'hgt':
            if val.count('cm'):
                cm = val.replace('cm', '')
                if int(cm) not in range(150, 194):
                    print(f'{key} invalid: {val}')
                    return False
            elif val.count('in'):
                _in = val.replace('in', '')
                if int(_in) not in range(59, 77):
                    print(f'{key} invalid: {val}')
                    return False
            else:
                return False
        elif key == 'hcl':
            if not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', val):
                print(f'{key} invalid: {val}')
                return False
        elif key == 'ecl':
            if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                print(f'{key} invalid: {val}')
                return False
        elif key == 'pid':
            if len(val) != 9:
                print(f'{key} invalid {val}')
                return False
        fields[key] = val

    for val in expected_fields:
        if not fields.get(val):
            return False
    return True


with open('passports.txt', 'r') as file:
    content = file.readlines()
    passport = ''
    for string in content:
        if string != '\n':
            passport += string
        else:
            if check_passport(passport.replace('\n', ' ').strip()):
                valids += 1
            passport = ''

print('\nvalid passports:', valids)
