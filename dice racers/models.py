from datetime import datetime, timedelta
from pytz import timezone
from sqlalchemy import Column, Integer, String, Text, Float
from database import Base

local = timezone('Asia/Manila') # our timezone +8

# database classes
class Track(Base):
    __tablename__ = 'tracks'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True) 
    tiles = Column(Integer) # maximum racing tiles
    envi = Column(String(30)) # environment
    trapblk = Column(Integer) # how many blocks of traps
    giftblk = Column(Integer) # how many blocks of gifts
    desc = Column(String(200)) # description
    
    def __init__(self, name, tiles, environment, 
            description, trapblocks=5, giftblocks=4):
        self.name = name.capitalize()
        self.tiles = tiles
        self.envi = environment.capitalize()
        self.desc = description.capitalize()
        self.trapblk = trapblocks
        self.giftblk = giftblocks
    
    def __repr__(self):
        return '<%r Track %r>' % (self.envi, self.name)

class Trap(Base):
    __tablename__ = 'traps'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    envi = Column(String(30)) # environment
    pwr = Column(Integer) # damage power
    eff = Column(String(10)) # target effect
    desc = Column(String(100)) # description
    
    def __init__(self, name, power, effect, environment, description):
        self.name = name.capitalize()
        self.pwr = power
        self.eff = effect.capitalize()
        self.envi = environment.capitalize()
        self.desc = description.capitalize()
        
    def __repr__(self):
        return '<%r Trap %r>' % (self.envi, self.name)
    
class Powerup(Trap):
    __tablename__ = 'powerups'
    # same from trap attributes
    # add two new att for powerup
    rng = Column(Integer) # attack range
    cls = Column(String(10)) # attack class
    
    def __init__(self, name, power, atkrange, atktype, effect, description):
        self.name = name.capitalize()
        self.pwr = power
        self.rng = atkrange
        self.cls = atktype
        self.eff = effect.capitalize()
        self.desc = description.capitalize()
        
    def __repr__(self):
        return '<%r Powerup %r>' % (self.cls, self.name)
    
class Player(Base):
    """ add players to the game. """
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    giv = Column(String(40)) # given name
    sur = Column(String(50)) # surname
    usn = Column(String(50), unique=True) # username
    psw = Column(String(80)) # password
    lvl = Column(Integer) # player level
    exp = Column(Float(precision=2)) # experience points
    pnt = Column(Integer) # points
    login = Column(String(25)) # last login
    
    def __init__(self, given, surname, username, password, points=0, exp=0.0):
        self.giv = given.capitalize()
        self.sur = surname.capitalize()
        self.usn = username
        self.psw = password
        self.lvl = 1
        self.exp = exp
        self.pnt = points
        self.login = local.localize(datetime.today()) # last login today
        
    def __repr__(self):
        return '<Lvl %r Player %r>' % (self.lvl, self.usn)
