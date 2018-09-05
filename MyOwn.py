# def vol(rad):
#     volume=((4/3)*3.14*rad*rad*rad)
#     print(volume)
#     
# vol(2)


# def unique_list(lst):
#     print(set(lst))
#     
# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
#     
operand1=int(input("Enter the value of operand 1:"))
operand2=int(input("Enter the value of operand 2:"))
print("-------------------------")
print("1-Add 2-Sub 3-Multiply 4-Divsion 5-Power")
choice=input("Enter the choice")
if choice=="1":
    result=operand1+operand2
    print("Hence the result is",result)
elif choice=="2":
    result=operand1-operand2
    print("Hence the result is",result)
elif choice=="3":
    result=operand1*operand2
    print("Hence the result is",result)
elif choice=="4":
    result=operand1/operand2
    print("Hence the result is",result)
elif choice=="5":
    result=operand1/operand2
    print("Hence the result is",result)
else: 
    print("OOPS! You have entered an invalid operation please enter valid choice")
    print("1-Add 2-Sub 3-Multiply 4-Divsion 5-Power")
