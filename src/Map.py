import os
import math

class Map(object):
	def __init__(self, mapName, xSize, ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.filename = mapName
		self.fileLocation = "/{}".format(mapName)
		self.mapContents = []


	def LoadMap(self, mapName, location="Default"):
		cwd = os.path.dirname(os.path.realpath(__file__))
		if location == "Default":
			mapFolder = cwd.replace("src","assets")
			mapFolder += "/maps"
		if not os.path.exists(mapFolder):
			print("File Doesn't Exist.")
			quit()
		with open((mapFolder + "/%s"%mapName), "r") as f:
			metadata = f.readline()
			metadata = metadata.split(",")
			self.xSize = metadata[0]
			self.ySize = metadata[1]
			self.filename = metadata[2]


			yLineCounter = 0 
			temporaryMapContents=[]
			for line in f:
				#check to see if the line has as many chars as the meta data suggests
				#no idea why len adds one..oh wait maybe the new line \n
				if (len(line)-1) == int(self.xSize):
					for x in line:
						if x != "\n":
							temporaryMapContents.append(x)
				else:
					print("Problem loading map, line #%i is %i chars not %i."%(yLineCounter,len(line-1),int(self.xSize)))
					quit()
				yLineCounter+=1

			if yLineCounter != int(self.ySize):
				print("Problem loading map, there should be %i map rows, there are %i."%(int(self.ySize), yLineCounter))
			#print(yLineCounter)
			#print(temporaryMapContents)
			self.mapContents=temporaryMapContents




	#check to see if file already exists, ask to overwrite
	def SaveMap(self, location="Default"):
		cwd = os.path.dirname(os.path.realpath(__file__))
		if location == "Default":
			mapFolder = cwd.replace("src","assets")
			mapFolder += "/maps"
		else:
			mapFolder = location
		if not os.path.exists(mapFolder):
			os.makedirs(mapFolder)

		with open(os.path.join(mapFolder,self.filename), "w+") as f:
			#meta data
			f.write("{0.xSize},{0.ySize},{0.filename} \n".format(self))
			
			#blocks
			blockString = ''
			stringCounter = 0
			for index, value in enumerate(self.mapContents):
				blockString += value
				stringCounter+=1 
				if stringCounter==self.xSize:
					f.write(blockString)
					f.write("\n")
					blockString = ''
					stringCounter = 0


	def GenerateSingleBlockMap(self, blocktype):
		for x in range(self.xSize):
			for y in range(self.ySize):
				self.mapContents.append(blocktype)
	
	#TODO fix problem where it changes halfway through mid point
	def GenerateBasicFlatMap(self, sky, ground):
		for x in range(self.xSize):
			blocktype=''
			if x/self.xSize < .5:
				blocktype = sky
			else:
				blocktype= ground
			blocktype = blocktype*self.ySize
			
			for block in blocktype:
				self.mapContents.append(block)

	
#level1 = Map("level1", 4,4)
#level1.GenerateSingleBlockMap("a")
#level1.SaveMap()
#level1.LoadMap("level1")
#print(level1.mapContents)



