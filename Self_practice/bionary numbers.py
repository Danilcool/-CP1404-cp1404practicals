denary = int(input("Enter a number between 0 and 255"))

binary = ""
starting = 128

for i in range(8):
    if denary >= starting:
        binary = binary + "1"
        denary = denary - starting
        starting /= 2
    else:
        binary = binary + "0"
        starting /= 2


#... Complete the code here...

print(binary)
