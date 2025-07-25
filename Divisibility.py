numn = int(input("Enter a number (Numerator): \n"))
numd = int(input("Enter a number (Denomanator): \n"))

if numn%numd == 0:
    print("The number", numn, "is divisible by", numd)
else:
    print("The number", numn, "is not divisible by", numd)