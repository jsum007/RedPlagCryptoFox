from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser

# Find out the c++ parser
generator_path, generator_name = utils.find_xml_generator()

# Configure the xml generator
xml_generator_config = parser.xml_generator_configuration_t(
    xml_generator_path=generator_path,
    xml_generator=generator_name)

# The c++ file we want to parse
filename = "sample4.cpp"

decls = parser.parse([filename], xml_generator_config)
global_namespace = declarations.get_global_namespace(decls)
std = global_namespace.namespace("std")
#print(decls)
#print(global_namespace.variables())

class_t_decl = []
for d in global_namespace.declarations:
    if isinstance(d, declarations.class_declaration_t):
        #print(d.name)
        pass
    if isinstance(d, declarations.class_t) and d.parent == global_namespace:
        #class_t_decl.append(d.class_type)
        #print('hhh', d.class_type)
        pass
    if isinstance(d, declarations.free_function_t):
        free_function_t_decl = d
        print(d.name)


# The variables() method will return a list of variables.
# We know that the c variable is the third one in the list:
'''c = ns.variables()[2]
print("My name is: " + c.name)
print("My type is: " + str(c.decl_type))
print("My value is: " + c.value)'''
print('ggggggggggggggggggggggggggggggg')
# Of course you can also loop over the list and look for the right name
main = global_namespace.free_function(name="main")


# Print all base and derived class names
for class_ in global_namespace.classes():
	if class_.class_type == 'class' and class_.parent == global_namespace:
	    print('class "%s" hierarchy information:' % class_.name)
	    print('\tbase classes   : ', repr([
	        base.related_class.name for base in class_.bases]))
	    print('\tderived classes: ', repr([
	        derive.related_class.name for derive in class_.derived]))
	    print('\tconstructors: ', repr([
	        p.decl_string for p in class_.constructors()]))
	    print('\toperators: ', repr([
	        p.name for p in class_.operators()]))
	    print('\tvariables: ', repr([
	        str(p.decl_type) for p in class_.variables()]))
	    print('\tfunctions: ', [
	        str(p) for p in class_.member_functions(allow_empty = True)])
	    
print('ggggggggggggggggggggggggggg\n')

'''
for var in global_namespace.variables():
    #if var.name == "c":
    print("My name is: " + var.name)
    print("My type is: " + str(var.decl_type))
    if var.value is not None:
    	print("My value is: " + var.value)

'''

'''criteria = declarations.variable_matcher()
var_a2 = declarations.matcher.find(criteria, global_namespace)
for n in var_a2:
	if n.parent in class_t_decl:
		print(n.parent)'''


# One way to get a variable is to use the variable() method and
# a lambda function. This is the most flexible way as you can implement
# your own lambda function to filter out variables following your
# specific criteria.
'''c = ns.variable(lambda v: v.name == "c")
print("My name is: " + c.name)
print("My type is: " + str(c.decl_type))
print("My value is: " + c.value)'''