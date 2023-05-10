#Reading a file
# f = open('myfile.txt', 'r' )
#print(f)
#text = f.read()
#print(text)
#f.close()

#f = open('myfile2.txt', 'w')
#f.write('Hello, world how are you tou!')
#f.close()

#with open('myfile2.txt', 'a'):
 #   f.write('hey i am inside with')

#f = open('myfile.txt', 'r')
#while True:
#    line = f.readline()
#    print(line)
#    if not line:
#        print(line, type(line))
 #       break
 #       print(line)

#f = open('myfile2.txt', 'r')
#i = 0
#while True:
  #  i = i + 1
  #  line = f.readline()
  #  if not line:
  #      break
   # m1 = int(line.split(",")[0])
   # m2 = int(line.split(",")[1])
   # m3 = int(line.split(",")[2])
   # print(f"Marks of students {i} in maths is: {m1*2}")
   # print(f"Marks of students {i} in english is: {m1 * 2}")
   # print(f"Marks of students {i} in sst is: {m1 * 2}")

   # print(line)

f = open('myfile3.txt', 'w')
lines = ['line 1\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close()