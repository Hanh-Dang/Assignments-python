#Hello
def say_hello(name):
    print("Hello", name)

#Total
def total(a,b):
    print(a+b)

#Operation
def Operation(a,b):
    print(f"{a} + {b} =",a+b) #f 'str'/"str" với giá trị biến được gán trong {}.
    print(f"{a} - {b} =",a-b)
    print(f"{a} * {b} =",a*b)
    print(f"{a} / {b} =",a/b)

#Variables and type of variables 
def variables():
    a = 5
    b = 3.14
    c = "Hello"
    d = True
    e = [1, 2, 3]
    f = (1, 2, 3)
    g = {1: "one", 2: "two"}
    h = None

    print(type(a)) #int
    print(type(b)) #float
    print(type(c)) #str
    print(type(d)) #bool
    print(type(e)) #list
    print(type(f)) #tuple
    print(type(g)) #dict
    print(type(h)) #NoneType

#input
def greet():
    print(f"Hello {input("Enter your name:" )}")
 
#input2
def Information():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"In 15 years, age of {name} will be {age + 15}")

#test 
def tinhtoan():
    a = int(input())
    b = int(input())
    print("a + b =" + str(a+b))  #print("a + b =",a+b) 
    print("a - b =" + str(a-b))  #print("a - b =",a-b)
    print("a * b =" + str(a*b))  #print("a * b =",a-b)
    print("a / b =" + str(a/b))  #print("a / b =",a-b)
    print("a % b =" + str(a%b))  #print("a % b =",a-b)

#Swap value
def Swap():
    a = int(input())
    b = int(input())
    c = a
    a = b
    b = c
    print("after swap a = " + str(a) + ", b = " + str(b))

#exponential
def exponential():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(f"{a} ^ {b} = {a**b}")

#Operator
def operator():
    a = int(input())
    Total = int(input())
    Total += a # Using += Operator
    print("The Value of the Total after using += Operator is:", Total)
    Total -= a # Using -= Operator
    print("The Value of the Total after using -= Operator is:", Total)
    Total *= a # Using *= Operator
    print("The Value of the Total after using *= Operator is:", Total)
    Total //= a # Using //= Operator
    print("The Value of the Total after using //= Operator is:", Total)
    Total **= a# Using **= Operator
    print("The Value of the Total after using **= Operator is:", Total)
    Total /= a# Using /= Operator
    print("The Value of the Total after using /= Operator is:", Total)
    Total %= a # Using %= Operator
    print("The Value of the Total after using %= Operator is:", Total)# Toán tử &= thực hiện phép AND bitwise giữa hai số. -Giữ lại các bit đều là 1 ở cả hai số. Ví dụ: 6 (0110) & 3 (0011) = 2 (0010).

#Membership_operator
def membership_operator():
    x = input("Enter a string: ")
    print("H" in str(x))
    print("Y" not in str(x))

#identity_operator
def identity_operator():
    a = 5
    b = 7
    c = 5
    print(a is b)#False
    print(a is c)#True
    print(a is not b)#True
    print(a is not c)#False

#logicall_operator
def logicall_operator():
    x = int(input())
    y = int(input())
    z = int(input())
    t = int(input())
    print("Result evuluation is",(x > y) and (z < t)) #Ca 2 deu kien deu dung thi tra ve True
    print("Result evuluation is",(x > y) or (z < t)) #Chi can 1 trong 2 kiem tra dung thi tra ve True
    print("Result evuluation is",not(x > y)) #Tra ve True neu x khong lon hon y
    print("Result evuluation is",not(x > y) and (z < t)) #Tra ve True neu x khong lon hon y va z nho hon t
    print("Result evuluation is",not(x > y) or (z < t)) #Tra ve True neu x khong lon hon y hoac z nho hon t

#if_else
def condition1():
    age = int(input("Enter your cat's age:"))
    print("Your cat is young") if age <5 else print("Your cat is old") #Toán tử 3 ngôi if-else

    """
    if age < 5:print("Your cat is young")
    else: print("Your cat is old")
    """
