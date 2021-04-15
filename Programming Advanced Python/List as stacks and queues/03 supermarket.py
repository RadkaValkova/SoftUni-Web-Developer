from collections import deque

# customers = deque()
#
# while True:
#     line = input()
#     if line == 'End':
#         print(f'{len(customers)} people remaining.')
#         break
#     if line == 'Paid':
#         while customers:
#             print(customers.popleft())
#     else:
#         customers.append(line)


def solve():
    q = deque()
    while True:
        line = input()
        if line == 'End':
            print(f'{len(q)} people remaining.')
            break
        elif line == 'Paid':
            while q:
                print(q.popleft())
        else:
            q.append(line)


solve()