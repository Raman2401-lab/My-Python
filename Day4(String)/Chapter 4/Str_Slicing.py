# string slicing

name = "Raman"

#  String indexing: 
#       R   a   m   a   n
#       0   1   2   3   4


print(name[0:3])   # Ram (Start index = 0,End index = 3 (excluded) )
print(name[1])     # a   (index = 1)

print(name[1:])    # aman (Start index = 1,End index = till last )
print(name[:3])    # Ram  (Start index = from begining ,End index = 3 )

print(name[::-1])  # namaR   (Revers)

print(name[-1])    # n
print(name[-3])    # m
print(name[-5])    # R

print(name[-4:-1]) # ama
print(name[1:4])   # ama