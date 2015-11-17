import time
from Resource import *
from Process import *
import random

PID = 1
WAITINGQ = []
RESOURCES = []
ACTIVEQ = []
TIME = 0

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
	serviceTime = 40 #TODO # from random exonential distribution
	nTypes = len(PTYPE['type'])
	n = random.randint(0, nTypes-1) #TODO#random number to select type of process
	cpu = PTYPE['type'][0]["cpu"]
	mem = PTYPE['type'][0]["mem"]
	WAITINGQ.append(Process(pid, cpu, mem, serviceTime))



def startService():
	global TIME
	global RESOURCES
	global WAITINGQ

	j=0
	while(len(WAITINGQ)!=0 and j < len(WAITINGQ)):
	#for j in range(len(WAITINGQ)):
		print("-----------------------------------------------------------------------------")
		print("TIME : " + str(TIME))
		TIME = TIME + 1
		#remove process after service time
		for i in range(len(RESOURCES)):
			#update running time of processes
			RESOURCES[i].update()
			#remove dead processes
			RESOURCES[i].flush()
			

		#prints details of cluster
		details()
		#prints details of process
		WAITINGQ[j].details()
		#select resource to allocate this process
		sresource = selectResource(WAITINGQ[j])
		if(sresource != -1):
			RESOURCES[sresource].allocate(copyProcess(WAITINGQ[j]))
			#remove process from WAITINGQ
			WAITINGQ = WAITINGQ[:j] + WAITINGQ[(j+1):]			
			
			#to give priotity to already waiting process
			if j!=0:
				j=0
		else:
			print("Skip")
			#to give priotity to already waiting process
			j=j+1

		print("No of procces in waiting Queue : " + str(len(WAITINGQ)))
		print("-----------------------------------------------------------------------------")





#returns -1 if resource not available or the resource number to which process need to be assigned
def selectResource(process):
	global RESOURCES

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


def copyProcess(p):
	out = Process(p.pid, p.cpu, p.mem, p.serviceTime)
	out.runningTime = p.runningTime
	out.serviceTime = p.serviceTime
	out.waitingTime = p.waitingTime

	return out 


def details():
	global RESOURCES

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

	s ='SCORE :\t'
	for i in RESOURCES:
		s = s + str(i.score()) + '\t\t'
	print(s + '\n')

	print("-----------------")
