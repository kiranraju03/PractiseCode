class SoccerPlayers:

    def __init__(self,health,salary):
        self.health = health
        self.salary = salary
        #these attributes will be added to the instance when created

    def foul(self, player): #when foul method is called, self points to ronal instance and player is beck, as it is sent as a arg.
        player.health = 0
        self.salary = self.salary + 10 ** 6

ronal = SoccerPlayers(100, 10 ** 7)
beck = SoccerPlayers(100, 10 ** 6)

ronal.foul(beck) #self points to ronal

print(beck.health)
print(ronal.health)

SoccerPlayers.foul(beck, ronal) # when class name is used instead of the instance, then the arguments sent to the
                                # function needs to explicity
                                # provided, i.e., self = beck, player = ronal

print(beck.health)
print(ronal.health)

print(beck.salary)
print(ronal.salary)

#the first argument of the methods in the class is referening to the instance that calls it.