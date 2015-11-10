#!/usr/bin/python

# my version of this:
# https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
# I chose bicycles:
# https://docs.oracle.com/javase/tutorial/java/concepts/object.html

class Bicycle(object):
    '''
    A bicycle has the following attributes:

    chainring_teeth: a list of integers representing the number of teeth on the chainring
    cog_teeth: a list of integers representing the number of teeth on the cog
    tire_size: the size of the bike tire in inches or millimeters
    tire_units: a string either 'mm' or 'in'
    '''

    def __init__(self, name, chainring_teeth=[44], cog_teeth=[16], tire_size=700, tire_units='mm'):
        self.name = name
        self.chainring_teeth = chainring_teeth
        self.cog_teeth = cog_teeth
        self.tire_size = tire_size
        self.tire_units = tire_units

    def __repr__(self):
        return('name:{}\nchainrings:{}\ncogs:{}\nsize:{}\nunits:{}'.\
                   format(self.name, self.chainring_teeth, self.cog_teeth, self.tire_size, self.tire_units))

    def biggest_gear_ratio(self):
        return(float(max(self.chainring_teeth))/float(min(self.cog_teeth)))

    def smallest_gear_ratio(self):
        return(float(min(self.chainring_teeth))/float(max(self.cog_teeth)))

    def speedness(self):
        return(len(self.chainring_teeth) * len(self.cog_teeth))

    def gears_by_ratio(self):
        ratios = []
        for front in self.chainring_teeth:
            for back in self.cog_teeth:
                ratios.append(((float(front)/float(back)), front, back))
        ratios.sort(reverse=True)
        return(ratios)

    def gears_by_index(self):
        index = 0
        ratios = []
        for front in self.chainring_teeth:
            for back in self.cog_teeth:
                index += 1
                ratios.append((index, (float(front)/float(back)), front, back))
        ratios.sort()
        return(ratios)

if '__main__' == __name__:
    bikes = [Bicycle('fixie'), Bicycle('my bike', chainring_teeth=[52,42], cog_teeth=[13,15,17,19,21,23])]
    for bike in bikes:
        print(bike)
        print('biggest gear ratio:{}'.format(bike.biggest_gear_ratio()))
        print('smallest gear ratio:{}'.format(bike.smallest_gear_ratio()))
        print('{} is a {}-speed bike'.format(bike.name, bike.speedness()))
        print('gear ratios')
        for (ratio, chainring, cog) in bike.gears_by_ratio():
            print('{} {} {:.2f}'.format(chainring, cog, ratio))
        print('gears by index')
        for (index, ratio, chainring, cog) in bike.gears_by_index():
            print('{:2d} {} {} {:.2f}'.format(index, chainring, cog, ratio))
        print('\n') # make room!
