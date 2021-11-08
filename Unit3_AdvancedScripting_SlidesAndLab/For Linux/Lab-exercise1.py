import datetime

f = open("connect.csv", 'r')
count = 0

for line in f:
    tokens = line.split(",")
    second = tokens[1]
    third  = tokens[2]
    print( "second: ", second, " third: ", third)
    if ( count == 0):
      pass
    if (count > 0):
      timestamp = datetime.datetime.strptime(second+" " + third, "%m/%d/%y %H:%M:%S %p")
      print( "timestamp:", timestamp )
    
    count = count + 1
    

