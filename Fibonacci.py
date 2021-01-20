sequence = [1]
for i in range(500):
    sequence.append(sequence[i]+sequence[i-1])
print(sequence)