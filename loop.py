# def loopthrough(d):
#     for key,values in d.items():
#         print(key)
#         print(values)
#         
# d={"apple":"Iphone 7 plus","Samsung":"Note 9"}
# loopthrough(d)
# class Mobile():
#     def __init__(self,brand,name,price):
#         self.brand=brand
#         self.name=name
#         self.price=price
#     
#     def show(self):
#         print("This mobile is from a {b} brand with a {n} name and has a {p:1.2f}".format(b=self.brand,n=self.name,p=self.price))
# 
# mymobile=Mobile("Apple","IphoneX",97600)
# mymobile.show()
string="Siddhartha"
for i in string[::-1]:
    print(i)