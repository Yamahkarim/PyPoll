#!/usr/bin/env python
# coding: utf-8

# # PyPoll

# Create a Python script that analyzes the votes and calculates each of the following:
# 
#     1.) The total number of votes cast
# 
#     2.) A complete list of candidates who received votes
# 
#     3.) The percentage of votes each candidate won
# 
#     4.) The total number of votes each candidate won
# 
#     5.) The winner of the election based on popular vote.
# 
# 

# In[1]:


#dependencies 
import os
import csv


# In[6]:


#import CSV 
csvpath = 'Data/election_data.csv'


# In[13]:


#read CSV 
with open(csvpath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    #skip header
    csvheader = next(reader)

    #create empty lists to hold data and perform calculations organized by candidate    
    candidate = []
    votes = []
    name = [] 
    
    for row in reader:
        candidate.append(row[2])

    #Use list comprhension to count the number of votes per candidate and output as dictionary
    candidate_count = [[x, candidate.count(x)] for x in set(candidate)]
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])
    
    #zip together vote count with corresponding candidate
    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

   #calculate winner by total votes 
    winner = max(votes)
    
    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]




    


# In[20]:


#Final Calculations 

# 1.) Total Vote Count 
total_votes = len(candidate) 

#2.) Complete list of candidates and vote percentage
correy_total = candidate.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = candidate.count('Li')
li_percent = li_total / total_votes

khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes


# In[23]:


#Print Results to console 
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.1%} ({khan_total})')
print(f'Correy: {correy_percent:.1%} ({correy_total})')
print(f'Li: {li_percent:.1%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.1%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')


# In[22]:


#Print Results to a text file  
with open('PyPoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan_total})', file=text_file)
    print(f'Correy: {correy_percent:.3%} ({correy_total})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li_total})', file=text_file)
    print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winner_name}', file=text_file)
    print(f'-------------------------', file=text_file)


# In[ ]:




