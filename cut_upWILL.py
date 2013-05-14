import sys
import random
 
article = list()
MasterList = list()
 
for line in open('MissedConnections.txt'):
	# strip the lines of carriage returns etc
	line = line.strip()
	# add this data to the set
	article.append(line)
 
random.shuffle(article)
 
comments = list()
 
# for line in open('termsconditions.txt'):
# for line in open('OutputToMarkov.txt'):
for line in open('nytRomanticTerms.txt'):
# for line in open('comments_FINAL3.txt'):
	line2 = line.strip()
	# offset = line.find(".")
	# if offset != -1:
	# 	line2 = line2[:offset+1]
	comments.append(line2)
 
random.shuffle(comments)
 
output = file('Output.txt', 'a')

for line, line2 in zip(article, comments):
	# tmpList = list()
	# tmpList.append(line)
	# tmpList.append(line2)
	# MasterList.append(tmpList)
	# stringText = str(MasterList)
	# output.write(MasterList)

	print line, line2
# output.close()