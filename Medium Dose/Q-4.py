file = open("log.txt", "r") #Opening the file
data = []
for line in file:
  if line.strip():
    data.append(float(line.strip()))
file.close()
def muchiko(data):
    result = []
    n = len(data)
    for i in range(1, n - 1):
      a = data[i - 1]
      b = data[i]
      c = data[i + 1]
    avg = (a + b + c) / 3
    result.append(avg)
    return result


def sanchiko(data):
  result = []
  n = len(data)
  for i in range(1, n - 1):
    a = data[i - 1]
    b = data[i]
    c = data[i + 1]
    values = [a, b, c]
    values.sort()
    median = values[1]
    result.append(median)
return result

Apply filters
muchiko_filter = muchiko(data)
sanchiko_filter = sanchiko(data)

Print individual filter results
print("Muchiko Filter:")
for d in muchiko_filter:
  print(d)

print("Sanchiko Filter:")
for d in sanchiko_filter:
  print(d)

Hybrid 1 = Sanchiko(Muchiko(data))
hybrid1 = sanchiko(muchiko_filter)
print("Hybrid 1 (Sanchiko on Muchiko):")
for d in hybrid1:
  print(d)

Hybrid 2 = Muchiko(Sanchiko(data))
hybrid2 = muchiko(sanchiko_filter)
print("Hybrid 2 (Muchiko on Sanchiko):")
for d in hybrid2:
print(d)