#if_else2
def condition2():
    temperature = int(input("Enter the temperature: "))
    if temperature >= 100: 
        print("Stay at home and enjoy a good movie")
    elif temperature >= 92: # elif = else : if codition : print....
        print("Stay at home")
    elif temperature ==75: 
        print("Go outside and enjoy the weather")
    elif temperature <= 0 :
        print("It's cool outside")
    else: 
        print("Let's go to school")
    
#if_else3
def condition3():
    x = int(input("Enter number x: "))
    y = int(input("Enter number y: "))
    z = int(input("Enter number z: "))

    if x % 2 == 0:  #if lồng if điều kiện lồng điều kiện.
        if y >= 20: 
            print("y is greater than or equal to 20")
    if x % 2 != 0:
        if z >= 30:
            print("z is greater than or equal to 30")
        else: print("z is less than 30")

#if_else4
def condition4():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    avg = (a + b + c)/3

    if avg >a and avg >b: #Use and operator to check if avg is greater than both a and b
            print("The average value is greater than both a and b")
    elif avg >a and avg >c:
            print("The average value is greater than both a and c")
    elif avg >b and avg > c:
            print("The average value is greater than both b and c")
    elif avg > a:
        print("The average value is greater than a")
    elif avg >b:
        print("The average value is greater than b")
    elif avg >c:
        print("The average value is greater than c")

#ForLoop
def forloop():
    name = "codelearn"
    n = int(input("Enter a number: "))
    total = 0
    for i in range(1,n+1) :
        total +=i
    print("Total from 1 to",n,"is",total) #Tính tổng từ 1 đến n
    for e in name:
        print(e) #In từng ký tự trong chuỗi name

#ForLoop2
def forloop2():
    a = int(input("Enter a: "))
    b = int(input("Enter b: ")) 
    total = 0
    for i in range(a,b+1): #Tính tổng từ a đến b
        if i % 2!= 0:
            total += i
        i +=1
    print("Total of odd numbers from a to b is",total) #Tính tổng các số lẻ từ a đến b

    
#Whileloop
def whileloop():
    n = int(input("Enter a number: "))
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print("Total from 1 to",n,"is",total) #Tính tổng từ 1 đến n

#Whileloop2
def whileloop2():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    total = 0
    while a <= b:
        if a % 2 == 0:
            total += a
        a += 1
    print("Total of even numbers from a to b is",total)

#continue/break
def continue_break():
    n = int(input("Enter a number: "))
    a = int(input("Enter n: "))
    for i in range(1,n+1):
        if i == a:
            continue #Bỏ qua số 5
        print(i, end=" ")
    print()
    for i in range(1,n+1):
        if i == a6:
            break #Dừng vòng lặp khi gặp số 5
        print(i, end=" ")

#Total_use_round
def total_round():
    a = int(input("Enter a: "))
    total = 0
    for i in range(1,a+1): #khong su dung for voi float
        total += i/(i+1)
    print("Total is",round(total,2)) #Làm tròn đến 2 chữ số thập phân

#list
def list1():
    n = int(input("Enter quanity of list: "))
    list1 = []
    for i in range(n): #lặp n lần với i từ 0 đến n-1
        list1.append(int(input("Enter number: "))) #Thêm số vào list1
    value_min = list1[0] #Giá trị đầu tiên trong list1
    for i in list1:
        if i < value_min:
            value_min = i
    print("The minimum value in the list is",value_min) #In giá trị nhỏ nhất trong list1 // ta có thể dùng min(list1) để tìm giá trị nhỏ nhất trong list1

#list2
def list2():
    n = int(input("Enter quanity of list: "))

    list = []
    for i in range(n):
        list.append(int(input("Enter number: "))) #Thêm số vào list5
    total = 0
    for a in list:
        total += a # sum(list) = sum(list1) + sum(list2) + sum(list3) + ... + sum(listn)
    print("Total of the list is",total)

