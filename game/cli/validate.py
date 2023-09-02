def input_int(message=''):
    try:
        selection = int(input(message))
        return selection
    except ValueError:
        print('Valor Invalido...')
        return 0 

def range_input(from_value=0, to_value=0, message=''):
    selection = input_int(message)
    while not((from_value <= selection) and (selection <= to_value)):
        selection = input_int(message)
    return selection