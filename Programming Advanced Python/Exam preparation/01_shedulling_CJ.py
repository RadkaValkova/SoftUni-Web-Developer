from collections import deque

tasks = [int(el) for el in input().split(', ')]
treads = deque([int(el) for el in input().split()])
task_to_kill = int(input())

while True:
    current_tread = treads[0]
    current_task = tasks[-1]
    if current_task == task_to_kill:
        print(f'Thread with value {current_tread} killed task {task_to_kill}')
        [print(el) for el in treads]
        break
    elif current_tread >= current_task:
        treads.popleft()
        tasks.pop()
    elif current_tread < current_task:
        treads.popleft()