def arithmetic_arranger(problems, show_answers=False):
    equations = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for p in problems:
        if '+' in p:
            terms = p.split('+')
            sign = '+'
        elif '-' in p:
            terms = p.split('-')
            sign = '-'
        else:
            return "Error: Operator must be \'+\' or \'-\'."

        first_term, second_term = [term.strip() for term in terms]

        if not first_term.isdigit() or not second_term.isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(first_term) > 4 or len(second_term) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        equations.append({"first_term": first_term, "second_term": second_term, "sign": sign})
        divider_length = max(len(first_term), len(second_term)) + 2
    
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    for equation in equations:
        first_term, second_term, sign = equation.values()
        divider_length = max(len(first_term), len(second_term)) + 2
        spaces_in_front_first_term = divider_length - len(first_term)
        spaces_in_front_second_term = divider_length - len(second_term) - 1
        first_line += spaces_in_front_first_term * ' ' + first_term + 4 * ' '
        second_line += sign + spaces_in_front_second_term * ' ' + second_term + 4 * ' '
        third_line += divider_length * '-' + 4 * ' '
        if sign == '+':
            answer = str(int(first_term) + int(second_term))
        elif sign == '-':
            answer = str(int(first_term) - int(second_term))
        spaces_in_front_answer = divider_length - len(answer)

        fourth_line += spaces_in_front_answer * ' ' + answer + 4 * ' '

    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    fourth_line = fourth_line.rstrip()
    if show_answers == True:      
        return f'{first_line}\n{second_line}\n{third_line}\n{fourth_line}'
    else:
        return f'{first_line}\n{second_line}\n{third_line}'

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"], True)}')
