Problem Statement:
There's an array with equal number of positive and negative elements.Without altering the realtive order of positive and negative Elements,  you must return an array of alternatively positive and negative
value. NOTE: start the array with positive element.

Example : Input : arr = [1,2,-4,-6]
output : 1 -4 2 -6

Optimal method:
As we know that must start from a positive element so we intialize the positive index as 0 and negative index as 1 and start traversing the array  whenever we see the positive element
it occupies  the space 0 and then posIndex increase by 2.(alternate place). similiarly  for negative element.

