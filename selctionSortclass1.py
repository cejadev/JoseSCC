
#Make an array for the sorting of the selcion 
#this is kind a selction sort finds the minnum value and pushes it to the front

array = [13, 4, 9, 5, 3, 16, 12] #its not in order so lets get in order 

def selctionSort(array):# pass it into the array that you create #pass it to the array in the function header
   
   #check the lenght of the array how long is the list??len means how many elements are in this particular array list
	n = len(array)

	#loop through the array 

	for i in range(n): # <--- whatever the lenght of the array is how many times you are going to run the for loop
						# this is the unsotrted part 

	 	#Initially assume the first element of the unsorted part as the minimum

	 	minimum = i  #your making a assumption 

	 	for j in range(i+1, n):# this is the sorted part # nested loop u have to swap it 

	 		if (array[j] < array[minimum]): #<-- Comparison operator 

	 		minimum = i

	 		#comparsion value to the minvalue 
	 		#Swap the minim element with the first element of the unsorted part 
	 		#compare the values 

	 		for j in range(i+1, n): 

	 			if (array[j] < array[minimum]):

	 				minimum = j #compare it to the min value

	 			# Swap the minimum element with the first element of the unsorted part 
	 		temp = array[i]
	 		array[i] = array[minimum] #swaping index elements around 
	 		array[minimum] = temp

	 	return array 


	 print(selctionSort(array)) 




