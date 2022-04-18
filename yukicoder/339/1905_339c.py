n = int(input())
a = list(map(int, input().split()))
height = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]
freq = [261.6, 294.3, 327.0, 348.8, 392.4, 436.0, 490.5]
period = [round(n/v) for v in freq]
diff = [0]*7
for i, v in enumerate(period):
    for j in range(n-v): diff[i] += abs(a[j]-a[j+v])
print(height[diff.index(min(diff))])