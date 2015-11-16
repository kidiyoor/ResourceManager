class Process:
	def __init__(self,pid,cpu,mem,st):
		self.pid = pid
		self.cpu = cpu
		self.mem = mem
		self.st = st

	def details(self):
		print('''
--- PROCESS DETAILS ---
pid = %s
cpu = %s	
mem = %s
st = %s
-----------------------
			''')%(self.pid, self.cpu, self.mem, self.st)





