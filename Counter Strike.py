initial_energy = int(input())

distance = input()

won_battle_counter = 0
is_winner = True
while not distance == "End of battle":
    distance = int(distance)

    if initial_energy - distance >= 0:
        initial_energy -= distance
        won_battle_counter += 1
        if won_battle_counter % 3 == 0:
            initial_energy += won_battle_counter
    else:
        print(f"Not enough energy! Game ends with {won_battle_counter} won battles and {initial_energy} energy")
        is_winner = False
        break
    distance = input()

if is_winner:
    print(f"Won battles: {won_battle_counter}. Energy left: {initial_energy}")