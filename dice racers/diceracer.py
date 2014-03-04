import random

from racering import *


def powerupCards(track):
    """ Initializes all powerup cards. Supply a [track] to include its power cards """
    # print track
    track = track.lower()
    
    #@@ regular cards list @@#
    regulars = [
        {'Name':'Ace Missile', 'Type':'Attack',
         'Effect':'Health', 'Damage':2,
         'Range':'First', 'Hits':1 },
        {'Name':'Thunderbolts', 'Type':'Attack',
         'Effect':'Turn', 'Damage':1,
         'Range':1, 'Hits':-1 },
        {'Name':'Health Capsule', 'Type':'Support',
         'Effect':'Health', 'Damage':5,
         'Range':None, 'Hits':None },
        {'Name':'Wind Surf', 'Type':'Support',
         'Effect':'Speed', 'Damage':3,
         'Range':None, 'Hits':None },
        {'Name':'Fire Blast', 'Type':'Attack',
         'Effect':'Health', 'Damage':3,
         'Range':5, 'Hits':3 },
        {'Name':'Shockwave', 'Type':'Attack',
         'Effect':'Speed', 'Damage':3,
         'Range':3, 'Hits':0 },
        {'Name':'Air Jumper', 'Type':'Support',
         'Effect':'Turn', 'Damage':1,
         'Range':None, 'Hits':None },
        {'Name':'Gravity Well', 'Type':'Attack',
         'Effect':'Card', 'Damage':0,
         'Range':3, 'Hits':0 }
        ]
    regulars.sort()

    #@@ special area only powerups @@#
    # forest card list
    forest = [
        {'Name':'Bee Launcher', 'Type':'Attack',
         'Effect':'Turn', 'Damage':1,
         'Range':4, 'Hits':1 },
        {'Name':'Slingshot', 'Type':'Attack',
         'Effect':'Health', 'Damage':2,
         'Range':6, 'Hits':1 },
        {'Name':'Juicy Fruit', 'Type':'Support',
         'Effect':'Health', 'Damage':4,
         'Range':None, 'Hits':None },
        {'Name':'Wooden Bow', 'Type':'Attack',
         'Effect':'Health', 'Damage':3,
         'Range':7, 'Hits':3 }
        ]
    forest.sort()
    
    # city card list
    city = [
        {'Name':'Oil Can', 'Type':'Attack',
         'Effect':'Speed', 'Damage':3,
         'Range':5, 'Hits':1 },
        {'Name':'Skateboard', 'Type':'Support',
         'Effect':'Speed', 'Damage':3,
         'Range':None, 'Hits':None },
        {'Name':'Icecream Sling', 'Type':'Attack',
         'Effect':'Health', 'Damage':3,
         'Range':4, 'Hits':1 },
        {'Name':'Groceries', 'Type':'Support',
         'Effect':'Health', 'Damage':5,
         'Range':None, 'Hits':None }
        ]
    city.sort()

    # desert card list
    desert = [
        {'Name':'Cactus Cannon', 'Type':'Attack',
         'Effect':'Speed', 'Damage':2,
         'Range':3, 'Hits':0 },
        {'Name':'Water Jug', 'Type':'Support',
         'Effect':'Health', 'Damage':3,
         'Range':None, 'Hits':None },
        {'Name':'Camel Caravan', 'Type':'Support',
         'Effect':'Speed', 'Damage':4,
         'Range':None, 'Hits':None },
        {'Name':'Sand Bag', 'Type':'Attack',
         'Effect':'Turn', 'Damage':1,
         'Range':4, 'Hits':1 }
        ]
    desert.sort()

    # mountain card list
    mountain = [
        {'Name':'Pickaxe Swing', 'Type':'Attack',
         'Effect':'Health', 'Damage':3,
         'Range':1, 'Hits':0 },
        {'Name':'Mountain Roar', 'Type':'Attack',
         'Effect':'Card', 'Damage':0,
         'Range':1, 'Hits':-1 },
        {'Name':'Strong Boots', 'Type':'Support',
         'Effect':'Turn', 'Damage':1,
         'Range':None, 'Hits':None },
        {'Name':'Mighty Slingshot', 'Type':'Attack',
         'Effect':'Health', 'Damage':2,
         'Range':7, 'Hits':3 }
        ]
    mountain.sort()

    # snow card list
    snow = [
        {'Name':'Big Snowball', 'Type':'Attack',
         'Effect':'Health', 'Damage':2,
         'Range':'Nearest', 'Hits':1 },
        {'Name':'Snow Mobile', 'Type':'Support',
         'Effect':'Speed', 'Damage':5,
         'Range':None, 'Hits':None },
        {'Name':'Ice Gripper', 'Type':'Support',
         'Effect':'Turn', 'Damage':1,
         'Range':None, 'Hits':None },
        {'Name':'Icicle Launcher', 'Type':'Attack',
         'Effect':'Health', 'Damage':3,
         'Range':5, 'Hits':1 }
        ]
    snow.sort()

    # island card list
    island = [
        {'Name':'Stick Harpoon', 'Type':'Attack',
         'Effect':'Health', 'Damage':2,
         'Range':4, 'Hits':1 },
        {'Name':'Improvised Cannon', 'Type':'Attack',
         'Effect':'Health', 'Damage':3,
         'Range':8, 'Hits':3 },
        {'Name':'Strong Boots', 'Type':'Support',
         'Effect':'Speed', 'Damage':3,
         'Range':None, 'Hits':None },
        {'Name':'Tiki Torcher', 'Type':'Attack',
         'Effect':'Speed', 'Damage':3,
         'Range':2, 'Hits':0 }
        ]
    island.sort()

    # check and return chosen track's special cards
    # plus the regular ones
    if track == 'forest':
        return (regulars + forest)    
    elif track == 'city':
        return (regulars + city)
    elif track == 'desert':
        return (regulars + desert)        
    elif track == 'mountain':
        return (regulars + mountain)
    elif track == 'snow':
        return (regulars + snow)
    elif track == 'island':
        return (regulars + island)
    
    elif track == 'all' or track == 'training':
        # sum up all cards
        cards = regulars + forest + city + desert + mountain + snow + island
        #cards.sort()
        count = 0
        # print em out yall
        for card in cards:
            if card['Type'] is 'Attack':
                print 'X '+card['Name'],
                print "["+card['Effect']+"-"+str(card['Damage']),
                if card['Hits'] is 0:
                    print 'HitAllInRange',
                elif card['Hits'] is -1:
                    print 'HitAll',
                else:
                    print 'Hitx'+str(card['Hits']),
                if type(card['Range']) is int:
                    print str(card['Range'])+"Tiles]"
                else:
                    print card['Range']+"]"
            else:
                print 'O '+card['Name'],
                print "["+card['Effect']+"+"+str(card['Damage'])+"]"
            count += 1
        print '  Total cards:', count
        if track == 'training':
            return cards


