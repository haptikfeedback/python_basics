# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.
def num_teachers(teachers):
    count = 0
    for d in teachers.keys():
        count = count+1
    return(count)

def num_courses(teachers):
    courses = 0
    for key, value in teachers.items():
    	courses += len(list(value))
    return(courses)

def courses(teachers):
    list_courses = []
    for value in teachers.values():
        for val in value:
        	list_courses.append(val)
    return(list_courses)

def most_courses(teachers):
    maxcourse = 0
    maxname   = ''

    for name in teachers.keys():
        if maxcourse < len(teachers[name]): 
            maxcourse = len(teachers[name])
            maxname = name
        else:
            continue
    return maxname 

def stats(teachers):
    lista = []
    for key in teachers:
        course = [key, len(teachers[key])]
        lista.append(course)
    return lista
