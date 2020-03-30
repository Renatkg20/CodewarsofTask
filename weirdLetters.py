g = "qwertyuiop"
new_string = ""
for i in g:
	num_index = g.index(i)
	if (num_index % 2) !=0:
		big_letters = g[num_index].upper()
		print(big_letters)
		new_string = g.replace(g[num_index], big_letters)
print(new_string)
