def recount(declaration: str) -> int:
    persons = len(declaration.split('\n'))
    answers = {}
    count = 0

    for answer in declaration:
        if answers.get(answer):
            answers[answer] += 1
        else:
            answers[answer] = 1
    for key, val in answers.items():
        if val == persons:
            count += 1
    return count


with open('customs_declaration.txt', 'r') as file:
    file = file.read().replace('\n\n', '@').split('@')
    counts = 0
    for declaration in file:
        counts += recount(declaration.strip())
    print(counts)
