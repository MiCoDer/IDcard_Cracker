import string

#===Function modified by http://mrcjtech.blogspot.com/2017/09/python.html===
locationCode = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33};

def check(id):
	if(len(id) != 10 or not(id[0].isalpha()) or not(id[1:].isdigit() or int[id[1] > 2 or id[1] < 1])):
        	print('Error: wrong format')
    # Convert 1st Alphabet to Numeric code
	encodeID = list(str(locationCode[id[0].upper()]))
	encodeID.extend(list(id[1:]))
	checkSum = int(encodeID[0])

    # Calculate the checksum of ID
	para = 9
	for n in encodeID[1:]:
		if para == 0:
			para = 1
		checkSum += int(n)*para
		para -= 1

    # Check the checksum
	if checkSum % 10 == 0:
		return True
	else:
		return False
#===Mico===
ID=input("輸入身份證(A123??6789):")
for i in range(0,100):
	tmpID=""
	tmpID=ID.replace("??",str(i).zfill(2))
	if(check(tmpID)):	
		print(tmpID)
