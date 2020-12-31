goal = int(input())
start_level = goal - 30
jump_counter = 0
bad_jump_counter = 0

while True:
    current_jump = int(input())
    jump_counter += 1

    if start_level == goal and current_jump > goal:
        print(f'Tihomir succeeded, he jumped over {goal}cm after {jump_counter} jumps.')
        break
    else:
        if current_jump > start_level:
            start_level += 5
            bad_jump_counter = 0
        elif current_jump <= start_level:
            bad_jump_counter += 1
            start_level = start_level
            if bad_jump_counter > 2:
                print(f'Tihomir failed at {start_level}cm after {jump_counter} jumps.')
                break
