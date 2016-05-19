import itertools, sys, time

def LowestUniqueNumber(line):
  f_hash = {}
  input_data = line.split(" "); 
  
  for item in input_data:
    num = int(item)
    if f_hash.has_key(num):
      f_hash[num] = f_hash[num] + 1
    else:
      f_hash[num] = 1   
  
  index = 0
  for item in f_hash.keys():
    if f_hash[item] == 1:
      index = input_data.index(str(item)) + 1
      break    
    
  print index
  
if __name__ == '__main__':    
  # check if command line arguments format is ok
  assert len(sys.argv) == 2, 'Wrong argument list'
  
  # open file and calculate suitability score for each line
  filename = sys.argv[1]  
  lines = open(filename, 'r').read().splitlines()
  for line in lines:    
    LowestUniqueNumber(line)
