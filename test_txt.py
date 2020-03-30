t = open("text.txt", "r")
y = t.read()

print(y.count("world"))
t.close()