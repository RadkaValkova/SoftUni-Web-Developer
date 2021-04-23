start = int(input())
end = int(input())

# filtered = [x for x in range(start, end + 1)
#             if len([True for d in range(2, 11) if x % d == 0]) > 0]

filtered = [x for x in range(start, end + 1)
            if any(x % d == 0 for d in range(2,11))]

print(filtered)
