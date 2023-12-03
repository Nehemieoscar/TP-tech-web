tèks = input("Antre yon tèks ki gen chif yo: ")

chif = [int(i) for i in tèks if i.isdigit()]
nonb = int(''.join(map(str, chif)))

faktoryel = 1
if nonb < 0:
    print("Faktoryèl pa egziste pou nonb negatif.")
elif nonb == 0:
    print("Faktoryèl de 0 se 1")
else:
    for i in range(1, nonb + 1):
        faktoryel *= i
    print("Faktoryèl de nonb ki soti nan tèks la se:", faktoryel)
