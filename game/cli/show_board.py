def print_board(board):
    print('                  TABLERO\n')
    print(' '*8,end='')
    for i in 'ABCDEFGHIJKLMNL':
        print(f'{i}',end=' ')
    print()
    for row in range(len(board)):
        if row+1 < 10:
           print(f'  {row+1}  | ', end=' ')
        else:
            print(f' {row+1}  | ', end=' ')
        for column in range(len(board[row])):
            try:
                print(f'{board[row][column].tile.letter}', end=' ')
            except:
                print('_',end=' ')
        print()
    print()

def print_lectern(lectern):
    print('                     ATRIL\n')
    print(f'Letras -> ',end='')
    letters = ''
    letters_index = ''
    for i in range(len(lectern)):
        letters += (f' | {lectern[i].letter}')
        if len(lectern[i].letter) == 1:
            letters_index += (f'   {i+1}')
        else:
            letters_index += (f'    {i+1}')
    letters += (f' |')
    print(letters)
    print(f'Indice -> ',end='')
    print(letters_index)
    print()