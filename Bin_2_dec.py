# Function calculates the decimal equivalent
# to given binary number
def binaryToDecimal(binary):
	
	decimal, i = 0, 0
	while(binary != 0): #1001
		print(binary, "im the binary part")
		dec = binary % 10
		print(dec, "im in the dec part")
		decimal = decimal + dec * pow(2, i)
		print(decimal, "im the decimal part")
		binary = binary//10
		print(binary,"im the binary //10")
		i += 1
	print(decimal)
	

# Driver code

binaryToDecimal(10001)
