def diagonal_diff(matrix):
    '''
    Calculate absolute difference between diagonals
    :param1 n: array of number, same height and weight
    :return: absolute difference
    '''
    last_m = len(matrix) - 1
    first_m = 0
    result = 0
    for m in matrix:
        result = (result + m[first_m]) - m[last_m]
        first_m+=1
        last_m-=1
    ## return absolute value
    return result if result > 0 else result * -1


def hulk(n):
    '''
    How the hulk feels
    :param1 n: how many times the feling iterates 
    :return: text of hulk feels
    '''
    if n < 1 or n > 100:
        print('Sólo es posible ingresar numeros entre 1 y 100')
        exit()
    text_result = ''
    text1 = 'I hate it'
    text2 = 'I love it'
    for i in range(n):
        if i != 0:
            text_result+= ' that'

        if (i+1) % 2 == 1:
            text_result = text_result + ' ' + text1
        else:
            text_result = text_result + ' ' + text2
    return text_result
        

def ex_functions():
    '''
    Execute all functions
    '''
    m = [[11,2,4],[4,5,6], [10, 8,-12]]
    m1 = [[0,15,2,1],[8,9,8,5], [3,3,16,7],[12,5,22,5]]
    print(m, diagonal_diff(m))
    print(m1, diagonal_diff(m1))

    print(hulk(3))


if __name__=="__main__":
    ex_functions()
