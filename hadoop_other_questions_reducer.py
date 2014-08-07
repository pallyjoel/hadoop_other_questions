import sys
from operator import itemgetter

answer_id = []

#words from questions with answers
w_ans = {}

#words from questions without answers
wo_ans = {}

#identifies if an id is present in an array
def findid(id, array):
	found = False;
	for i in array:
		if id == i:
			found = True;
	return found

	
for row in sys.stdin:

	data = row.strip().split('\t')
	
	if len(data) == 2:
	# Create an array of all IDs that have answers
		id = int(data[1])
		
		if findid(id, answer_id) == False:
			answer_id.append(id)
			
		
	if len(data) == 3:
		ida = int(data[1])
		word = data[2]
	# Identify whether a question ID is associated with an answer
	# build a dictionary of words with counts for each category
		if findid(id, answer_id) == False:
			try:
				wo_ans[word] += 1
			except KeyError:
				wo_ans[word] = 1
		else:
			try:
				w_ans[word] += 1
			except KeyError:
				wo_ans[word] =1
			
# categories are sorted by count of each word
sorted_w = sorted(w_ans.items(), key=itemgetter(1))

sorted_wo = sorted(wo_ans.items(), key=itemgetter(1))


print "top words from unanswered questions"
for i in range(10):
	print sorted_wo[i][0], sorted_wo[i][1]	

print "top words from answered questions"
for i in range(10):
	print sorted_w[i][0], sorted_w[i][1]	
		
		
		
		
		