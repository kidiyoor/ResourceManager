class Resource:
	def __init__(self, id, name, cpu, mem):
		self.id = id
		self.name = name
		self.cpu = cpu
		self.mem = mem
		self.fcpu = cpu
		self.fmem = mem
		self.processes = []

	def score(self):
		out = self.fcpu/self.cpu * self.fmem/self.mem
		return out

	def allocate(self, process):
		if(self.assignable(process)):
			self.fcpu = self.cpu - process.cpu
			self.fmem = self.mem - process.mem
			self.processes.append(process)
		else:
			print("cant assign") #remove

	def assignable(self, p):
		if p.cpu <= self.fcpu and p.mem <= self.fmem :
			return True
		else:
			return False
