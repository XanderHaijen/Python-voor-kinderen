def fibonacci(aantal_nummers):
    """
    De Fibbonacirij is een rij van getallen waarbij het volgende getal de som is van de 2 vorige:
    1,1,2,3,5,8,13,21, ...
    """
    if aantal_nummers == 1:
        return [1]
    elif aantal_nummers == 2:
        return [1, 1]
    else:
        fibonaccirij = [1, 1]
        for stap in range(2, aantal_nummers):
            fibonaccirij.append(fibonaccirij[-1] + fibonaccirij[-2])
        return fibonaccirij


for i in range(1, 20):
    print(f'De eerste {i} getallen in de Fibonaccirij: ')
    print(fibonacci(i), '\n')
