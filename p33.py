def nim_game():
    heaps = [3, 4, 5]
    player = 1

    while True:
        print("Current state of heaps:", heaps)

        # Check if the game is over
        if sum(heaps) == 0:
            print("Player", player, "wins!!")
            break
        
        while True:
            i = int(input("Player " + str(player) + ", choose a heap (0-2): "))
            if i >= 0 and i < len(heaps) and heaps[i] > 0:
                break
            else:
                print("Invalid move. Please choose a non-empty heap within range.")
        
        max_removal = max(1, heaps[i] // 2)  # Maximum number of objects to remove is half the heap size, minimum is 1
        
        while True:
            n = int(input("Player " + str(player) + ", choose the number of objects to remove (1 to " + str(max_removal) + "): "))
            if n > 0 and n <= max_removal:
                break
            else:
                print("Invalid move. Please choose a valid number of objects to remove.")
        
        heaps[i] -= n
        player = 3 - player  # Switch player (if 1 then 2, if 2 then 1)

nim_game()
