#!/usr/bin/python
import sys
import os
import time
from string import ascii_uppercase
import numpy as np

filename = "sumchrg5I6W.out"
lines_ = open(filename).readlines() 

i = 0
mylist_1 = []
mylist_2 = []
nameList = []
 
TITLEformat = '{:10}     {:5}     {:5}       {:5}      {:5}      {:5}\n' 
SUMCHGformat = '{:10s}     {: 2.3f}     {: 2.3f}     {: 2.3f}     {: 2.3f}     {: 2.3f}\n' 


with open("post_sumchrg5I6W.out",'w') as newSUMCHG:
	for row in lines_:  

		lineElements = row.split() 

		# here we only append lineElements[0] (the res names) if it is not the line with "-----"	
		if len(lineElements) != 1:  
			nameList.append(lineElements[0]) #building the nameList
		
		#to make the line elements be only the numbers (which we will perform computations on)
		lineElements = lineElements[1:] 

		for item in lineElements:	#lineElements goes to the side -->
			data = float(item)
			mylist_1.append(data)   # mylist is an array of all the protonation states varying pH
									# so it goes down the line. builds mylist_1, 
									# after this for loop, mylist_1 is an array of all the prot states
									# along a given row (or residue) ***maybe call this list prot state***

		mylist_2.append(mylist_1)   # now outside of last for loop, we put the array we just built of 
									# all the prot states, and we input it into a slot for each residue
									# as we iterate down the list of residues (still in "for row in lines_:" loop)
		
		mylist_1 = []				#now we empty this list again so it can be refilled upon next iteration		



	#initializing our arrays
	avg_list = []
	stdv_list = []
	min_list = []
	max_list = []
	diff_list = []



	for i in range(1,len(lines_)): # i counts each line 

		# following if statement:
		# if this array is not empty (would be for "----" case since we made lineElements = lineElements[1:])
		# then, we will perform calculations on entire array. we will append to avg_list, stdv_list ...etc
		# to build arrays to feed into the final formatting

		if mylist_2[i][1:len(lineElements)-1] != []:

			array = mylist_2[i][0:len(lineElements)+1] 

			#absolute = np.absolute(array)

			
			#avg
			avg = np.average(array)
			avg_list.append(avg)

			#stdv
			stdv = np.std(array)
			stdv_list.append(stdv)



			#min
			minimum = np.nanmin(array)
			min_list.append(minimum)

			#max
			maximum = np.nanmax(array)
			max_list.append(maximum)
			
			#diff
			diff = mylist_2[i][0] - mylist_2[i][len(lineElements)-1]
			diff_list.append(diff)
			


	newSUMCHG.write(TITLEformat.format('RESIDUE','AVERAGE','STDEV','MIN','MAX', 'DIFF'))



	for i in range(0,len(lines_)-2):  # i dont know why 4 doesnt work... or i need to know why i cant average the 4 data points
		newSUMCHG.write(SUMCHGformat.format(nameList[i+1],avg_list[i],stdv_list[i],min_list[i],max_list[i],diff_list[i])) #now this can go in a forloop!

		# 		NOTE:
		# here its length of lines that will be two counts short for the numerical data
		# but one count short for the name data because of the '-----' line in the sumchrg.out file
		# we start 



newSUMCHG.close()		

