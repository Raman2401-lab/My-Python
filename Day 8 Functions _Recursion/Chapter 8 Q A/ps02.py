' write a program to print the elements of a list in a single line.(list is the parameter)'

heroes = ["thor", "ironman", "spyderman", "batman", "superman"]

def printList(list):
   for i in list:
      print(i, end = " ")

printList(heroes)