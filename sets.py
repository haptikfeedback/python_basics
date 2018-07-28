def covers(args): 
    result = [] 
    for key, value in COURSES.items(): 
        if args.intersection(value): 
            result.append(key) 
    return result

def covers_all(args):
	new_list = [] 
    for key, value in COURSES.items(): 
		if args & COURSES[key] == args: 
			new_list.append(key) 
    return new_list
    

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

