a = [
	" Death of Salesman - Arthur Miller ",
	" Macbeth - William Shakespeare ",
	" A Separate Peace - John Knowles ",
	" Lord of the Flies - William Golding ",
	"A Tale of Two Cities - Charles Dickens"
		]
y = []
for i in a:
	y.append(str(i).split())

for i in y:
	i.remove('-')

print y 
