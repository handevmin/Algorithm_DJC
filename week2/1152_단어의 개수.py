word = input()
word = word.strip()
count = 1
for i in word:
    if i == ' ':
        count += 1
if len(word) == 0:
    count -=1
print(count)