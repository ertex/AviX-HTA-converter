import xml.etree.ElementTree as ET
print("%Starting Python module....")

#NOTE this is just a slightly modified version of the default script. so most of the things is just commented out with some bodge ontop

root_node = ET.parse("tmp/avix_out.xml").getroot()
#print(root_node)

for child in root_node:
#	print(child.tag)
#	print("\n")
	for child2 in child.findall("children/[@{http://www.w3.org/2001/XMLSchema-instance}type='se.solme.avix.common.data.datamodel:Factory']"):
#		print(child2.attrib)
		print("%your company is named: ", child2.get('i18nName'))
		for child3 in child2:	
			print("%You have the following buidnings", child3.get('i18nName'))
			for child4 in child3:
				print("%  In that building you have the following:", child4.get('i18nName'))
				for bench in child4:
					print("%    Here you have: ", bench.get('i18nName'))
					print("%Assuming this is your workbench...")
					print("%====================================")
					last_task=""
					for task in bench:
						
						if(task.get('i18nName')):
							task_name = task.get('i18nName').strip('\"')
							#if(not last_task):
								#print("\\node [block, name="+ task_name + "] (" + task_name + ") {" +task_name +"};")
							#else:
								#print("\\node [block,right of="+ last_task+ "] ("+task_name+") {"+task_name+"};")
								#print("\\draw [->] ("+last_task+") -- ("+task_name+");")
							last_task =  task_name


						last_subop=""
						for operation in task:      #If a timestudy is used the nName is one level further down
							if(operation.get('i18nName')):
								task_name = operation.get('i18nName').strip('\"')
								#print(operation_name)
								#This level is the same as the folders
	#							print(task_name," , " + operation.get('startTime'), " , " + operation.get('endTime'))
								#if(not last_task):
									#print("\\node [block, name="+task_name+ "] ("+task_name+") {"+task_name+"};")
								#else:
									#print("\\node [block,right of="+ last_task+ "] ("+task_name+") {"+task_name+"};")
									#print("\\draw [->] ("+last_task+") -- ("+task_name+");")
								last_task = task_name



							for subop in operation: #This is a operation in a folder under a workbench
								if(subop.get('i18nName')):
									subop_name = subop.get('i18nName').strip('\"')
									#print(" -- ", subop.get('i18nName'))
									print(subop.get('i18nName'))
									for subsubop in subop: #since the timestudy has mulitple rows the individual rows are new entries and need to be itterated though
										#print(subsubop.attrib)
										if(subsubop.get('startTime')):
											print(-eval(subsubop.get('startTime'))+eval(subsubop.get('endTime')))
									#if(not last_subop):
										#print("\\node [block,below of="+ last_task+"] ("+subop_name+") {"+subop_name+"};")
										#print("\\draw [->] ("+last_task+") -- ("+subop_name+");")
									#else:
										#print("\\node [block,below of="+ last_subop+ "] ("+subop_name+") {"+subop_name+"};")
										#print("\\draw [->] ("+last_subop+") -- ("+subop_name+");")
									last_subop = subop_name
				#Lower levels not implemented but repeat the pattern for more levels
