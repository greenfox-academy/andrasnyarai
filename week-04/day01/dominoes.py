from domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...

print(dominoes)



length = len(dominoes) - 1
sorted = False
while not sorted:
    sorted = True
    for j in range(length):
        if dominoes[j-1].values[1] > dominoes[j].values[0]:
            sorted = False
            dominoes[j - 1], dominoes[j] = dominoes[j], dominoes[j - 1]
            
print(dominoes)