#list3
def list3():
    n = int(input("Enter quanity of list: "))
    list3 = []
    for i in range(n):
        list1.append(int(input("Enter number: ")))
    for i in range(len(list3)): #i không thể bằng 0 vì không có phần tử nào trong list3
        for j in range(i): #Duyệt qua từng phần tử trong list3 
            if list3[i] < list3[j]:
                list3[i], list3[j] = list3[j], list3[i] # tmp = list[i], list[i] = list[j], list[j] = tmp
    print("The sorted list is",list3) #In danh sách đã được sắp xếp theo thứ tự tăng dần

#Max_min
def Max_min():
    lst = [1, 2, 3, 4, 5]
    print("Max value in the list is",max(lst)) #Tìm giá trị lớn nhất trong lst
    print("Min value in the list is",min(lst)) #Tìm giá trị nhỏ nhất trong lst

#insert
def insertt():
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels.insert(3,'y') #Thêm 'y' vào vị trí thứ 3 trong danh sách vowels
    print("The list after inserting 'y' is",vowels) #In danh sách vowels sau khi thêm 'y'

#remove
def removee():
    lst = ['A' , 'B' , 'C' , 'D' , 'E']
    lst.remove('C') #Xóa phần tử 'C' trong danh sách lst
    print("The list after removing 'C' is",lst) #In danh sách lst sau khi xóa 'C' 

#pop
def popp():
    lst = ['A' , 'B' , 'C' , 'D' , 'E']
    lst.pop(3) #Xóa phần tử tại vị trí thứ 3 trong danh sách lst
    print("The list after popping the element at index 3 is",lst) #In danh sách lst sau khi xóa phần tử tại vị trí thứ 3
    lst.pop() #Xóa phần tử cuối cùng trong danh sách lst
    print("The list after popping the last element is",lst) #In danh sách lst sau khi xóa phần tử cuối cùng

#sort
def sortt():
    lst = [5, 2, 9, 1, 5, 6]
    lst.sort() #Sắp xếp danh sách lst theo thứ tự tăng dần = lst.sort(reverse=False)
    # lst = sorted(lst) #Sắp xếp danh sách lst theo thứ tự tăng dần
    print("The sorted list is",lst) #In danh sách lst đã được sắp xếp theo thứ tự tăng dần
    lst.sort(reverse=True) #Sắp xếp danh sách lst theo thứ tự giảm dần
    print("The sorted list in descending order is",lst) #In danh sách lst đã được sắp xếp theo thứ tự giảm dần

#reverse
def reversee():
    lst = [1, 2, 3, 4, 5]
    lst.reverse() #Đảo ngược danh sách lst
    print("The reversed list is",lst) #In danh sách lst đã được đảo ngược

#count
def countt():
    lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    count = lst.count(1) #Đếm số lần xuất hiện của phần tử '1' trong danh sách lst
    print("The count of '1' in the list is",count) #In số lần xuất hiện của phần tử '1' trong danh sách lst

#clear 
def clearr():
    lst = [1, 2, 3, 4, 5]
    lst.clear() #Xóa tất cả các phần tử trong danh sách lst
    print("The list after clearing is",lst) #In danh sách lst sau khi xóa tất cả các phần tử trong danh sách lst

#copy
def copyy():
    lst = [1, 2, 3, 4, 5]
    lst2 = lst.copy() #Sao chép danh sách lst sang danh sách lst2
    print("The copied list is",lst2) #In danh sách lst2 đã được sao chép từ danh sách lst

#extend
def extendd():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    lst1.extend(lst2) #Mở rộng danh sách lst1 bằng cách thêm các phần tử trong danh sách lst2 vào danh sách lst1
    print("The extended list is",lst1) #In danh sách lst1 đã được mở rộng bằng cách thêm các phần tử trong danh sách lst2 vào danh sách lst1
    lst1.extend([7, 8, 9]) #Mở rộng danh sách lst1 bằng cách thêm các phần tử [7, 8, 9] vào danh sách lst1
    print("The extended list is",lst1) #In danh sách lst1 đã được mở rộng bằng cách thêm các phần tử [7, 8, 9] vào danh sách lst1
