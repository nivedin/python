# f=open("65","w")
# print("the name of the file is",f.name)
# print("the name of the file is",f.mode)
# # string=f.read()
# # print(string)
# f.write("this is line 12")
# f.close()
# f=open("newfile.txt","wb")
# f.write("fgdfg")
# f.close()
# None=None
# cubes=[i*10 for i in range(5,9)]
# print(cubes)
# print("sdadjas".upper())
# print(sum((1,2,3,4,5)))
# a=min([sum([11,22]),max(abs(-30),2)])
# print(a)
# def countchar(text,char):
#     count=0
#     for c in text:
#         if c==char:
#             count+=1
#     return count        
# filename=input("enter a filename:")
# with open(filename) as f:
#     text=f.read()
# print(text)    
# print(countchar(text,"r"))
def sum(func,arg):
    return func(func(arg))
def add_five(x):
    return x+5
print(sum(add_five,10))        