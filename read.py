data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0 # %=求餘數 例如：7%3=1 (7除以3餘數是1)
			 print(len(data))

print(data[0])