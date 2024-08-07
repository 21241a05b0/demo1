# Given an array of integers, implement a function to find the maximum sum of a contiguous subarray. Describe your approach and the time complexity of your solution.
import sys
li=[2, 3 ,-4, 1,-2]
def max_sum(ar):

    msum=-sys.maxsize-1 #using kadanes algorithm with time complexity O(n),msum=maxsum 

    csum=0#csum refers to the current sum
    for i in range(len(li)):  #iterating over the array
        csum+=li[i] #adding each element into csum
        if(csum> msum): #if adding the current element increases the sum of the current subbarray then it is considered
            msum=csum  #max sum till now is updated by adding current element ,this ensures that msum till now is achieved
        if csum<0: #if adding the current element reduces the sum to negative then the current subarray couldnot provide max subarray sum 
            csum=0 #so we update it zero
        #this ensures beginning of next subarray and continuing the process to achieve max sum
        #this approach also handles the edge case of array of length 1 and also if the  element is negative

    return msum    
print(max_sum(li))           


#  Implement a function to rotate an array by k positions. Explain your method and the space complexity of your solution.
ar=[1,2,3,4,5,6,7]
k=3    # using inplace rotation with space complexity of O(1)
def k_rotate(ar,k):
    n=len(ar)
    if k<0:
        k=-k #as the rotating direction is not specified we consider k as positive integer
    if k==len(ar):
        return ar #if k==n the rotation would result in the same array
    if k>n:
        k=k%n   #if k>n then k//n times rotation would result the same array so we only require to rotate the array for k%n times

    for i in range(k): 
        temp=ar[i]  #storing the current element to be rotated in temp which takes O(1) space
        ar.remove(ar[i]) #this method removes the element and pushes the next elements by index 1
    #print(ar)
        ar.append(temp)#append method adds the element at the end of the list
    return ar # this approach ensures all the edgecases are passed and space complexity is O(1)
print(k_rotate(ar,k))    



