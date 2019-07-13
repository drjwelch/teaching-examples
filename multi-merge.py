#!/usr/bin/python
import os, sys, time
import math, random
from multiprocessing import Process, Manager
 
# This is the function that will be run by each thread
# It will split and sort the data into sublists
def merge_sort_multi( list_part,results):
  results.append( merge_sort( list_part ) )
 
# explained earlier
def merge_sort(a):
  length_a = len(a)
  if length_a <= 1: return a
  m = int(math.floor(length_a / 2))
  a_left = a[0:m]
  a_right = a[m:]
  a_left = merge_sort(a_left)
  a_right = merge_sort(a_right)
  return merge(a_left, a_right)
 
# ... also explained earlier
def merge(left, right):
  a = []
  while len(left) > 0 or len(right) > 0:
    if len(left) > 0 and len(right) > 0:
      if left[0] <= right[0]:
        a.append(left.pop(0))
      else:
        a.append(right.pop(0))
    elif len(left) > 0:
      a.extend(left)
      break
    elif len(right) > 0:
      a.extend(right)
      break
  return a
 
if __name__ == '__main__':

  print("Multi-core Merge Sort")
  print("=====================")
  
  cores = 2  # set to the number of CPU cores in your PC (2 for the i3s we have)
   
  # The Manager object is the process that controls the threads
  manager = Manager() 

  # This is the list that will hold the results - it is owned by Manager so that
  # it is accessible to all the threads ('global')
  results = manager.list()
   
  # Create an unsorted list of 100,000 random numbers
  NUMDATA = 100000
  mydata = [ random.randint(0, 100) for n in range(0, NUMDATA) ]

  # First run the merge sort with a single thread  
  start_time = time.time()
  single = merge_sort(mydata)
  single_core_time = time.time() - start_time
  print('Single Core:',round(single_core_time,2),'s')

  # Now do with 2 or 4 threads ...
  start_time = time.time()
  # Divide the list in "cores" parts
  size_per_core = int( NUMDATA/cores )
  # Create a list to hold the thread IDs
  p = []
  # Create the processes
  for n in range(0, cores):
    proc = Process( target=merge_sort_multi, args=(mydata[n*size_per_core:(n+1)*size_per_core],results) )
    p.append(proc)
  # Start all the processes
  for proc in p:
    proc.start()
  # Wait until all are completed
  for proc in p:
    proc.join()
  end_split_time = time.time()
  multi_core_sort_time = end_split_time - start_time
  # Split done, now merge
  # NB merging two lists needs to be done on one thread
  # but if we had 4 cores, we could merge each pair of lists on a separate thread
  start_time_final_merge = time.time()
  mydata = merge(results[0], results[1])
  final_merge_time = time.time() - start_time_final_merge

  print(cores,'Core:',round(multi_core_sort_time+final_merge_time,2),'s')
  print('Final merge duration : ', round(final_merge_time,2),'s')
  print('Single core sort-only time:',round(single_core_time-final_merge_time,2),'s')
  print(cores,'core sort-only time:',round(multi_core_sort_time,2),'s')
  
