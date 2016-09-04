#  File: ISBN.py

#  Description: Verifies if an ISBN number is valid using cumulative sum function twice

#  Student Name: Christina Nerona

#  Student UT EID: cmn845

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 04/01/15

#  Date Last Modified: 04/03/15

def main():
  #Open file to read
  valid_char=list(str(range(10)))
  in_file=open('isbn.txt','r')

  #Open file to write
  isbnOut = open("isbnOut.txt", "w")
  
  #Set count for checking purposes
  i=1
  for line in in_file:
    #Check 1
    #print('Line #',i)

    #Prepping line - strip and remove '-' and extraneous spaces
    i+=1
    initial_copy=line[:]
    line=line.replace('-','')
    line=line.strip()

    #Converting line into a list format
    line=list(line)
    
    #Check 2
    #print(line)

    #Isolate the last digit
    last_digit=line.pop(-1)

    #Copy of new line
    copy_line=line[:]

    #Check to see if other digits exist in the isbn; if so, invalid
    if i in copy_line:
      if not i.isdigit():
        isbnOut.write(initial_copy.strip()+'  invalid \n')
        continue

    #Isolating only digits in isbn
    new_line = [i for i in copy_line if i.isdigit()]

    #Checking if length of new line minus the last number is of appropriate length
    if (len(new_line)==9):
      if (last_digit.isdigit() or last_digit=='X' or last_digit=='x'):
        new_line.append(last_digit) #Append last digit if last digit is X or numbers

      #Replacing X with 10
      for i in range(len(new_line)):
        if (i==len(new_line)-1):
          if (new_line[i]=='X'):
            new_line[i]=10

      #Converting list to int not string   
      new_line= [int(x) for x in new_line]
      #print(new_line)

      #First cumulative sum
      for i in range(1,len(new_line)):
        new_line[i]=new_line[i-1]+new_line[i]
      #Check 3: print(new_line)
        
      #Second cumulative sum
      for i in range(1,len(new_line)):
        new_line[i]=new_line[i-1]+new_line[i]
      #Check 4: print(new_line)
      #print(new_line[-1])
        
      #If div by 11; valid and write
      if (new_line[-1]%11==0):
          isbnOut.write(initial_copy.strip()+'  valid \n')
      #Non valid response
      else:
          isbnOut.write(initial_copy.strip()+'  invalid \n')
      isbnOut.write('')
    #If len is out of bounds for valid; return invalid
    else:
      isbnOut.write(initial_copy.strip()+'  invalid \n')
      isbnOut.write('')
  in_file.close()
  isbnOut.close()
main()
