'''
Message.py

Author: Keith Chester

Version: 0.1
Date modified: September 23, 2009

This is the Message class. More to come.
I am assuming pyserial was imported already.
'''

import random

class Message:
	#The serial interface this message belongs to
	serialInterface = None

	#The identifier, the most important part, is
	#the understood overall meaning of each
	#individual message. DO NOT use id, as it is
	#a key word.
	identifier = None

	#Data for messages
	dataOut = None
	dataReceived = None

	#Variables that control parsing
	size = 0 #Total size in bytes, to be calculated
	isOutgoing = True #One of two. Default out, so True
	sizeOut = 0 #Total outgoing bytes
	sizeIn = 0 #Total incoming bytes

	def __init__(self, serialInterfaceInstance, identifierInstance, directionInstance = True):
		#get an identifier check here to make sure
		#it exists. until then, placeholder.
		self.serialInterface = serialInterfaceInstance
		self.identifier = identifierInstance
		self.direction = directionInstance

	def process(self):
		'''
			This function, when called, will read the number of bytes
			requested, and process the information as needed. Result
			is returned to write/read.
			This is very basic on a generic Message object - it will
			just return what it reads.
			This is where other messages will see their biggest
			difference.
		'''
		return

	def make(self, messageOut, messageIn = None):
		'''
Here we place the incoming list of messages, figure out their size, etc. All work
done here.
		'''
		#make it create ranges too.
		self.size = self.data.count #Save message size

	def transmit(self):
		syncCheck = self.sync()
		if syncCheck is False:
			print "Could not sync with device."
			return False
		else:
			self.identify()
			self.write(self.sizeOut)
			self.write(self.dataOut)
			self.dataReceived = self.process() #Process the incoming data.
			if self.isOutgoing is False:
				return self.dataReceived
			else:
				return True

	def sync(self):
		random.seed()
		syncStart = random.randint(6, 127) #Get the value the sync will work with.
		syncReturn = 2 * syncStart - 12 #Calculate the result we should be getting back

		self.write(syncStart) #send the start bit

		tmp = syncReturn - 1
		syncAttemptCounter = 0 #NOTE : One wrong attempt should fail...
		while tmp is not syncReturn or syncAttemptCounter is not 3:
			try:
				tmp = self.read(1)
			except:
				print "Handshake sync failed. Trying again."
				syncAttemptCounter += 1

		if syncAttemptCounter is 3:
			return False
		elif tmp is syncReturn:
			return True

	def identify(self):
		self.write(self.identifier)

	def write(self, outgoingData):
		'''
			return a list of characters, byte by byte,
			that is compatible with character printing.
		'''

	def read(self):
		'''
			Not quite sure if there is anything new that
			needs to be done here...
		'''

	def print(self):
		print "Raw message data"
		print "Function incomplete :-("
