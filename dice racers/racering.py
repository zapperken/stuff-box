# default stat parameters
MAX_HEALTH = 10
DEF_SPEED  = 6
RACE_LAPS  = 2

# display constants
RACER_W_CARD  = "%6s (HP:%2d | MV:1/%d) Laps: %d/%d [%s]"
RACER_NO_CARD = "%6s (HP:%2d | MV:1/%d) Laps: %d/%d"
RECEIVE_CARD  = "  ! %s got %s !"
TRAPPED       = "  > %s %s %s! (%s-%d) <"
ATTACKED      = "  %s got hit by %s's %s"
SUPPORT       = "  %s increased its %s by using %s"
BLESSING      = "  {0} has additional move of {1} blocks"

import random 

# # # # # # # # # # # # #
# # #  Racer class  # # #
# # # # # # # # # # # # #
class Racer(object):
    """ create an auto racer """
    # constructor
    def __init__(self, name, race_tiles):
        self.name = name
        self.data = []
        self.hp = MAX_HEALTH
        self.tspd = DEF_SPEED
        self.card = None # hold card
        ### counters ###
        self.resting = False # lose a turn, bool
        self.win = False # not yet a winner
        # trap immunity
        self.immune = False # immune to attacks or traps
        self.turns = [] # trap or card effect turn counter
        ### race ###
        self.raceplace = 0
        self.laps = 0
        self.tiles = race_tiles
        

    # # # # # # game modules # # # # # #
    
    # display status, game module
    def __str__(self):
        # player status
        if self.win:
            # if already won
            return "%6s passed the finish line!" % (self.name)
        elif self.resting:
            # resting means losing a turn after health has been zeroed
            return "%6s lost a turn.." % (self.name)
        else:
            if self.card != None:
                # has a card
                return RACER_W_CARD % (self.name, self.hp, 
                                       self.tspd, self.laps+1,
                                       RACE_LAPS, self.card['Name'])
            elif self.card == None:
                # no card
                return RACER_NO_CARD % (self.name, self.hp, 
                                         self.tspd, self.laps+1,
                                         RACE_LAPS)

    # check racer, game module
    def check(self, option='place'):
        """ returns racer's 'place' <int>, 'distance' <int> or 'card' <bool> status """
        option = option.lower()
        if self.raceplace >= self.tiles:
            self.raceplace -= self.tiles
            self.laps += 1
            print self.name, "crossed the finish line"
            if self.laps > (RACE_LAPS-1):
                # unlock assigning of win title to racer
                self.win = True
        # returning conditionals
        if 'place' in option:
            # returns racer place value
            return self.raceplace
        elif 'distance' in option:
            # returns racer distance if attacked
            return self.raceplace + (self.tiles * (self.laps))
        elif 'card' in option:
            # returns if racer has card
            if self.card != None: return True
            else: return False
        elif 'finish' in option:
            return self.win
            

    # racer trapped, game module
    def trap(self, traps):
        """ racer got trapped. supply traps <list> as parameter """
        if not self.immune:
            # randomly select a trap from a list of traps
            spring = random.choice(traps)
            # call hit upon racer trap
            self._hit(spring['Effect'], spring['Damage'])
            self.immune = True
            print TRAPPED % (self.name, spring['Description'],
                             spring['Name'], spring['Effect'],
                             spring['Damage'])
        else:
            self.immune = False

    # racer receive powerup, game module
    def receive(self, cards):
        """ racer receives card. supply cards <list> as parameter """
        # if no card and not yet a winner
        if self.card == None and not self.win:
            # randomly select a card from a list of cards
            self.card = random.choice(cards)
            print RECEIVE_CARD % (self.name, self.card['Name'])

    
    # # # # # # interface options # # # # # #
    
    # move racer, interface method
    def move(self):
        """ returns <int> new move for racer """
        # generate new move from 1 to racer's topspeed
        newmove = random.randint(1, self.tspd)
        # if ailing status still lingers (turns)
        if len(self.turns) > 0:
            # if effect turn counter is greater than zero
            if self.turns[1] > 0:
                # get effect turn variable at second index
                ctr = self.turns[1] 
                ctr -= 1 # subtract one turn 
                self.turns[1] = ctr
            else:
                # if effect turn is zero
                # default speed and effect counter is blank
                self.tspd = DEF_SPEED
                self.turns = []
        
        if self.resting: # if loses a turn
            # racer is resting reset its resting to default
            self.resting = False
            newmove = 0 # assign no new move
            
        # if not yet on finish line
        if not self.win: 
            self.raceplace += newmove # add new move to race placement
            return newmove
        else:
            return ''
        
    # use powerup, interface method
    def powerup(self, enemies):
        """ racer uses powerup card. supply racers <dict> as parameter """
        # powerup if card slot is not empty
        if self.card != None:
            # get card details
            cardname = self.card['Name']
            maxhits = self.card['Hits']
            # distance variable counter
            distance = []
            
            # # # attack card types # # #
            if 'Attack' in self.card['Type']:
                # supply effect turn counter
                self.turns = [self.card['Effect'], 2]
                # loop enemies to get their relative distance
                for racer in enemies:
                    # not including the initiating racer
                    if enemies[racer].name != self.name:
                        distance.append(enemies[racer])
                # after calculating opponents distances
                # check what card the hits
                
                ## hits one or more within range, forward attack
                if self.card['Hits'] > 0:
                    # hits only the first racer in the race track
                    if 'First' in self.card['Range']:
                        # check if one 
                        attack = True
                        # for each enemy racer, compute distance and attack
                        for dist in distance:
                            places = self._compute(dist)
                            # if enemy is ahead of initiating racer, attack
                            if places > 0: attack = True
                            else: attack = False
                        if attack:
                            # call special range to attack first racer
                            self._specialRange(distance, 
                                               self.card['Range'])
                    
                    # hits only the most nearest racer
                    elif 'Nearest' in self.card['Range']:
                        # call special range nearest racer
                        self._specialRange(distance, self.card['Range'])

                    # hits all others under attack range
                    else:
                        hits = maxhits
                        # for each enemy racer, calculate distance if hit
                        for dist in distance:
                            # compute range from each opponent's distance
                            targetting = self._compute(dist)
                            # hits are up and enemy racer in range
                            if hits > 0 and targetting >= 0 and \
                               targetting <= self.card['Range']:
                                # apply hit 
                                dist._hit(self.card['Effect'], 
                                          self.card['Damage'])
                                print ATTACKED % (dist.name, self.name,
                                                  cardname)
                                # diminish remaining hits
                                hits -= 1
                ## hits both front and backward within range, wave attack
                elif self.card['Hits'] == 0:
                    front = self.card['Range']
                    back = front * -1
                    # for each enemy, calculate its distance
                    for dist in distance:
                        targetting = self._compute(dist)
                        if targetting >= back and targetting <= front:
                            # call _hit with effect and damage parameter
                            dist._hit(self.card['Effect'], 
                                      self.card['Damage'])
                            print ATTACKED % (dist.name, self.name,
                                              cardname)
                ## hits all others, mega attack
                elif self.card['Hits'] == -1:
                    # for each enemy, just hit them all
                    for dist in distance:
                        dist._hit(self.card['Effect'], self.card['Damage'])
                        print ATTACKED % (dist.name, self.name, cardname)

            # # # support card type # # #
            elif 'Support' in self.card['Type']:
                # call on _support with effect and damage parameter
                self._support(self.card['Effect'], self.card['Damage'])
                print SUPPORT % (self.name, self.card['Effect'],
                                 self.card['Name'])
            # save card details to racer's knowledge if not yet saved
            if self.card not in self.data:
                self.data.append(self.card)
            # make racer's card slot empty
            self.card = None
        

    # # # # # # hidden calls # # # # # #

    # special range attack function, hidden call
    def _specialRange(self, distance_list, range_type):
        """ range types are 'First' and 'Nearest' also supply distance list here """
        # highest equals to zero in first
        if 'First' in range_type:
            highest = 0
        # highest equals to 10 in nearest
        elif 'Nearest' in range_type:
            highest = 10
        racer = None
        
        for dist in distance_list:
            targetting = self._compute(dist)
            # find the furthest enemy from the attacking racer
            if 'First' in range_type and targetting >= highest:
                highest = targetting
                # assign dist as the racer to hit
                racer = dist
            # find the nearest enemy from the attacking racer
            elif 'Nearest' in range_type and targetting <= highest:
                highest = targetting
                # assign dist as the racer to hit
                racer = dist
        else:
            racer._hit(self.card['Effect'], self.card['Damage'])
            # call other variables thru self
            print ATTACKED % (racer.name, self.name, self.card['Name'])
    
    # compute and return racer distance, hidden call
    def _compute(self, distance):
        """ returns racer's distance """
        # calculation is target's distance - attacker's (place * laps +1)
        return distance.check('distance') - (self.raceplace * (self.laps+1))
            
    # racer hit, hidden call
    def _hit(self, effect, damage):
        """ racer has been hit """
        effect = effect.lower()
        # decrease in stamina
        if "health" in effect:
            self.hp -= damage
            # if stamina falls below zero, movement halted
            if self.hp < 0:
                self.resting = True
                self.hp = MAX_HEALTH
        # decrease in speed
        if "speed" in effect:
            self.tspd -= damage
            # supply turn counter to two turns
            self.turns = [effect, 2]
            # never go down to negative or one move block
            if self.tspd < 2:
                self.tspd = 2            
        # lose a card
        if "card" in effect:
            # if no card, deal 1 damage to speed
            if not self.card:
                self.tspd -= 1
            else:
                self.card = None
        # lose a turn
        if "turn" in effect:
            self.resting = True
            
    # racer heal, hidden call
    def _support(self, effect, bonus):
        """ racer used support """
        effect = effect.lower()
        # increase in stamina
        if "health" in effect:
            self.hp += bonus
            # if stamina exceeds maximum, set it to max
            if self.hp > MAX_HEALTH:
                self.hp = MAX_HEALTH
        # increase in speed
        if "speed" in effect:
            self.tspd += bonus
            # supply turn counter to two turns
            self.turns = [effect, 2]
            # speed exceeding 10 remains 10
            if self.tspd > DEF_SPEED + 4:
                self.tspd = DEF_SPEED + 4
        # still under development
        if "card" in effect:
            self.receive(self.data)
        # gain extra turns
        if "turn" in effect:
            extra = self.move()
            print BLESSING.format(self.name, extra)


