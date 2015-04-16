name = input("Class name : ").capitalize()
nb_var = int(input("Number of variables : "))
var = []
for i in range(0, nb_var) :
	tmp = {}
	print("var #", i + 1)
	tmp["type"] = input("type : ")
	tmp["name"] = input("name : ")
	tmp["vis"] = int(input("visiblity (1: public, 2: protected, 3: private) : "))
	tmp["vname"] = tmp["name"]
	tmp["set"] = False;
	if tmp["vis"] == 2 or tmp["vis"] == 3:
		tmp["vname"] = '_' + tmp["name"]
		tmp["set"] = (input("setter (y/n) ? ") == "y")
	tmp["default"] = input("default value : ")
	var.append(tmp)

cpp_name = name + ".cpp"
hpp_name = name + ".hpp"

# CPP

cpp = open(cpp_name, "w+")

#include hpp
cpp.write('#include "' + hpp_name + '"\n\n')
#default constructor
cpp.write(name + '::' + name + '(void){\n')
if nb_var > 0 :
	for v in var :
		cpp.write("\tthis->" + v["vname"] + " = " + v["default"] + ";\n")
cpp.write('}\n\n')
#destructor
cpp.write(name + '::~' + name + '(void){\n')
cpp.write('}\n\n')
#copy constructor
cpp.write(name + '::' + name + '(' + name + ' const & src){\n')
cpp.write('\t*this = src;\n')
cpp.write('}\n\n')
#assignment operator
cpp.write(name + ' &\t' + name + '::operator=(' + name + ' const & src){\n')
if nb_var > 0 :
	cpp.write('\tif(this != *src) {\n')
	for v in var :
		if v["vis"] == 2 or v["vis"] == 3:
			cpp.write("\t\tthis->" + v["vname"] + " = src.get" + v["name"].capitalize() + "();\n")
		else :
			cpp.write("\t\tthis->" + v["vname"] + " = src." + v["vname"] + ";\n")
	cpp.write('\t}\n')
cpp.write('\treturn *this;\n')
cpp.write('}\n\n')
if nb_var > 0 :
	for v in var :
		if v["vis"] == 2 or v["vis"] == 3:
			cpp.write(v["type"] + "\tget" + v["name"].capitalize() + "(void) const {\n")
			cpp.write('\treturn this->' + v["vname"] + ';\n')
			cpp.write('}\n\n')
			if v["set"]:
				cpp.write("void\tset" + v["name"].capitalize() + "(" + v["type"] + " val){\n")
				cpp.write('\tthis->' + v["vname"] + ' = val;\n')
				cpp.write('}\n\n')

# HPP

hpp = open(hpp_name, "w+")

#protection
hpp.write('#ifndef ' + name.upper() + '_HPP\n')
hpp.write('# define ' + name.upper() + '_HPP\n\n')
#class
hpp.write('class ' + name + ' {\n')
#public
hpp.write('\tpublic:\n')
hpp.write('\t\t' + name + '(void);\n')
hpp.write('\t\t~' + name + '(void);\n')
hpp.write('\t\t' + name + '(' + name + ' const & src);\n')
hpp.write('\t\t' + name + ' &\toperator=(' + name + ' const & src);\n')
if nb_var > 0 :
	for v in var :
		if v["vis"] == 2 or v["vis"] == 3:
			hpp.write('\t\t' + v["type"] + "\tget" + v["name"].capitalize() + "(void) const;\n")
			if v["set"]:
				hpp.write('\t\t' + "void\tset" + v["name"].capitalize() + "(" + v["type"] + " val);\n")
if nb_var > 0 :
	for v in var :
		if v["vis"] == 1 :
			hpp.write("\t\t" + v["type"] + "\t" + v["vname"] + ";\n")
#private
hpp.write('\tprivate:\n')
if nb_var > 0 :
	for v in var :
		if v["vis"] == 3 :
			hpp.write("\t\t" + v["type"] + "\t" + v["vname"] + ";\n")
hpp.write('\n')
#protected
hpp.write('\tprotected:\n')
if nb_var > 0 :
	for v in var :
		if v["vis"] == 2 :
			hpp.write("\t\t" + v["type"] + "\t" + v["vname"] + ";\n")
hpp.write('\n')
#!class
hpp.write('};\n')
#!protection
hpp.write('\n#endif\n')


#close docs
cpp.close()
hpp.close()