def trapCards(track):
    """ Initializes [track] trap cards """
    track = track.lower()
    sample_name = 'Ampryieol'

    # forest traps
    forest = [
        {'Name':'Prickly Thorns',   'Effect':'Speed',   'Damage':2,
         'Description':'walked in nearby the'},
        {'Name':'Mad Woodcutter',   'Effect':'Health',  'Damage':3,
         'Description':'got chased by a'},
        {'Name':'Forest Fire',      'Effect':'Turn',    'Damage':1,
         'Description':'was trapped near the'},
        {'Name':'Wild Boar',        'Effect':'Health',  'Damage':2,
         'Description':'got attacked by a'},
        {'Name':'Rapid Ape',        'Effect':'Card',    'Damage':0,
         'Description':'\'s card was stolen by a'},
        {'Name':'Plant Growth',      'Effect':'Speed',   'Damage':2,
         'Description':'got slowed down by'}
        ]
    # city traps
    city = [
        {'Name':'Open Manhole',     'Effect':'Health',  'Damage':3,
         'Description':'fell in an'},
        {'Name':'Pedestrian',       'Effect':'Turn',    'Damage':1,
         'Description':'must wait for the'},
        {'Name':'Construction Site','Effect':'Speed',   'Damage':3,
         'Description':'cautioned from the'},
        {'Name':'Garbage Truck',    'Effect':'Health',  'Damage':4,
         'Description':'was rammed by a busy'},
        {'Name':'Sneaky Burglar',  'Effect':'Card',    'Damage':0,
         'Description':'\'s card was robbed by a'},
        {'Name':'Rushing Biker',       'Effect':'Health',  'Damage':3,
         'Description':'got trampled from a'}
        ]
    # desert traps
    desert = [
        {'Name':'Cactus Plant',     'Effect':'Card', 'Damage':0,
         'Description':'fell and got bruised by a'},
        {'Name':'Sandy Wind',       'Effect':'Turn', 'Damage':1,
         'Description':'got blinded by a'},
        {'Name':'Gila Monster',     'Effect':'Health', 'Damage':3,
         'Description':'was attacked by a'},
        {'Name':'Arid Scorpion',    'Effect':'Speed', 'Damage':2,
         'Description':'was nearly disabled by an'},
        {'Name':'Intense Heat',     'Effect':'Health', 'Damage':4,
         'Description':'got sunburned by'},
        {'Name':'Desert Mirage', 'Effect':'Speed', 'Damage':3,
         'Description':'miscalculated the'}
        ]
    # mountain traps
    mountain = [
        {'Name':'Cliff Slide', 'Effect':'Card', 'Damage':0,
         'Description':'\'s card fell to the'},
        {'Name':'Cold Rain', 'Effect':'Speed', 'Damage':3,
         'Description':'got pelted by sudden'},
        {'Name':'Mountain Goat', 'Effect':'Health', 'Damage':3,
         'Description':'got rammed by a huge'},
        {'Name':'Wild Yak', 'Effect':'Health', 'Damage':2,
         'Description':'was shocked from a'},
        {'Name':'Rattlesnake', 'Effect':'Speed', 'Damage':2,
         'Description':'\'s leg got bitten by a'},
        {'Name':'Grizzly Bear', 'Effect':'Turn', 'Damage':1,
         'Description':'got chased by a'}
        ]
    # snow traps
    snow = [
        {'Name':'Blizzards', 'Effect':'Turn', 'Damage':1,
         'Description':'was slowed down by harsh'},
        {'Name':'Hailstones', 'Effect':'Speed', 'Damage':2,
         'Description':'got pelted by golf-sized'},
        {'Name':'Frostbite', 'Effect':'Card', 'Damage':0,
         'Description':'suffered a'},
        {'Name':'Polar Bear', 'Effect':'Health', 'Damage':3,
         'Description':'provoked a large'},
        {'Name':'Rabid Wolf', 'Effect':'Health', 'Damage':2,
         'Description':'was attacked by a'},
        {'Name':'Icy Walkway', 'Effect':'Speed', 'Damage':3,
         'Description':'got slipped on an'}
        ]
    # island traps
    island = [
        {'Name':'Tropical Storm',   'Effect':'Speed', 'Damage':3,
         'Description':'got buffeted by a severe'},
        {'Name':'Coconuts',         'Effect':'Speed', 'Damage':2,
         'Description':'was disabled by falling'},
        {'Name':'Rockfall',         'Effect':'Turn', 'Damage':1,
         'Description':'\'s path was covered by a'},
        {'Name':'Coral Reef',       'Effect':'Health', 'Damage':2,
         'Description':'got injured by the shore\'s'},
        {'Name':'Craggy Rocks',     'Effect':'Card', 'Damage':0,
         'Description':'stumbled upon the island\'s'},
        {'Name':'Tribesman',        'Effect':'Health', 'Damage':3,
         'Description':'got darted by a disturbed'}
        ]
    
    if track == 'forest':
        return forest
    elif track == 'city':
        return city            
    elif track == 'desert':
        return desert
    elif track == 'mountain':
        return mountain
    elif track == 'snow':
        return snow
    elif track == 'island':
        return island
            
    elif track == 'all':
        print 'Sample Racer:', sample_name
        print
        count = 0
        traps = (forest + city + desert + mountain + snow + island)
        for trap in traps:
            print "%s %s '%s' [%s-%d]" % (sample_name, trap['Description'],
                                        trap['Name'], trap['Effect'],
                                        trap['Damage'])
            count += 1
        print '   Total traps:', count


