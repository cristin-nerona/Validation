#  File: CreditCard.py

#  Description: Tests if credit card is valid and if valid using Luhn's, returns type 

#  Student Name: Christina Nerona

#  Student UT EID: cmn845

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 2/27/15

#  Date Last Modified: 3/6/15


#This function checks if a credit card number is valid
def is_valid(cc_num):
  if (len(cc_num)==16):
  #Returns cc_num to int for calculations
    cc_num=int(cc_num)
  # Get d0
    d0=cc_num%10
  # Get d1
    d1=(cc_num//10)%10
  # Get d2
    d2=(cc_num//10**2)%10
  # Get d3
    d3=(cc_num//10**3)%10
  # Get d4
    d4=(cc_num//10**4)%10
  # Get d5
    d5=(cc_num//10**5)%10
  # Get d6
    d6=(cc_num//10**6)%10
  # Get d7
    d7=(cc_num//10**7)%10
  # Get d8
    d8=(cc_num//10**8)%10
  # Get d9
    d9=(cc_num//10**9)%10
  # Get d10
    d10=(cc_num//10**10)%10
  # Get d11
    d11=(cc_num//10**11)%10
  # Get d12
    d12=(cc_num//10**12)%10
  # Get d13
    d13=(cc_num//10**13)%10
  # Get d14
    d14=(cc_num//10**14)%10
  # Get d15
    d15=(cc_num//10**15)%10
  # Multiply odd digit by 2 and sum digits
    d15= d15 *2
    d13 = d13 * 2
    d11 = d11 * 2
    d9 = d9 * 2
    d7 = d7 * 2
    d5 = d5 * 2
    d3 = d3 * 2
    d1 = d1 * 2
    
    sum_d15 = (d15 % 10) + (d15 // 10)
    sum_d13 = (d13 % 10) + (d13 // 10)
    sum_d11 = (d11 % 10) + (d11 // 10)
    sum_d9 = (d9 % 10) + (d9 // 10)
    sum_d7 = (d7 % 10) + (d7 // 10)
    sum_d5 = (d5 % 10) + (d5 // 10)
    sum_d3 = (d3 % 10) + (d3 // 10)
    sum_d1 = (d1 % 10) + (d1 // 10)
    

  # Sum of even digits
    sum_even = d2 + d4 + d6 + d8 + d10 + d12 + d14 + d0

  # Sum of odd single digit products
    sum_odd = sum_d15 + sum_d13 + sum_d11 + sum_d9 + sum_d7 + sum_d5 + sum_d3 + sum_d1
    
  # Sum of even digits and single digit products
    sum_digits = sum_even + sum_odd
  # Return True or False
    return (sum_digits % 10 == 0)

      
  elif (len(cc_num)==15):
  #Returns cc_num to int for calculations
    cc_num=int(cc_num)
  # Get d0
    d0=cc_num%10
  # Get d1
    d1=(cc_num//10)%10
  # Get d2
    d2=(cc_num//10**2)%10
  # Get d3
    d3=(cc_num//10**3)%10
  # Get d4
    d4=(cc_num//10**4)%10
  # Get d5
    d5=(cc_num//10**5)%10
  # Get d6
    d6=(cc_num//10**6)%10
  # Get d7
    d7=(cc_num//10**7)%10
  # Get d8
    d8=(cc_num//10**8)%10
  # Get d9
    d9=(cc_num//10**9)%10
  # Get d10
    d10=(cc_num//10**10)%10
  # Get d11
    d11=(cc_num//10**11)%10
  # Get d12
    d12=(cc_num//10**12)%10
  # Get d13
    d13=(cc_num//10**13)%10
  # Get d14
    d14=(cc_num//10**14)%10

  # Multiply odd digit by 2 and sum digits
    d13 = d13 * 2
    d11 = d11 * 2
    d9 = d9 * 2
    d7 = d7 * 2
    d5 = d5 * 2
    d3 = d3 * 2
    d1 = d1 * 2
    
    sum_d13 = (d13 % 10) + (d13 // 10)
    sum_d11 = (d11 % 10) + (d11 // 10)
    sum_d9 = (d9 % 10) + (d9 // 10)
    sum_d7 = (d7 % 10) + (d7 // 10)
    sum_d5 = (d5 % 10) + (d5 // 10)
    sum_d3 = (d3 % 10) + (d3 // 10)
    sum_d1 = (d1 % 10) + (d1 // 10)
   
  # Sum of even digits
    sum_even = d2 + d4 + d6 + d8 + d10 + d12 + d14 + d0

  # Sum of odd single digit products
    sum_odd = sum_d13 + sum_d11 + sum_d9 + sum_d7 + sum_d5 + sum_d3 + sum_d1

  # Sum of even digits and single digit products
    sum_digits = sum_even + sum_odd
  # Return True or False
    return (sum_digits % 10 == 0)

#This function returns the type of credit card
def cc_type(cc_num):
  if (len(cc_num)==16):
  #Returns cc_num to int for calculations
    cc_num=int(cc_num)
  # Get digit d4
    cc4 = cc_num // 1000000000000
    d4 = cc4 % 10
  # Get digit d3
    cc3 = cc_num // 10000000000000
    d3 = cc3 % 10
  # Get digit d2
    cc2 = cc_num // 100000000000000
    d2 = cc2 % 10
  # Get digit d1
    cc1 = cc_num // 1000000000000000
    d1 = cc1 % 10
      
  elif (len(cc_num)==15):
  #Returns cc_num to int for calculations
    cc_num=int(cc_num)
  # Get digit d4
    cc4 = cc_num // 100000000000
    d4 = cc4 % 10
  # Get digit d3
    cc3 = cc_num // 1000000000000
    d3 = cc3 % 10
  # Get digit d2
    cc2 = cc_num // 10000000000000
    d2 = cc2 % 10
  # Get digit d1
    cc1 = cc_num // 100000000000000
    d1 = cc1 % 10

  #Choosing the credit card type
  if (d1==4):
      return('Visa')
  if (d1==5 and d2>=0 and d2<=5):
      return('MasterCard')
  if (d1==6 and ((d2==4 and d3==4) or (d2==5) or (d2==0 and d3==1 and d4==1))):
      return('Discover')
  if (d1==3 and (d2==4 or d2==7)):
      return('American Express')
  else:
      return ("")
      
def main():
  # Prompt the user to enter the credit card number
  cc_num = int (input ('Enter a 15 or 16-digit credit card number: '))
  #Find number of digits in credit card number
  num_digits=len(str(cc_num))
  #Convert credit card number into a string
  str_cc=str(cc_num)
  
  #Check if credit card number is 15 or 16 digits
  if ((num_digits<15) or (num_digits>16)):
    print('Not a 15 or 16-digit number.')
    return
  
  #Return output
  else:
    #If credit card is valid to Luhn's
    if (is_valid(str_cc)):
      print('Valid',cc_type(str_cc),'credit card number')
    #If credit card is in valid to Luhn's
    else:
      print('Invalid credit card number')
main()
