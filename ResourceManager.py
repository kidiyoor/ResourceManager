import time
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
	n = random.randint(0, nTypes-1) #random number to select type of process
	cpu = PTYPE['type'][n]["cpu"]
	mem = PTYPE['type'][n]["mem"]
	WAITINGQ.append(Process(pid, cpu, mem, st))



def startService():
	#loop till WAINTINGQ is empty
	#remove expired process
	for j in range(len(WAITINGQ)):
		details()
		WAITINGQ[j].details()
		sresource = selectResource(WAITINGQ[j])
		if(sresource != -1):
			RESOURCES[sresource].allocate(WAITINGQ[j])
		else:
			print("skip")
		ACTIVEQ.append(WAITINGQ[j])
		time.sleep(4)





#returns -1 if resource not available or the resource number to which process need to be assigned
def selectResource(process):
	candidates = []
	for i in range(len(RESOURCES)):
		if (RESOURCES[i].assignable(process)):
			candidates.append([RESOURCES[i],i])

	if len(candidates) == 0:
		print("no candidates resources")

	maxscore = 0
	out = -1

	for i in range(len(candidates)):
		if candidates[i][0].score() > maxscore :
			maxscore = candidates[i][0].score()
			out = candidates[i][1]
	print("Selected : " + str(out))
	return out


def details():
	print("--- CLUSTER STATUS ---")
	s = 'NAME :\t'
	
	for i in RESOURCES:
		s = s + i.name + '\t\t'
	print(s + '\n')
	
	s = 'FCPU :\t'
	for i in RESOURCES:
		s = s + str(i.fcpu) + '\t\t'
	print(s + '\n')
	
	s ='FMEM :\t'
	for i in RESOURCES:
		s = s + str(i.fmem) + '\t\t'
	print(s + '\n')

	print("-----------------")