people = list(range(1, 31))

die_num = 0
it = iter(people)

while die_num < 15:
	for n in range(8):
		next(it)
	die = next(it)
	people.remove(die)
	
	if 
