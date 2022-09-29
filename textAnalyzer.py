#final project python

def textAnalyzer():

	int size=0
	int count=0

	print("This is my text analyzer")


	# file open


	with open("example.txt", "r") as f:

		line = f.readlines()
		for l in line:
			print(l.strip())



	print("the top 5 most frequently used words in the file ")
	print("the number of times the top 5 words are used")
	print("should be sorted by most frequently used count")
	print("the longest word in the document")
	print("the average word size")


textAnalyzer()