import random


def get_burger_part(filename):
	parts = open(filename)
	text = parts.read()
	lines = text.splitlines()
	count = len(lines)
	count = count - 1
	random_int = random.randint(0, count)
	random_part = lines[random_int]
	return random_part


def make_burger():
	bun = get_burger_part("buns.txt")
	patty = get_burger_part("patties.txt")
	sauce = get_burger_part("sauces.txt")
	veggie = get_burger_part("veggies.txt")
	drug = get_burger_part("drugs.txt")
	attribute = get_burger_part("attributes.txt")

	x = '\n'

	patty = x + patty + x
	sauce = sauce + x
	veggie = veggie + x

	if random.randint(0, 25) <= 5:
			drug = ''
			burger = bun + patty + sauce + veggie + drug + bun
	else:
			drug = drug + x
			burger = bun + patty + sauce + veggie + drug + bun

	if random.randint(0, 10) <= 2:
			burger = burger + x + '(' + attribute + ')'
	return burger