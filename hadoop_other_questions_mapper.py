import sys, csv

#break up string line into an array
reader = csv.reader(sys.stdin, delimiter='\t')

for row in reader:
		
		if len(row) != 19:
			continue
		#print len(row)
		if row[0] == "id" :
			continue
		
		#break up array into valuable information
		if row[3] == "\\N":
			author_id = 0
		else:
			author_id = (row[3])
		if row[0] == "\\N":
			forum_id = 0
		else:
			forum_id = (row[0])
		
		if row[2] == "\\N":
			tag = None;
		else:
			tag_full = row[2]
			tags = tag_full.split(" ")
			
		
		if row[6] == "\\N":
			parent_id = 0
		else:
			parent_id = (row[6])
		
		if row[7] == "\\N":
			abs_parent_id = 0;
		else:	
			abs_parent_id = (row[7])		
		body = row[4]
		
		node_type = row[5]

		time = row[8]
		hour = time[11:13]
		
		

		#break up the body into individual words / remove unecessary characters
		body_temp = row[4].replace('</p>', "?").replace('\n', '?').replace('\N', '?').replace('<p>', '?').replace('<ul>', '?').replace('</ul>', '?').replace('<li>', '?').replace('</li>', '?')
		chars = [',','!','.',';','?','[',']','<','>','/','-','\t','\\','"',"(",")","_",'*',':','&', '%']
		
		body = body_temp.translate(None, ''.join(chars)).strip().split()
		
		#print out the word of from a question body individually as long as associated ID
		if node_type == "question":
			for i in range(0,len(body)):
				if len(body[i]) > 3 and not "=" in body[i] and not "+" in body[i]:
					print "{0}\t{1}\t{2}".format("Q", int(forum_id), body[i])

		else:
			print "{0}\t{1}".format("A", int(abs_parent_id))
		"""
		print '{0}\t{1}\t{2}\t{3}'.format(forum_id, parent_id, abs_parent_id, node_type,)
		#print '{0}\t{1}\t{2}\t{3}'.format(forum_id, node_type, parent_id, abs_parent_id)
		"""
		