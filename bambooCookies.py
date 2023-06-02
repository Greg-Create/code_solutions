N = int(input())
batches = list(map(int, input().split(' ')))
batches.sort()
max_repeats = 0

print("Batches, ", batches)

while len(batches) > 1:
    current_batch = batches.pop(0)
    previous_batch = batches.pop(0)
    print(current_batch, previous_batch)

    if (current_batch + previous_batch) % 2 == 0:
        max_repeats = max_repeats+1
    

print(max_repeats)