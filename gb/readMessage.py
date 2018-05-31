from parseMessage import parseMessage
from boto.sqs.message import Message

""" Method for reading the queue and passing on the object of one message """
def nextMessage(queue):
	try:
		# read the first entry in the queue and take the string from the body
		message = queue.read(1)
		messageBody = message.get_body()

		# Parse the string from the body
		messageToReturn = parseMessage(messageBody)

		# Delete the message from the queue and return the parsed object
		queue.delete_message(message)
		return messageToReturn

	except AttributeError:
		print "No messages in queue"
