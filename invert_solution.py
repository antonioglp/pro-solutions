def rotacion_izq(rotacion, arr_entrada):
    for i in range(rotacion):
        elemento = arr_entrada.pop(0)
        arr_entrada.append(elemento)
    return arr_entrada
        

def birth_candle(arr_entrada):
    alto = max(arr_entrada)

    incluido = 0
    for i in arr_entrada:
        if i == alto:
            incluido+=1
    return incluido


def invertido(arr_char):
    arr_fin = list()
    for i in arr_char.split(' '):
        if len(i) >= 5:
            print(reversed(list(i)))
            list().__str__


if __name__=="__main__":
    print(rotacion_izq(2, [1,2,3,4,5]))
    print(birth_candle([1,2,3,54,56,80,80,90,90,90,91.3, 91.4, 91.5]))
    print(invertido('Hey fellow warriors'))
