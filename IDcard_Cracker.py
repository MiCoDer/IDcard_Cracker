import string

#===Auth function by http://mrcjtech.blogspot.com/2017/09/python.html===
# create alphabet for 1st char of ID
alphabet = list(string.ascii_uppercase[0:8])
alphabet.extend(list(string.ascii_uppercase[9:]))
code = list(range(10,33))

# create the location mapping code for char of ID
locationCode = dict(zip(alphabet,code))

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
