import ResourceManager

class Resource:
	def __init__(self, idn, name, cpu, mem):
		self.id = idn
		self.name = name
		self.cpu = cpu
		self.mem = mem
		self.fcpu = cpu
		self.fmem = mem
		self.processes = []

	def score(self):
		out = float(self.fcpu)/self.cpu * float(self.fmem)/self.mem
		return out

	def allocate(self, p):
		if(self.assignable(p)):
			self.fcpu = self.fcpu - p.cpu
			self.fmem = self.fmem - p.mem
			self.processes.append(p)
		else:
			print("cant assign") #remove

	def assignable(self, p):
		if p.cpu <= self.fcpu and p.mem <= self.fmem :
			return True
		else:
			return False

	def update(self):
		for i in range(len(self.processes)):
			self.processes[i].runningTime = self.processes[i].runningTime + 1

	def flush(self):
		'''		i = 0
		for p in self.processes:
			#print("rt : " + str(self.processes[i].runningTime) + "	st : " + str(self.processes[i].serviceTime) )
			if self.processes[i].runningTime >= self.processes[i].serviceTime :
				temp = self.processes[i]
				self.processes = self.processes[:i] + self.processes[(i+1):]
				self.fcpu = self.fcpu + temp.cpu
				self.fmem = self.fmem + temp.mem
			else:
				i = i + 1
		'''
		t = []
		for i in range(len(self.processes)):
			if self.processes[i].runningTime >= self.processes[i].serviceTime :
				temp = self.processes[i]
				t.append(self.processes[i])
				self.fcpu = self.fcpu + temp.cpu
				self.fmem = self.fmem + temp.mem
		
		for i in range(len(t)):
			self.processes.remove(t[i])