# # # # # # # # # # # # #
# # #  Game class   # # #
# # # # # # # # # # # # #
class Game(object):
    """ carry game saving and loading progress """
    
    # constructor
    def __init__(self):
        self._progress = None
        self.loadGame()

    # # # # # # game modules # # # # # #

    ''' 
    # check game progress
    def checkGameProgress(self):
        pass

    # set new player progress
    def setProgress(self, key, value):
        """ one-at-a-time appends [key] and [value] to player's progress """
        if not key in self.progress.iterkeys():
            try:
                self.progress[key] = value
            except KeyError, name:
                print 'Error appending key', name
        # new player's progress 
        new = {}
        # checks and updates player's progress
        for k in self.progress.iterkeys():
            if not self.progress[k] is False:
                new[k] = self.progress[k]
        # assign new progress to player
        self.progress = new

    # get player's progress
    def getProgress(self):
        """ returns a dictionary of the player's progress """
        return self.progress
    '''
    # save game
    def saveGame(self):
        # get game progress
        # write open a file
        # save progress to contents
        print '\nSaving...'
        with open('saveGame','w') as savefile:
            savefile.write('savegame='+str(self._progress))
        if savefile.closed:
            print 'Game Saved!'
    
    # load progress
    def loadGame(self):
        # read open a file
        # get contents on progress
        # save read content to game progress
        print 'Loading...'
        try:
            with open('saveGame','r') as loadfile:
                load = loadfile.readline()
                loadgame = load.split('=')
                self._progress = int(loadgame[1])
        except IOError:
            self._progress = 2
        else:
            if loadfile.closed:
                print 'Game Loaded!'

    def unlock(self, racetracksList, unlocked):
        if unlocked: # is true
            self._progress += 1
            print '\n\nYou have unlocked a new stage!\n\n'

    def checkLock(self):
        return self._progress



