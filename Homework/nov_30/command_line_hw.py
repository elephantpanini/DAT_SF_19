## Homework exercises ##

#### Question 1 #### 
### Look at the head and the tail of chipotle.tsv in the data subdirectory
### and think for a minute about how the data is structured. 
### What do you think each column means? 
### What do you think each row means? 
### Tell me! (If you're unsure, look at more of the file contents.)

from sys import argv
from itertools import islice 

script, filename = argv

print "Press RETURN to open the file. Or press CONTROL-D to exit."

# Await action from user
raw_input('> ')

# If the user presses RETURN the file will open; if not the file won't open.
print "The file is now opening..."

chipotle_file = open(filename)

# Now the entire file will open
print chipotle_file.read()

print "Press RETURN to review the first 10 lines of the file. Or press CONTROL-D to exit."

# Await action from user
raw_input('> ')

# If the user presses RETURN the first 10 lines of the file will open; if not the file won't open.
print "The first 10 lines are now opening..."

chipotle_file = open(filename,'r')
print chipotle_file.readlines()[0:9]

print "Press RETURN to review the last 10 lines of the file. Or press CONTROL-D to exit."

# Await action from user
raw_input('> ')

# If the user presses RETURN the last 10 lines of the file will open; if not the file won't open.
print "The last 10 lines are now opening..."

chipotle_file = open(filename,'r')
print chipotle_file.readlines()[-10:-9]
