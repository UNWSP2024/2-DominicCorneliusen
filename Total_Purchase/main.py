#Title: Total Purchase
#Author: Dominic Corneliusen
#Date last Modified: 1/29/26

from ftplib import print_line

#Variables and User interaction
Sales_tax = .07
input("Enter Item name: ")
Item1 = float(input("Enter Item Price:"))
input ("Enter Item Name: ")
Item2 = float(input("Enter Item Price: "))
input ("Enter Item Name: ")
Item3 = float(input("Enter Item Price: "))
input ("Enter Item Name: ")
Item4 = float(input("Enter Item Price: "))
input ("Enter Item Name: ")
Item5 = float(input("Enter Item Price: "))
Subtotal = Item1 + Item2 + Item3 + Item4 + Item5
Sales_tax = Subtotal * Sales_tax
Total = Subtotal - Sales_tax

#Print
print_line(Subtotal)
print_line(Sales_tax)
print_line(Total)