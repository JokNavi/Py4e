input_string = 'X-DSPAM-Confidence: 0.8475 '
colon_index = input_string.find(':')+1
number2 = float(input_string[colon_index:])
print(number2)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])