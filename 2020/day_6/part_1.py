def recount(declaration: str) -> int:
    answers = ''

    for answer in declaration:
        if answer not in answers:
            answers += answer
    return len(answers)


with open('customs_declaration.txt', 'r') as file:
    file = file.read().replace('\n\n', '@').split('@')
    counts = 0
    for declaration in file:
        counts += recount(declaration.replace('\n', '').strip())
    print(counts)
