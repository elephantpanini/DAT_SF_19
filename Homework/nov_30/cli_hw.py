## Homework exercises ##

#### Question 1 ####
### Look at the head and the tail of chipotle.tsv in the data subdirectory
### and think for a minute about how the data is structured.
### What do you think each column means?
### What do you think each row means?
### Tell me! (If you're unsure, look at more of the file contents.)

from sys import argv
from itertools import islice

script, filename, head_filename, tail_filename = argv

print "Press RETURN to open the file. Or press CONTROL-D to exit."

# Await action from user
raw_input('> ')

# If the user presses RETURN the file will open; if not the file won't open.
print "The file is now opening..."

chipotle_file = open(filename)

# Now the entire file will open
print chipotle_file.read()

print " "

# Sub-questions within the first question
print "*Note*: each column represents a variable to organize the data"

print " "

print "*Note*: each row respresents a qauntitative or qualitative value per variable; \
also, the data is not itemized"

print " "
print " "

print "Press RETURN to proceed"
raw_input('> ')

print "Press RETURN to review the first 10 lines of the file. Or press CONTROL-D to exit."

# Await action from user
raw_input('> ')

# If the user presses RETURN the first 10 lines of the file will open; if not the file won't open.
print "The first 10 lines are now opening..."

# head_filename was created by running the following UNIX command from the CLI: 
## head ~//Desktop/GeneralAssembly/DAT_SF_19/Homework/nov_30/chipotle.tsv
## the contents of this file were then saved by running the follow UNIX command:
### touch head_chipotle.tsv
chipotle_file_head = open(head_filename,'r')
print chipotle_file_head.read()

print " "
print " "

print "Press RETURN to proceed"
raw_input('> ')

print "Press RETURN to review the last 10 lines of the file. Or press CONTROL-D to exit."

# Await action from user
raw_input('> ')

# If the user presses RETURN the last 10 lines of the file will open; if not the file won't open.
print "The last 10 lines are now opening..."

# tail_filename was created by running the following UNIX command from the CLI: 
## tail ~/Desktop/GeneralAssembly/DAT_SF_19/Homework/nov_30/chipotle.tsv
## the contents of this file were then saved by running the follow UNIX command:
### touch tail_chipotle.tsv
chipotle_file_tail = open(tail_filename,'r')
print chipotle_file_tail.read()

print " "

print " "
print " "

print "Press RETURN to proceed"
raw_input('> ')

#### Question 1, ii ####
# How many orders do there appear to be? #
print "How many orders are in the file?"
raw_input('Press RETURN to see the number of orders there appear to be: ')
print "1834 orders"

print " "
print " "

print "Press RETURN to proceed"
raw_input('> ')

#### Question 1, iii ####
# How many lines do there appear to be? #
print "How many lines do there appear to be?"
print "After running the UNIX command 'wc -l chipotle.tsv' I discovered \
there are the following number of lines:"
raw_input('Press RETUN to see the total number of lines: ')
print "4623 lines"

print " "
print " "

print "Press RETURN to proceed"
raw_input('> ')

#### Question 1, iv ####
# Which burrito is more popular, steak or chicken #
print "Which burrito is more popular, steak or chicken?"
print "???????"
print "???????"

print """After running the UNIX command "grep -i 'Chicken Burrito' \
~/Desktop/GeneralAssembly/DAT_SF_19/Homework/nov_30/chipotle.tsv" I discovered \
that the following number of Chicken Burritos were ordered:"""

raw_input('Press RETUN to see the total number of Chicken Burritos ordered: ')
print "553 Chicken Burritos"

print " "

print """After running the UNIX command "grep -i 'Steak Burrito' \
~/Desktop/GeneralAssembly/DAT_SF_19/Homework/nov_30/chipotle.tsv" I discovered \
that the following number of Steak Burritos were ordered:"""

raw_input('Press RETUN to see the total number of Steak Burritos ordered: ')
print "368 Steak Burritos"

print "Press RETURN to proceed"
raw_input('> ')

print "Because more Chicken Burritos were ordered we can conclude \
that Chicken Burritos are more popular than Steak Burritos."

print "Press RETURN to proceed"
raw_input('> ')

#### Question 1, v ####
print "Do chicken burritos more often have black beans or pinto beans?"
print "???????"
print "???????"

print """After running the UNIX command "grep -i 'Chicken Burrito' \
~/Desktop/GeneralAssembly/DAT_SF_19/Homework/nov_30/chipotle.tsv \
| grep -i 'Black Beans' | wc -l" I discovered \
that the following number of orders of Black Beans accompanied \
orders of Chicken Burritos:"""

raw_input('Press RETUN to see the total number of orders of Black Beans \
that accompanied Chicken Burritos: ')
print "282 orders of Black Beans accompanied Chicken Burritos"

print " "

print """
After running the UNIX command "grep -i 'Chicken Burrito' \
~/Desktop/GeneralAssembly/DAT_SF_19/Homework/nov_30/chipotle.tsv \
| grep -i 'Pinto Beans' | wc -l" I discovered \
that the following number of orders of Pinto Beans accompanied \
orders of Chicken Burritos:
"""

raw_input('Press RETUN to see the total number of orders of Pinto Beans \
that accompanied Chicken Burritos: ')
print "105 orders of Pinto Beans accompanied Chicken Burritos"

print "Press RETURN to proceed"
raw_input('> ')

print "Therefore, Chicken Burritos more often have black beans."

print "Press RETURN to proceed"
raw_input('> ')

#### Question 2 ####
print """
Make a list of all of the CSV or TSV files in the DAT_SF_19 repo \
(using a single command).
"""
# Think about how wildcard characters can help you with this task.
print """
After running the UNIX command "find ~/Desktop/GeneralAssembly/DAT_SF_19/ -name *sv \
I successfully listed all of the CSV or TSV files in the DAT_SF_19 repo."
"""

#### Question 3 ####
print """
Count the number of occurrences of the word 'dictionary' \
(regardless of case) across all files in the DAT_SF_19 repo.
"""
print """
After running the UNIX command "grep -r -i 'dictionary' \
~/Desktop/GeneralAssembly/DAT_SF_19/ | l wc -l \
I discovered that there are 7 occurances of the word dictinoary."
"""

#### Optional Question ####
print """
After running the UNIX command \
'uniq ~/Desktop/GeneralAssembly/DAT_SF_19/Homework/nov_30/chipotle.tsv \
| wc -l' \
I discovered that there are 4589 unique rows in the file.
"""