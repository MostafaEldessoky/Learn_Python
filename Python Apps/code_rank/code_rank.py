n = input().split(" ")
k = int(n[0])
m = int(n[1])
i = []
for _ in range(k):
  i.append(input().split(" "))

c = []
y = 0
counter = 0
if len(i) == 1:
  for x1 in i[0]:
    if y < int(x1)**2 % m:
      y = int(x1)**2 % m
else:
  while True:
    counter = counter + 1
    if len(i) == 1:
      break
    else:
      for x1 in i[0]:
        for x2 in i[1]:
          if counter == 1:
            t = int(x2)**2
          else:
            t = x2
          c.append((int(x1)**2 + t) % m)
      if len(i) != 1:
        i.pop(0)
        i.pop(0)
        i.append(c.copy())

  for x1 in i[0]:
    if y < x1:
      y = x1
print(y)