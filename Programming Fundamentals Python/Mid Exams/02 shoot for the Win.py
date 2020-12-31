targets = list(map(int, input().split()))
shot_counter = []
while True:
    line = input()
    if line == 'End':
        print(f"Shot targets: {len(shot_counter)} -> {' '.join(map(str, targets))}")
        break

    idx_tobe_shot = int(line)
    idx_is_valid = len(targets) > idx_tobe_shot >= 0

    if idx_is_valid:

        for i in range(len(targets)):
            if targets[i] > targets[idx_tobe_shot] and i != idx_tobe_shot and targets[i] != -1:
                targets[i] -= targets[idx_tobe_shot]
                i = 0

            elif targets[i] <= targets[idx_tobe_shot] and i != idx_tobe_shot and targets[i] != -1:
                targets[i] += targets[idx_tobe_shot]
                i = 0

        targets[idx_tobe_shot] = -1
        shot_counter.append(targets[idx_tobe_shot])


