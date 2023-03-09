## EX-1
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * *

# # x1 = int(input("X =  "))
# #str_ = input("nshan- ")
# x1 = 7
# str_ = "*"
# for i in range(x1 + 1):
#     for j in range(i):           
#         print (str_, end=" ")
#     print()

## EX-2
# * * * * * * * 
# * * * * * * 
# * * * * *   
# * * * *     
# * * *       
# * *         
# *

# # x2 = int(input("X =  "))
# # str_ = input("nshan- ")
# x2 = 7
# str_ = "*"
# for i in range(x2 + 1, 1, -1):
#     for j in range(i - 1):
#         print (str_, end=" ")
#     print()


# EX-3
# *                *
# **              **
# ***            ***
# ****          ****
# *****        *****
# ******      ******
# *******    *******
# ********  ********
# ******************

## x1 =int(input("X =  "))
# str_ = "*"
# for i in range(1, x1 + 1):
#     v =str_ * i + " " * ((x1 - i) * 2) + "*" * i
#     print(v)



## EX-3
#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********

# x1 =int(input("X =  "))
# str_ = "*"
# for i in range(x1+1):
#     print(" " * (x1-i), str_*i)


## EX-4
#  *******
#   ******
#    *****
#     ****
#      ***
#       **
#        *
# x1 =int(input("X =  "))
# str_ = "*"
# for i in range(x1, 0, -1):
#     print(" " * (x1-i),  str_* i)


## EX-4
#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#  * * * * * *         
# * * * * * * *  
# rows = int(input("Введите количество строк: "))

# for i in range(1, rows+1):
#     print(" "*(rows-i), end="")
#     print("* " * i)


## EX-5
# * * * * * * *        
#  * * * * * *         
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       *  
# rows = int(input("Введите количество строк: "))

# for i in range(rows, 0, -1):
#     print(" "*(rows-i), end="")
#     print("* " * i)


## EX-6
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

# s = int(input("Введите количество строк: "))
# str_ = "*"
# for i in range(1, s+1):
#     print((" " * (s - i)) + ("*" * (2*i-1)))
# for i in range(s-1, 0, -1):
#     print((" " * (s - i)) + ("*" * (2*i-1)))



## EX-7
# *        
# **       
# ***      
# ****     
# *****    
# ****     
# ***      
# **       
# * 
# x1 = int(input("Введите количество строк: "))
# str_ = "*"
# for i in range(1,(x1//2) + 1):       
#     print (str_ * i, " " * (x1-i))
# for i in range((x1//2) + 1, 0, -1):       
#     print (str_ * i, " " * (x1-i))







## EX-8
# 0 0 0 9 9 9 
# 0 0 0 9 9 9 
# 0 0 0 9 9 9 
# 4 4 4 5 5 5 
# 4 4 4 5 5 5 
# 4 4 4 5 5 5 



# x=[0]*6
# for i in range(6):
#     x[i]=[0]*6
# for i in range(6):
#     for j in range(3):
#         x[i][j]=0
#     for j in range(3, 6):
#         x[i][j]=9
# for i in range(3,6):
#     for j in range(3):
#         x[i][j]=4
#     for j in range(3, 6):
#         x[i][j]=5
# for i in range (6):
#     for j in range(6):
#         print(x[i][j], end=" ")
#     print()


## EX-9
#   5   5   5   5   5   5 
#   0   5   5   5   5   0 
#   0   0   5   5   0   0
#   0   0   0   0   0   0
#   0   0   0   0   0   0
#   0   0   0   0   0   0
# x=[0]*6
# for i in range(6):
#     x[i]=[0]*6
# for i in range(6//2):
#     for j in range(i, 6-i):
#         x[i][j]=5
# for i in range(6):
#     for j in range(6):
#         print(f"{x[i][j]: 3d}", end=' ')
#     print()


## EX-10

#   6   6   6   6   6   6 
#   5   5   5   5   5   5 
#   4   4   4   4   4   4
#   3   3   3   3   3   3
#   2   2   2   2   2   2
#   1   1   1   1   1   1

# x=[6]*6
# for i in range(6):
#     x[i]=[6]*6
# for i in range(1,6):
#     for j in range(6):
#         x[i][j]=x[0][j]-i
# for i in range(6):
#     for j in range(6):
#         print(f"{x[i][j]: 3d}", end=' ')
#     print()


## EX-11
#   1   1   1   1   1   1 
#   0   1   1   1   1   0 
#   0   0   1   1   0   0
#   0   0   2   2   0   0
#   0   2   2   2   2   0
#   2   2   2   2   2   2

# x=[0]*6
# for i in range(6):
#     x[i]=[0]*6
# for i in range(6//2):
#     for j in range(i, 6-i):
#         x[i][j]=1
# for i in range(6//2,6):
#     for j in range(5-i,i+1):
#         x[i][j]=2
# for i in range(6):
#     for j in range(6):
#         print(f"{x[i][j]: 3d}", end=' ')
#     print()


## EX-12

#   8   8   8   8   8   1 
#   8   8   8   8   1   0 
#   8   8   8   1   0   0
#   8   8   1   0   0   0
#   8   1   0   0   0   0
#   1   0   0   0   0   0

# x=[0]*6
# for i in range(6):
#     x[i]=[0]*6
# for i in range(6):
#     x[i][5-i]=1
# for i in range(6):
#     for j in range(5-i):
#         x[i][j]= 8
# for i in range(6):
#     for j in range(6-i, 6):
#         x[i][j] = 0

# for i in range(6):
#     for j in range(6):
#         print(f"{x[i][j]: 3d}", end=' ')
#     print()



##EX-13
#  4  4  4  4  4  4 
#  4  3  3  3  3  4 
#  4  3  3  3  3  4
#  4  3  3  3  3  4
#  4  3  3  3  3  4
#  4  4  4  4  4  4

# x=[3]*6
# for i in range(6):
#     x[i]=[3]*6
# for i in range(6):
#     x[i][0]=4
#     x[i][5]=4
# for j in range(6):
#     x[0][j]=4
#     x[5][j]=4
# for i in range(6):
#     for j in range(6):
#         print(f"{x[i][j]: 2d}", end=' ')
#     print()
