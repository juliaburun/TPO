
def ordenar(array):
    i = 0
    while(i < len(array)-1):
        if (array[i] > array[i+1]):
            mayor = array[i]
            menor = array[i+1]
            array[i+1] = mayor
            array[i] = menor
            i = 0
        else:
            i += 1
    return array

print(ordenar([22,50,3,1,70,80,90,1120,24,1,3,70]))

