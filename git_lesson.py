def is_palindrom(stroka):
    part1= stroka[:len(stroka)//2]
    rev= part1[::-1]
    part2=stroka[len(stroka)//2:]
    if rev == part2:
        print('True')
    else:
        print('False')
    


text=input(str('ведите текст: '))
is_palindrom(text)
