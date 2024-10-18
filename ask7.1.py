cards = [1, 4, 2, 2, 3, 1, 4, 3 ]
N = 8
game = ["closed","closed","closed","closed","closed","closed","closed","closed"]
active_game = True
found = 0
tries = 0
while active_game:
    tries += 1
    first = int(input("Pick a card: "))
    while first < 0 or first >= N or game[first] == "open":
        print("error!")
        first = int(input("Pick a card: "))
    second = int(input("Pick again: "))
    while second < 0 or second >= N or game[second] == "open" or second == first:
        print("error!")
        second = int(input("Pick a card: "))
        game[first] = "temp_open"
        game[second] = "temp_open"
    print(" ")
    for position in range(N):
        if game[position] == "closed":
            print("_", end = " ")
        elif game[position] == "open":
            print(cards[position], end = " ")
        else:#temp_open
            print(game[position])
    print(" ")
    if cards[first] == cards[second]:
        game[first] = "open"
        game[second] = "open"
        found += 2
        if found == N:
            print("Good job, game finished, you tried " + str(tries)+" times")
            active_game = False
    else:
        game[first] = "closed"
        game[second] = "closed"

    for position in range(N):
        if game[position] == "closed":
            print("_", end=" ")
        elif game[position] == "open":
            print(cards[position], end = " ")
        else:  # temp_open
            print(game[position])




