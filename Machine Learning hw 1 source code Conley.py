print("Problem 1:")
#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
###
#Sort the list and find the min and max age
ages.sort()
print(ages)
print(max(ages))
print(min(ages))
###
#Add the min age and the max age again to the list
ages.insert(0, 19)
ages.insert(11, 26)
print(ages)
###
#Find the median age (one middle item or two middle items divided by two)
print((ages[6]-ages[5])/2+ages[5])
###
#Find the average age (sum of all items divided by their number)
print(sum(ages)/len(ages))
###
#Find the range of the ages (max minus min)
print(ages[11]-ages[0])
######
######
print("Problem 2:")
###
#Create an empty dictionary called dog
dog = {}
print(dog)
###
#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = '1'
dog['color'] = '2'
dog['breed'] = '3'
dog['legs'] = '4'
dog['age'] = '5'
print(dog)
###
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'a'
student['last_name'] = 'b'
student['gender'] = 'c'
student['age'] = 'd'
student['marital_status'] = 'e'
student['skills'] = ['f','g']
student['country'] = 'h'
student['city'] = 'i'
student['address'] = 'j'
print(student)
###
#Get the length of the student dictionary
print(len(student))
###
#Get the value of skills and check the data type, it should be a list
print(type(student['skills']))
###
#Modify the skills values by adding one or two skills
student['skills'].append('f1')
student['skills'].append('g1')
print(student['skills'])
###
#Get the dictionary keys as a list
print(student.keys())
###
#Get the dictionary values as a list
print(student.values())
######
######
print("Problem 3:")
###
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Robby", "Imajinari")
print(brothers)
sisters = ("Feika", "Nahtreel")
print(sisters)
###
#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
###
#How many siblings do you have?
print(len(siblings))
###
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Steve", "Jenny")
print(family_members)
######
######
print("Problem 4:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
###
#Find the length of the set it_companies
print(len(it_companies))
###
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
###
#Insert multiple IT companies at once to the set it_companies
it_companies.add("YouTube")
it_companies.add("Nintendo")
print(it_companies)
###
#Remove one of the companies from the set it_companies
it_companies.remove("Facebook")
print(it_companies)
###
#What is the difference between remove and discard
print("Remove can cause a KeyError exception, while Discard does not.")
###
#Join A and B
C = A | B
print(C)
###
#Find A intersection B
D = A & B
print(D)
###
#Is A subset of B
print("Subset? Yes, all A's values are part of B.")
###
#Are A and B disjoint sets
print("Disjoint? No, they contain shared values.")
###
#Join A with B and B with A
E = A | B
F = B | A
print(E)
print(F)
###
#What is the symmetric difference between A and B
G = B - A
print(G)
###
#Delete the sets completely
A.clear()
B.clear()
print(A)
print(B)
###
#Convert the ages to a set and compare the length of the list and the set.
ageset = set(age)
print(len(age))
print(len(ageset))
######
######
print("Problem 5:")
#The radius of a circle is 30 meters.
###
#Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
area_of_circle = 3.141592 * 30 * 30
print(area_of_circle)
###
#Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
circum_of_circle = 2 * 3.141592 * 30
print(circum_of_circle)
###
#Take radius as user input and calculate the area.
dummy = float(input("Enter radius: "))
print(3.141592 * dummy * dummy)
######
######
print("Problem 6:")
#“I am a teacher and I love to inspire and teach people”
#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
quote = "I am a teacher and I love to inspire and teach people"
words = quote.split()
unique = set(words)
print(len(unique))
print(unique)
######
######
print("Problem 7:")
#Use a tab escape sequence to get the following lines.
#Name Age Country City
#Asabeneh 250 Finland Helsinki
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
######
######
print("Problem 8:")
#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
#“The area of a circle with radius 10 is 314 meters square.”
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))
######
######
print("Problem 9:")
#Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop. N: No of students (Read input from user)
#Ex: L1: [150, 155, 145, 148]
#Output: [68.03, 70.3, 65.77, 67.13]
N = float(input("Enter number of students: "))
N1 = 1
weights = []
while N1 <= N:
    N2 = float(input("Enter student "+str(N1)+"'s weight: "))
    N3 = N2 * 0.45359237
    weights.insert(N1, N3)
    N1 += 1
print(weights)
######
######
print("Problem 10:")
#The diagram below shows a dataset with 2 classes and 8 data points, each with only one feature value, labeled f. Note that there are two data points with the same feature value of 6. These are shown as two x’s one above the other. 
###
#1. Divide this data equally into two parts. Use first part as training and second part as testing. Using KNN classifier, for K=3, what would be the predicted outputs for the test samples? Show how you arrived at your answer. 
print("Training: 1o, 2o, 3x, 6x\nTesting: 6x, 7o, 10o, 11o")
print("Predicted test outputs would be 8 and 9; the former is directly between 6 and 10 and the latter between 7 and 11, the far points for each of the two possible k=3 midpoints. Both would be o points rather than x points.")
###
#2. Compute the confusion matrix for this and calculate accuracy, sensitivity and specificity values.
print("TN: 1\tFP: 0\nFN: 0\tTP: 5\nAccuracy: 1\nSensitivity: 1\nSpecificity: 1")