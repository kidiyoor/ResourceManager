from Resource import *
from Process import *
import random

PID = 1
WAITINGQ = []
RESOURCES = []
ACTIVEQ = []

PTYPE = {
	"type" : 
		[
		{
			"cpu" : 1,
			"mem" : 2
		},
		{
			"cpu" : 2,
			"mem" : 2
		},
		{
			"cpu" : 2,
			"mem" : 4
		},
		{
			"cpu" : 4,
			"mem" : 4
		}
		]
}

def createCluster(res):
	global RESOURCES
	RESOURCES = []
	for r in res['resources']:
		RESOURCES.append(Resource(r['id'],r['name'],r['cpu'],r['mem']))


def newProcess():
	global PID
	pid = PID
	PID = PID + 1
	st = 5 # from random exonential distribution
	nTypes = len(PTYPE['type'])
	n = random.randomint(1, nTypes) #random number to select type of process
	cpu = PTYPE['type'][n]["cpu"]
	mem = PTYPE['type'][n]["mem"]
	WAITINGQ.append(Process(pid, cpu, mem, st))



def status():
	pass

def startService():
	#loop till WAINTINGQ is empty
	#remove expired process
	for i in range(len(WAITINGQ)):
		WAITINGQ[i].details()
		sresource = selectResource(WAITINGQ[i])
		RESOURCES[sresource].allocate(WAITINGQ[i])
		ACTIVEQ.append(WAITINGQ[i])




#returns -1 if resource not available or the resource number to which process need to be assigned
def selectResource(process):
	candidates = []
	for i in range(len(RESOURCES)):
		if (RESOURCES[i].assignable(process)):
			candidates.append(RESOURCES[i])

	maxscore = 0
	out = -1

	for i in range(len(RESOURCES)):
		if RESOURCES[i].score() > maxscore :
			maxscore = RESOURCES[i].score
			out = i
	return out