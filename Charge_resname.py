class C_B_R:
	#init class
	def __init__(self, input_filename, output_filename, old_resname, new_resname):
		self.INfilename = input_filename
		self.OUTfilename = output_filename
		self.Nresname = new_resname
		self.Oresname = old_resname
	# for make the pdb file can be indentification of pandans module
	def chag_res(self):
		import re
		OUTf = self.OUTfilename
		fp = open(OUTf, 'w')
		INf = self.INfilename
		for line in open(INf):
			#charge resname
			line = line.strip().replace(self.Oresname, self.Nresname)
			name = re.findall(r"[A-Z]\d{4}", line)
			if len(name) != 0:	
				#get chain and resid
				old_name = re.findall(r"[A-Z]{1}\d{4}", line)[0]
				#new name 
				new_name = re.findall(r"[A-Z]", old_name)[0] + " " + "".join(re.findall(r"\d{1}", old_name)[1:4])
				line = line.replace(old_name, new_name)
			print >> fp, line
		fp.close()
