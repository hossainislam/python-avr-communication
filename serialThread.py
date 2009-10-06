#! usr/bin/python

from threading import Thread
from Queue import Queue

outgoing = Queue()
incoming = Queue()

class serialThread(Thread):

	serialInterface = None

	def __init__(self, serialInterfaceInstance):
		if serialInterfaceInstance is None:
			print 'Error - must be passed a serial interface.'
			return
		else:
			Thread.__init__(self)
			self.serialInterface = serialInterfaceInstance

	def run(self):
		while True:
			while outgoing.empty() is False:
				self.serialInterface.write(outgoing.get())
			while self.serialInterface.inWaiting() is not 0:
				incoming.put(self.serialInterface.read(1))

