friends = ["Hail", "JP", "Nan"]
print ("My friends are " +', '.join(str(f) for f in friends[:-1]) + " and " + str(friends[-1]))