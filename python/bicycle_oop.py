#!/usr/bin/python

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

fixed_gear_bike = Bicycle('fixie')
print(fixed_gear_bike)
print(fixed_gear_bike.biggest_gear_ratio())
print(fixed_gear_bike.smallest_gear_ratio())
print('{} is a {}-speed bike'.format(fixed_gear_bike.name, fixed_gear_bike.speedness()))

dj_bike = Bicycle('my bike', chainring_teeth=[52,42], cog_teeth=[13,15,17,19,21,23])
print(dj_bike)
print(dj_bike.biggest_gear_ratio())
print(dj_bike.smallest_gear_ratio())
print('{} is a {}-speed bike'.format(dj_bike.name, dj_bike.speedness()))
