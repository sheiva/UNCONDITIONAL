import sys
for line in sys.stdin:
	line = line.strip()
	line = line.replace(" the Services ", " my body ")
	line = line.replace("The Services ", "my body ")
	line = line.replace("Terms of Service", "this relationship")
	line = line.replace("NYT", "I ")
	line = line.replace("New York Times", "I ")
	line = line.replace("its", "my")
	line = line.replace("the Site", " our friends")
	line = line.replace("Site", "our friends")
	line = line.replace("The Content", "our love")
	line = line.replace("Contents", "love")
	line = line.replace("your account", "this relationship")
	print line
