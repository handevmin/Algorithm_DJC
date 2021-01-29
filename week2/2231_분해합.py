n = input()
const = list(n)
const = int(''.join(const))
if const > 54:
    const -= 54
else: const =0
for i in range(55):
    res = const+sum(list(map(int, str(const))))
    if res == int(n):
        break
    if const == int(n):
        const =0
        break
    const+=1
print(const)