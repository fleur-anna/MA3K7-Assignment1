'''''''''''''''''''''''''''''
MA3K7 ASSiGNMENT 1 CODE

'''''''''''''''''''''''''''''

##########
#Code to prove the conjecture that all chains are bracelets.
##########

#Create for loops to cover all starting options.
for i in range(10):
    for j in range(10):
         chain = [i, j]

	#Create a while loop that keeps adding the sum of the last two elements. to the chain until it loops back around to form a bracelet.
         while chain[-1] != j or chain[-2] != i or len(chain) <= 2:
             chain.append((chain[-1] + chain[-2]) %10)

#Create a command afterwards. If the chains form bracelets then all the code will be executed and the command will be executed.
#If the chains do not form bracelets then the code will continue and the command will never be executed.
print('All the chains form bracelets.')


##########
#Code to find out how many distict bracelets there are.
##########

#I want to create a chain, I then want to find a pair that is not in the chain.
#I then want to find the chain starting with that pair.
#I then want to find what pair is not in either of the 2 chains.
#Then I want to create that chain and so on.

#Defining a function to create a bracelet from the first 2 numbers.
#We know we can do this from the code above.
def bracelet(x, y):

    #Start with the chain as the first 2 elements.
    chain = [x, y]

    #Then keep adding the sum of the last 2 elements of the chain together unti it cycles back around.
    while chain[-1] != y or chain[-2] != x or len(chain) <= 2:
        chain.append((chain[-1] + chain[-2]) %10)
    return chain

#Create a list with all the possible starting combinations.
starters = []
for i in range (10):
    for j in range (10):
        starters.append((i,j))

#Count the number of times the while loop runs, since this will tell us how many different brcaelets there are.
j = 0

#Create a while loop that creates a bracelet from the first entry in the starters list.
#Then remove all the tuples in the starters list that are present in that bracelet.
#This will then repeat with the new starters list. This will continue until nothing is left in the starters list.
while len(starters) > 0:
    chain = bracelet(starters[0][0], starters[0][1])
    for i in range (len(chain) -1):
        if (chain[i], chain[i+1]) in starters:
            starters.remove((chain[i], chain[i+1]))
    j = j+1
print('The number of distinct bracelets is', j)


##########
#Find all the 6 distinct bracelets.
##########

#Using the code above, but printing the bracelet after each loop.
starters2 = []
for i in range (10):
    for j in range (10):
        starters2.append((i,j))
j = 0
while len(starters2) > 0:
    chain2 = bracelet(starters2[0][0], starters2[0][1])
    print('Chain number', j+1, 'is:', chain2)
    for i in range (len(chain2) -1):
        if (chain2[i], chain2[i+1]) in starters2:
            starters2.remove((chain2[i], chain2[i+1]))
    j = j+1