def racersAndTrack(game):
    """ initializes and returns racers and race tracks """
    # racers dictionary #
    racers = {'a':'Leon', 'b':'Eric', 'c':'Sean', 'd':'Alice', 'e':'Basty',
              'f':'Tina', 'g':'Joann', 'h':'Denver', 'i':'Kent', 'j':'Meg'
              }
    # race track list
    tracks = {
        'a':Track('Forest', 30),
        'b':Track('City', 38),
        'c':Track('Desert',42),
        'd':Track('Mountain',40),
        'e':Track('Snow',32),
        'f':Track('Island',40)
        }
    racetracks = {}
    progress = 0
    for trc in sorted(tracks.iterkeys()):
        if progress < game.checkLock():
            racetracks[trc] = tracks[trc]
            progress += 1
        else:
            break
    
    return racers, racetracks

"""
def setup():
    "" selects the race track and players ""
    
    racers, racetracks = racersAndTrack()

    # select players loop
    while True:
        for index, racer in enumerate(sorted(racers.iterkeys())):
            print "  %s. %s  |" % (racer, racers[racer]),
            if (index+1) % 5 == 0:
                print
                print "- " *30
        
        # prompt for player 1
        racer1 = raw_input("Select Racer #1: ").lower()
        # prompt for player 2
        racer2 = raw_input("Select Racer #2: ").lower()
        
        try:
            player1 = racers[racer1]
            player2 = racers[racer2]
        except KeyError, name:
            print "No such racer!", name
            continue

        if player1 != player2:
            print ">>> Racer 1 has chosen '%s'" % (player1)
            print ">>> Racer 2 has chosen '%s'" % (player2)
            break
        else:
            print "No identical racers allowed!"
            continue
        
    # print a newline
    print 

    # sort out the chosen players from the racers list
    other_players = []
    for racer in racers:
        if racer != racer1 and racer != racer2:
            other_players.append(racer)
    
    # randomize one for player3
    numbr = randint(0,len(other_players)-1)
    racer3 = other_players[numbr]
    other_players.remove(racer3)
    
    numbr = randint(0,len(other_players)-1)
    racer4 = other_players[numbr]
    # select race track loop
    while True:
        print "Race Tracks"
        for rt in racetracks:
            print " %s. %s @ %d" % (rt, racetracks[rt].get('name'), racetracks[rt].get('tiles'))

        choice = raw_input('Select race track: ').lower()
        
        try:
            tracks = racetracks[choice]
        except KeyError, choice:
            print "No such track exist!", choice
            continue
        break
    
    players = {'a':Player(racers[racer1], tracks.get('tiles')),
               'b':Racer(racers[racer2], tracks.get('tiles')),
               'c':Racer(racers[racer3], tracks.get('tiles')),
               'd':Racer(racers[racer4], tracks.get('tiles'))
               }
    
    trackname = tracks.get('name')
    for player in players.values():
        player.add(tracks.get('tiles'))
    return [tracks, players, trapCards(trackname), powerupCards(trackname)]

"""
    
