# - *- coding: utf- 8 - *-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man, dat OK!\n"

print "We can hardcode!"
cheese_and_crackers(20, 30)

print "Or we can do it right..."
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "Oh, we could even be math geeks!"
cheese_and_crackers(10 + 20, 5 + 6)

print "А теперь давим оба окурка вместе!"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



