#!usr/bin/python
list1 = [1, 2, 3, 2, 1, 0, 1, 2, 2];
list2 = [0, 1, 0, 0, 0, 0, 0, 0, 0];

n = 2;
while (n <= 8):
       list2[n] = list1[n-1] - list2[n-1] - list2[n-2];
       n = n + 1;
       print (list2);
