import json

def readobj(file):
	f = open(file, 'r')
	data = f.read()
	out = json.loads(data)
	return out