# # # # # # # # # # # # #
# # #  Track class  # # #
# # # # # # # # # # # # #
class Track(object):
    """ create a race track """

    # constructor
    def __init__(self, name, tiles):
        """ supply a track [name] and its maximum [tiles] """
        self.name = name
        self.tiles = tiles
        self.design = self._create('#','+')


    # # # # # # game modules # # # # # #
    
    # gets track information, game module
    def get(self, option='tiles'):
        """ returns track properties. [tiles] [name] [trap] [powerup] """
        if option == 'tiles':
            return self.tiles
        if option == 'name':
            return self.name
        if option == 'trap':
            return self.trapTL
        if option == 'powerup':
            return self.powerupTL

    # for console game, game module
    def __str__(self):
        return ' '.join(self.design)
        for i in self.design:
            print "%s" % i,
        return ''


    # # # # # # hidden calls # # # # # #
    
    # for console game, hidden call
    def _create(self, trapSymbol="x", powerupSymbol="*"):
        """
        changes trap and powerup symbols in the track
        returns three list inorder: Track design, trap tiles and powerup tiles
        """
        self.trapTL = []
        self.powerupTL = []

        # run random runner
        self.trapTL = self._runner(self.tiles, 4)
        # call regulate to no duplicate and adjacent tiles
        self.trapTL = self._regulate(self.trapTL, None)            
                
        self.powerupTL = self._runner(self.tiles,2)
        self.powerupTL = self._regulate(self.powerupTL, self.trapTL)
        self.powerupTL = self._regulate(self.powerupTL)
        
        powerups = []
        # remove same tile from trap list in powerup tile list
        for num in range(len(self.powerupTL)):
            if not (self.powerupTL[num] in self.trapTL):
                powerups.append(self.powerupTL[num])
        self.powerupTL = powerups[:]
        
        trapSymbol += "|"
        powerupSymbol += "|"
        self.newtrack = []
        for i in range(0, self.tiles):
            if i in self.trapTL:
                # print trapSymbol,
                self.newtrack.append(trapSymbol)
            elif i in self.powerupTL:
                # print powerupSymbol,
                self.newtrack.append(powerupSymbol)
            else:
                # print " |",
                self.newtrack.append(str(i%10)+"|")
        return self.newtrack

    # creates random tiles, hidden call
    def _runner(self, tilestotal, start=1, step=5):
        self.block = []
        end = step
        num = random.randint(start, end)
        self.block.append(num)
        start += 5
        end += 5
        while end < tilestotal:
            #print start, ',', end, ' : ',
            num = random.randint(start, end)
            start += step
            end += step
            self.block.append(num)
            #print start, ',', end
        return self.block

    def _regulate(self, tilelist1, tilelist2=None):
        """ check for adjacent tiles in tilelist1 and tilelist2 and correct them """
        if tilelist2 is None:    
            for num in range(1, len(tilelist1)-1):
                if tilelist1[num]-1 == tilelist1[num-1]:
                    # example, if num[2] is 7 and num[3] is 8
                    # if num[3]-1 == num[3-1=2]
                    # so num[3]=8-1=7 == num[2]=7
                    # num[2] must be subtracted by 2
                    new = tilelist1[num-1]
                    new-= 2
                    tilelist1[num-1] = new
            return tilelist1
        else:
            for num in range(len(tilelist1)-1):
                for ber in range(len(tilelist2)-1):
                    if tilelist1[num]+1 == tilelist2[ber]:
                        # example, if num[2] is 7 and num[3] is 8
                        # if num[3]-1 == num[3-1=2]
                        # so num[3]=8-1=7 == num[2]=7
                        # num[2] must be subtracted by 2
                        new = tilelist1[num]
                        new-= 1
                        tilelist1[num] = new
                    elif tilelist1[num]-1 == tilelist2[ber]:
                        # example, if num[2] is 7 and num[3] is 8
                        # if num[3]-1 == num[3-1=2]
                        # so num[3]=8-1=7 == num[2]=7
                        # num[2] must be subtracted by 2
                        new = tilelist1[num]
                        new+= 1
                        tilelist1[num] = new
            return tilelist1
        
