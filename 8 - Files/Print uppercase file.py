total = 0
count = 0
finput = input('Enter the file name: ')
try:
    f = open(finput)
except:
    if finput == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    else:
        print('File cannot be opened: '+finput)
else:
    for line in f:
        if line.startswith('X-DSPAM-Confidence:'):
            start_index = line.find(':')+1
            total = total + float(line[start_index:])
            count = count + 1
    average = total/count
    print("Average spam confidence: " + str(average))