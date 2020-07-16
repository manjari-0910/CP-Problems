# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch
# of fabric requires purchasing 1 entire yard. With this in mind,
# write the function fabricYards(inches) that takes the number of
# inches of fabric desired, and returns the smallest number of whole
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of
# inches of fabric desired and returns the number of inches of excess
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!


def fun_fabricyards(inches):
	# your code goes here
	q=inches//36
	r=inches%36
	if r==0:
		return q
	else:
		return q+1


def fun_fabricexcess(inches):
	# your code goes here
	q=inches//36
	r=inches%36
	if r==0:
		return 0
	else:
		return 36-r
	return 1


