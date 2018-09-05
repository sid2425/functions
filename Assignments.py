
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# def lesser_of_two_evens(a,b):
#     if a%2 == 0 and b%2 == 0:
#         return min(a,b)
#     else:
#         return max(a,b)
#         
# result=lesser_of_two_evens(2,4)
# print(result)
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# def animal_crackers(text):
#     a=text.split()
#     if(a[0][0]==a[1][0]):
#       return True  
#     else:
#        return False      
# 
# result=animal_crackers('Crazy Kangaroo')
# print(result)

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# def makes_twenty(n1,n2):
#     if (n1+n2==20) or (n1==20 or n2==20):
#         return True
#     else:
#         return False
# 
# result=makes_twenty(18,2)
# print(result)

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# def old_macdonald(name):
#    a=name[0].upper()+name[1:3]+name[3].upper()+name[4:]
#    print(a)
# 
# old_macdonald('thirthala siddartha')

# Given a sentence, return a sentence with the words reversed
# def master_yoda(text):
#     return ' '.join(text.split()[::-1])
# 
# result=master_yoda('I am home')
# print(result)

# def has_33(nums):
#     for i in range(0, len(nums)-1):
#       
#         # nicer looking alternative in commented code
#         #if nums[i] == 3 and nums[i+1] == 3:
#     
#         if nums[i:i+2] == [3,3]:
#             return True  
#     
#     return False
#         
#     
# result=has_33([1, 3, 3])
# print(result)
# def paper_doll(text):
#     result = ''
#     for char in text:
#         result += char * 3
#     return result
# 
# result=paper_doll('Hello')
# print(result)

# def blackjack(a,b,c):
#     sum=a+b+c
#     if sum>=21:
#         print(sum)
#     elif sum<21 and (a==11 or b==11 or c==11):
#         sum=sum-10
#         print(sum)
#     elif sum<21:
#         print("BUST")
#         
# blackjack(5,6,7)    

