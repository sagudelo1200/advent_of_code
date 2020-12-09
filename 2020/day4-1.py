valids = 0


def check_passport(passport: str) -> bool:
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = {}

    key_val_pairs = passport.split(' ')

    for key_val in key_val_pairs:
        key_val = key_val.split(':')
        key, val = key_val[0], key_val[1]
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

print(valids)
