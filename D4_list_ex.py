#sum all numbers in a list
numbers = [1, 2, 3, 4, 5, 6, - 1]
factor = 3
print(sum(numbers))

#find the largest number
print(max(numbers))

#find the largest number
print(max(numbers))


#find the even numbers
even_list = []

for number in numbers:
    if number % 2 == 0:
        even_list.append(number)
print(even_list)

# # #postive numbers
counter = 0
while numbers[counter] > 0:
     print(numbers[counter])
     counter += 1


# postive numbers II
postive_numbers = []

counter = 0
while numbers[counter] > 0:
    postive_numbers.append(numbers[counter])
    counter += 1
print(postive_numbers)

 #multiply a list
factor_mul = []

for numb in numbers:
     factor_mul.append(numb * factor)
print(factor_mul)


# # Multiply Vectors
li1 = [2,-2]
li2 = [5,3]
new_li = []

for num in range(len(li1)):
     new_li.append(li1[num] * li2[num])
     print(len(li1))
 # print(new_li)
    
#Matrix Addition
lis1 = [1, 3, 2, 4]
lis2= [5,2,1,0]
new_li2 = []

for numb in range(len(lis1)):
     new_li2.append(lis1[numb] + lis2[numb])

print(new_li2, end=' ')


#Matrix Addition II
lis3 = [1,2,3,4,5,6,7]
lis4 = [7,8,9,10,11,12, 13]
new_li3 = []

for num5 in range(len(lis3)):
     new_li3.append(lis3[num5] + lis4[num5])
print(new_li3)


#de-dup

de_dup = [1,2,3,4, 3, 1]
de_dup2= []


print('The original list is : ' + str(de_dup))

for de in de_dup:
    if de not in de_dup2:
        de_dup2.append(de)


print("the list after removal is : " + str(de_dup2))
           
#Matrix multiplication
mat1 = [2,2,4,4]
mat2 = [3,3,4,4]
mat3 = []

for mat in range(len(mat1)):
    mat3.append(mat1[mat] + mat2[mat])

print(mat3)


