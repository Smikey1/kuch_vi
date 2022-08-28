num = int(input("Enter number:"))

# def number_checker(yuta_number):
#     odd=[]
#     even=[]
#     for num in range(0,yuta_number):
#         if( num%2 == 0) and (num != 0):
#             even.append(num)
#         else:
#             odd.append(num)
#     print(f"Even list is : {even}, odd list is : {odd}")

# number_checker(num)

odd_list=[]
even_list=[]
[even_list.append(i) if i%2 ==0 else odd_list.append(i) for i in range(0,num)]
print(f"Even list is : {even_list}, odd list is : {odd_list}")