### prototype game methods ###
def display(option='all'):
    """ display option ['all','racers','traps','gifts'] """
    print tracks
    if option == 'racers' or option == 'all':
        for racer in sorted(racers.iterkeys()):
            print racers[racer].check(), racers[racer]
    print '-'*30
    if option == 'traps' or option == 'all':
        for trap in traps:
            sorted(trap.iterkeys())
            print trap.values()
    print '-'*30
    if option == 'gifts' or option == 'all':
        for card in cards:
            sorted(card.iterkeys())
            print card.values()

def moveall():
    """ moves all racers """
    positions = []
    # set blank dirt road
    for tile in range(0, tracks.get()):
        positions.append(" |")
    # set racers in the dirt
    for racer in sorted(racers.iterkeys()):
        move = racers[racer].move()
        positions[racers[racer].check()] = ">"+racer
    # print dirt road of the track
    for pos in positions:
        print pos,
    print
    print tracks
    print "  Moving Racers... "
    for racer in sorted(racers.iterkeys()):
        place = racers[racer].check()
        # trap block
        if place in tracks.get('trap'):
            racers[racer].trap(traps)
        # gift block
        if place in tracks.get('powerup'):
            racers[racer].receive(cards)
        print place, racers[racer]
        print
    

def usePowerup(racer_index):
    """ uses the powerups of those who are in the [racer_index] """
    print "  Using Cards... "
    for racer in sorted(racers.iterkeys()):
        if racer in racer_index:
            racers[racer].powerup(racers)
    for racer in racers:
        print racers[racer]
        print
    print " *" * 40


