import ResourceManager
import Process
import json
import common

if __name__ == "__main__":
	r = common.readobj("resources.json")
	nresources = len(r['resources'])

	ResourceManager.createCluster(r)

	print("Enter number of process")
	n = int(raw_input())
	for i in range(n):
		ResourceManager.newProcess()
	
	ResourceManager.startService()

	

