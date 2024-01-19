#cyclic redundancy check
#method to perform XOR
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


crc8="10000111"
crc10="11000110101"
crc16="10001000000100001"
crc32="100000100110000010001110110110111"

data =""
data=input("Enter the data:")
print('''Choice 1  : Crc8 (10000111)\nChoice 2  : Crc10 (11000110101)\nChoice 3  : Crc16 (10001000000100001)\nChoice 4  : Crc32 (100000100110000010001110110110111)\n
      ------------------------------''')
#selcting the crc from the sender
choice = int(input("Enter the genrator polynomial from the choices above: "))
key=""
if choice==1:
    key=crc8
elif choice==2:
    key=crc10
elif choice==3:
    key=crc16
elif choice==4:
    key=crc32
else:
    print("enter a valid choice between 1 to 4")
    

length=len(key)
append_data=data + '0'*(length-1)
temp=append_data[0:length]
while length<len(append_data):
    if temp[0]=='1':
        temp=xor(key,temp)+append_data[length]
    else:
        temp=xor('0'*length,temp)+append_data[length]
    length+=1
if temp[0]=='1':
    temp=xor(key,temp)
else:
    temp=xor("0"*length,temp)
remainder=temp
codeword = data+remainder
print("Remainder : ", remainder)
print("Transmited data (data + crc):", codeword)

#verification
recieverdata=input("Enter recived data:")
lenrec=len(recieverdata)

lenrec=len(key)
temp=recieverdata[0:lenrec]
while lenrec<len(recieverdata):
    if temp[0]=='1':
        temp=xor(key,temp)+recieverdata[lenrec]
    else:
        temp=xor('0'*lenrec,temp)+recieverdata[lenrec]
    lenrec+=1
if temp[0]=='1':
    temp=xor(key,temp)
else:
    temp=xor("0"*lenrec,temp)
remainder=temp

print("reminder after verification",remainder)
for i in range(0,len(remainder)):
    if remainder[i]=='1':
        print("data does not match, error in communication")
        break
else:
    print("no error")
        