####### ## ##### ##### ##### ## # #####

def startup():
    with open('intro','r') as f:
        for line in f:
            print line,
    print
    # play true
    return True

def menu(gameController):
    print '---'*5
    print
    print 'r=Race'
    print 'l=Load'
    print 'e=Exit'
    print '---'*5
    while True:
        choice = str(raw_input('Select: ')).lower()
        if choice in '':
            continue
        if choice in 'r':
            return 1
        elif choice in 'l':
            gameController.loadGame()
        elif choice in 'e':
            return None
        else:
            continue

def setup(ctrls, racers, racetracks):
    """ supply controllers (players) to return a list containing race essentials """
    print '\n'*3
    if ctrls is not None:

        print 'Select your Racer '
        print "- " *32
        for index, racer in enumerate(sorted(racers.iterkeys())):
            print "| %s %6s |" % (racer, racers[racer]),
            if (index+1) % 5 == 0:
                print
            
        print "- " *32
        # select players loop
        while True:
            # prompt for player 1
            racer1 = raw_input("Select Racer#1: ").lower()
            if ctrls == 2:
                # prompt for player 2
                racer2 = raw_input("Select Racer#2: ").lower()
        
            try:
                player1 = racers[racer1]
                # ctrlr is 2 players
                if ctrls == 2:
                    player2 = racers[racer2]
                else:
                    racer2 = None
            except KeyError, name:
                print "No such racer!", name
                print
                continue

            if ctrls == 1:
                print ">>> Racer 1 has chosen '%s'" % player1
                break
            elif ctrls == 2:
                # c
                if player1 != player2:
                    print ">>> Racer 1 has chosen '%s'" % (player1)
                    print ">>> Racer 2 has chosen '%s'" % (player2)
                    break
                else:
                    print "No identical racers allowed!"
                    print
                    continue
            
        # print a newline
        print 
    
        # sort out the chosen players from the racers list
        other_players = []
        for racer in racers:
            if ctrls == 2:
                if racer != racer1 and racer != racer2:
                    other_players.append(racer)
            else:
                if racer != racer1:
                    other_players.append(racer)

        if ctrls == 1:
            # randomize player2 if only one player
            racer2 = random.choice(other_players)
            other_players.remove(racer2)
        
        # randomize one for player3
        racer3 = random.choice(other_players)
        other_players.remove(racer3)
        # randomize for player4
        racer4 = random.choice(other_players)


        print '\n'*3
        # select race track loop
        while True:
            print "Select Race track"
            print '--'*10
            for rt in sorted(racetracks.iterkeys()):
                print " %s. %s @ %d" % \
                      (rt, racetracks[rt].get('name'), racetracks[rt].get('tiles'))
            print '--'*10
            choice = raw_input('Select race track: ').lower()
            
            try:
                tracks = racetracks[choice]
            except KeyError, choice:
                print "No such track exist!", choice
                continue
            break
    
        # add track total blocks and complete the racers
        players = {'a':Racer(racers[racer1], tracks.get('tiles')),
                   'b':Racer(racers[racer2], tracks.get('tiles')),
                   'c':Racer(racers[racer3], tracks.get('tiles')),
                   'd':Racer(racers[racer4], tracks.get('tiles'))
                   }

        trackname = tracks.get('name')
        return [tracks, players, trapCards(trackname), powerupCards(trackname)]
        
    else:
        # return empty list
        return []


# call startup
#tracks, racers, traps, cards = setup(1)
#print
#display()

