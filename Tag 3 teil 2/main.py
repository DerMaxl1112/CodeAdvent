with open('input.txt') as f:
    lines = f.readlines()

array_0 = [0] * 12
array_1 = [0] * 12

oxygen = [0] * 12
CO2 = [0] * 12

oxygen_atribute = [0] * 12
CO2_atribute = [0] * 12

for line in lines:
    for i in range(12):
        if int(line[i] == "1"):
            array_1[i] += 1
        else:
            array_0[i] += 1

print('0', array_0)
print('1', array_1)


#oxygen
for zaler in range(12):
	oxygen_atribute = array_1[zaler]
	for line2 in lines:
		for i2 in range(12):
			if line2[i2] == oxygen_atribute[i2]:
				oxygen[i2] = line2[i2]
			else:
				oxygen[i2] = None
			
	for line3 in oxygen:
	    for i3 in range(12):
	        if int(line3[i3] == "1"):
	            array_1[i] += 1
 	       else:
    	        array_0[i] += 1
 
	print('1', array_1)
print(oxygen)
		
	

	








#gamma = [0] * 12
#epsilon = [0] * 12

#for line in lines:
#    for i in range(12):
#        if int(line[i] == "1"):
#            array_1[i] += 1
#        else:
#            array_0[i] += 1

#print(array_1)
#print(array_0)

#for i2 in range(12):
#    if array_1[i2] > array_0[i2]:
#        gamma[i2] = 1
#    else:
#        epsilon[i2] = 1

#print("gamma: ", gamma)
#print("epsilon: ", epsilon)

#gamma_word = ""
#for g in gamma:
#    gamma_word += str(g)


#epsilon_word = ""
#for e in epsilon:
#    epsilon_word += str(e)

#gamma_int = int(gamma_word, 2)
#epsilon_int = int(epsilon_word, 2)

#print(gamma_int)
#print(epsilon_int)

#fin = gamma_int * epsilon_int

#print(fin)
    # for char in line:
    #     print(char)
    # print()
    # print(lines_split)


# abc = "100100101011"
# for character in abc:
#     print(character)


# lines_split[1] = int(lines_split[1])
