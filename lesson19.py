def first():
	def f(x, y, h):
		if h == 3 and x + y >= 67:
			return 1
		elif h == 3 and x + y < 67:
			return 0
		elif h > 3 and x + y >= 67:
			return 0
		elif h % 2 == 0:
			return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x + y, y, h + 1) or f(x, y + x, h + 1)
		else:
			return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x + y, y, h + 1) or f(x, y + x, h + 1)

	for i in range(1, 58):
		if f(i, 9, 1) == 1:
			print(i)
			break


if __name__ == '__main__':
	first()
