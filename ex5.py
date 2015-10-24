name = 'Ivan'
age = 30 #true
height = 175 #cm
weight = 80 #kg, not exactly true
eyes = 'Grey' #or blue, depends
teeth = 'White' #mostly
hair = 'Blonde' #was someday... eh.

print "Let's talk about %s." % name
print "He's %r cm tall." % height
print "He's %d kg heavy." % weight
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)
