# Example of kNN implemented from Scratch in Python

import csv
import random
import math
import operator

def cargarDataset(filename, trainingSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    print(len(dataset))
	    for x in range(len(dataset)-1):
	        for y in range(5):
	            #print(dataset[x][y])
	            if dataset[x][y] == 'A':
	            	dataset[x][y] = 10
	            elif dataset[x][y] == 'B':
	            	dataset[x][y] = 11
	            elif dataset[x][y] == 'C':
	            	dataset[x][y] = 12
	            elif dataset[x][y] == 'D':
	            	dataset[x][y] = 13
	            elif dataset[x][y] == 'E':
	            	dataset[x][y] = 14
	            elif dataset[x][y] == 'F':
	            	dataset[x][y] = 15
	            else:
	            	#print(dataset[x][y])
	            	#print(str(x)+"  "+str(y))
	            	dataset[x][y] = int(dataset[x][y])
			trainingSet.append(dataset[x])

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))#ordena de menor a mayor

	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
		#print("aqui  "+str(distances[x][0]))
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]
	
def datos():
	newInstance = ""
	codHex = []
	while len(newInstance) < 6 or len(newInstance) > 6:
		newInstance = raw_input("\n 	Ingresa tu valor hexadecimal sin espacios\n\n 	: ")
	for x in range(0,6):
		if newInstance[x] == 'a' or newInstance[x] == 'A':
			codHex.append(10)
		elif newInstance[x] == 'b' or newInstance[x] == 'B':
			codHex.append(11)
		elif newInstance[x] == 'c' or newInstance[x] == 'C':
			codHex.append(12)
		elif newInstance[x] == 'd' or newInstance[x] == 'D':
			codHex.append(13)
		elif newInstance[x] == 'e' or newInstance[x] == 'E':
			codHex.append(14)
		elif newInstance[x] == 'f' or newInstance[x] == 'F':
			codHex.append(15)
		else:
			codHex.append(int(newInstance[x]))
	return codHex

def main():
	# prepare data
	trainingSet=[]
	cargarDataset('colors.data', trainingSet)
	#print(trainingSet)
	print 'Data set: ' + repr(len(trainingSet))
	codHex = datos()
	#print(codHex)

	predictions=[]
	k = int(raw_input("\n 	Ingresa el valor k\n\n 	: "))
	neighbors = getNeighbors(trainingSet, codHex, k)
	result = getResponse(neighbors)
	predictions.append(result)
	print('> Es un color=' + repr(result))
	#print(neighbors)
"""
	with open('colors.data', 'ab') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(neighbors)
	"""
main()