def gameplay(ctrls, essentials, game):
    """ supply as parameter the list returned by setup function """

    if len(essentials) == 0:
        return False
    
    # get main track
    racetrack = essentials[0]
    # get racers selected
    racers = essentials[1]
    # selected track traps
    traps = essentials[2]
    # regular cards + track specials
    cards = essentials[3]

    ### in module functions ###
    def display(key, players, track):
        if key == 'track':
            print
            road = []
            for tile in range(0, track.get()):
                road.append("_|")
            # set racers in the dirt
            for racer in sorted(players.iterkeys()):
                road[players[racer].check()] = racer+'|'
            # print dirt road of the track
            for dirt in road:
                print dirt,
            print
            print track
            print
        else:
            print players[key].check(), players[key]

    def move(key, players):
        players[key].move()

    def checktiles(key, players, track, traps, cards):
        # get player[key]'s place position
        place = players[key].check()
        # trap block
        if place in track.get('trap'):
            # call on trap method 
            players[key].trap(traps)
        # gift block
        if place in track.get('powerup'):
            # call on receive method
            players[key].receive(cards)
            
    def powerup(key, players):
        # call powerup method on player[key]
        players[key].powerup(players)

    # manual players game menu
    options = {'z':'Move','x':'Use Card','p':'Pause'}
    # race standings dictionary
    standing = []
    # start the race
    startRace = True
    
    print '\n'*3
    
    while startRace:
        # # # # display track # # # #
        display('track', racers, racetrack)
        
        # # # # display racers loop # # # #
        for racer in sorted(racers.iterkeys()):
            checktiles(racer, racers, racetrack, traps, cards)
            display(racer, racers, racetrack)
            print
        
        print '#'*46            
        # # # # interface loop # # # #
        for racer in sorted(racers.iterkeys()):
            # player one
            if racer in 'a' and not racers[racer].check('finish'):
                while True:
                    # player one menu
                    print '[',
                    for opt in sorted(options.iterkeys(), reverse=True):
                        if opt in 'x' and not racers[racer].check('card'):
                            continue
                        else:
                            print opt+'-'+options[opt],
                            if not opt in 'p':
                                print '|',
                    # input command
                    #print 'check card: ', racers[racer].check('card')
                    select = raw_input(']  Orders? ').lower()
                    if select in '':
                        continue
                    
                    # compare
                    if select in 'zxp':
                        print
                        print '#'*46
                        if select == 'z':
                            move(racer, racers)
                            break
                        elif select == 'x' and racers[racer].check('card'):
                            powerup(racer, racers)
                            move(racer, racers)
                            break
                        else:
                            # to be continued 'p' command
                            continue
                    else:
                        # input not found in 'zxp'
                        continue
                    
            elif not racer in 'a' and not racers[racer].check('finish'):
                # move npcs
                move(racer, racers)
                
            else:
                # if already finished append to race standing variable
                if not racer in standing:
                    standing.append(racer)
                if len(standing) == 4:
                    startRace = False

        # opponents powerup    
        for racer in sorted(racers.iterkeys()):
            if not racer in 'a' and random.randint(1, 10) % 2 == 1:
                powerup(racer, racers)
        print '#'*46

    print '\n' * 5
    print '#' * 5, 'R A N K I N G', '#' * 5
    print
    unlockvar = False
    # display winners
    for pos in range(len(standing)):
        if standing[pos] in 'a' and pos == 0:
            print '  {0}  ==> {1:10} !!!'.format(pos+1, racers[standing[pos]].name),
            # set unlock mechanism
            unlockvar = True
            print 'yay'
        else:
            print '  {0}  ==> {1:10}'.format(pos+1, racers[standing[pos]].name)
        print
        
    print ' Thank you for playing!'
    print '#' * 25, '\n'*3
    
    while True:
        ans = raw_input('[m-Main Menu | e-Exit Game]   ').lower()
        if ans in 'm':
            # continue 
            ans = True
            break
        elif ans in 'e':
            ans = False
            break
        else:
            continue
    return (ans, unlockvar)



def main():
    play = startup()
    gameControl = Game()
    while play:
        # menu
        players = menu(gameControl)
        if players is None:
            break
        # racersList and racetracksList
        racers, racetracks = racersAndTrack(gameControl)
        # setup 
        essentials = setup(players, racers, racetracks)
        # race play
        play, lock = gameplay(players, essentials, gameControl)
        # unlock
        gameControl.unlock(racetracks, lock)
        gameControl.saveGame()
        
    print '\n\nLets race again!\n\n'
    

main()
raw_input('\n\nPress the enter key to quit.')
