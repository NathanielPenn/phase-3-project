from app import db  
from models import Fish, Location, Bait
Session = sessionmaker(bind=engine)

session = Session()

# create fish instances  - Pelican Town - Spring
smallmouth_bass = Fish(name='Smallmouth Bass', season='Spring', price=50)
shad = Fish(name='Shad', season='Spring', price=60)
bream = Fish(name='Bream', season='Spring', price=45)

# create fish instances  - Pelican Town - Summer
catfish = Fish(name='Catfish', season='Summer', price=200)  
sunfish = Fish(name='Pike', season='Summer', price=30)

# create fish instances  - Pelican Town - Fall  
tiger_trout = Fish(name='Tiger Trout', season='Fall', price=150)

# create fish instances  - Pelican Town - Winter
lingcod = Fish(name='Lingcod', season='Winter', price=120)  
pike = Fish(name='Pike', season='Winter', price=100)

# create fish instances - Beach - Spring
flounder = Fish(name='Flounder', season='Spring', price=100)
eel = Fish(name='Eeel', season='Spring', price=85)  
herring = Fish(name='Herring', season='Spring', price=30)

# create fish instances  - Beach - Summer
red_snapper = Fish(name='Red Snapper', season='Summer', price=50)  
pufferfish = Fish(name='Pufferfish', season='Summer', price=200)

# create fish instances  - Beach - Fall
sardine = Fish(name='Sardine', season='Fall', price=40)  
albacore = Fish(name='Albacore', season='Fall', price=75)
super_cucumber = Fish(name='Super Cucumber', season='Fall', price=250)

# create fish instances  - Beach - Winter
red_mullet = Fish(name='Red Mullet', season='Winter', price=75)  
squid = Fish(name='Squid', season='Winter', price=80)
pike = Fish(name='Pike', season='Winter', price=100)



#create fish instances Cindsnap Forest - Spring
chub = Fish(name='Chub', season='Spring', price=50)

#create fish instances Cindsnap Forest - Summer
dorado = Fish(name='Dorado', season='Summer', price=100)

#create fish instances Cindsnap Forest - Fall
salmon = Fish(name='Salmon', season='Fall', price=75)

#create fish instances Cindsnap Forest - Winter
midnight_carp = Fish(name='Midnight Carp', season='Winter', price=225) 

#create fish instances Mountain - Spring
bullhead = Fish(name='Bullhead', season='Spring', price=75)
large_mouth_bass = Fish(name='Large Mouth Bass', season='Spring', price=100)

#create fish instances Mountain - Summer
sturgeon = Fish(name='Sturgeon', season='Summer', price=200)

#create fish instances Mountain - Fall
walleye = Fish(name='Walleye', season='Fall', price=105)

#create fish instances Mountain - Winter
perch = Fish(name='Perch', season='Winter', price=55) 



#create fish instances Mine - Null

ghostfish = Fish(name='Ghostfish', season='year round', price=45) 
stonefish = Fish(name='Stonefish', season='year round', price=300) 
ice_pip = Fish(name='Ice Pip', season='year round', price=500) 
lava_eel = Fish(name='Lava Eel', season='year round', price=700) 


#create fish instances Secret Woods - Null
woodskip = Fish(name='Woodskip', season='year round', price=75) 

#create fish instances The Desert - Null
sandfish = Fish(name='Sandfish', season='year round', price=75)
scorpion_carp = Fish(name='Scorpion Carp', season='year round', price=150)

#create fish instances Sewers - Null
green_algae = Fish(name='Green Algae', season='year round', price=15)
white_algae = Fish(name='White Algae', season='year round', price=25)

#create fish instances Mutant Bug Lair - Null
slimejack = Fish(name='Slimejack', season='year round', price=100) 

#create fish instances Witch Swamp - Null
void_salmon = Fish(name='Void Salmon', season='year round', price=150) 


#create fish instances Ginger Island - Null
blue_discus = Fish(name='Blue Discus', season='year round', price=120)
lionfish = Fish(name='Lionfish', season='year round', price=100)
tilapia = Fish(name='Tilapia', season='year round', price=75)


#create fish instances Pirate Cove - Null
stingray = Fish(name='Stingray', season='year round', price=180)
tuna = Fish(name='Tuna', season='year round', price=100)




# create location instances  
farm = Location(name='Farm', type='Lake', water='Fresh')  
pelican_town = Location(name='Pelican Town', type='River', water='Fresh')
cindersnap_forest = Location(name='Cindsnap Forest', type='River', water='Fresh')
beach = Location(name='The Beach', type='Ocean', water='Salt')
mountain = Location(name='The Mountain', type='Lake', water='Fresh')

desert = Location(name='The Desert', type='River', water='Salt')
sewer = Location(name='The Sewers', type='Lake', water='Fresh')  
mines = Location(name='The Mines', type='Lake', water='Fresh')
secret_woods = Location(name='Secret Woods', type='Lake', water='Fresh')

night_market = Location(name='Night Market', type='Lake', water='Fresh')  
mutant_bug_lair = Location(name='Mutant Bug Lair', type='River', water='Fresh')
witch_swamp = Location(name='Witch Swamp', type='Lake', water='Fresh')  

ginger_island = Location(name='Ginger Island', type='River', water='Fresh')
pirate_cove = Location(name='Pirate Cove', type='Lake', water='Fresh')  

# create bait instances  
bait = Bait(name='Bait', live= 1, price=5)
magnet = Bait(name='Magnet', live= 0, price=1000)
wild_bait = Bait(name='Wild Bait', live= 1, price=10)  
magic_bait = Bait(name='Magic Bait', live= 1, price=5000)  

# add fish instances to database  
session.bulk_save_objects([smallmouth_bass, shad, bream, catfish, sunfish, tiger_trout, lingcod, pike, flouder, eel, herring, red_snapper, pufferfish, sardine, albacore, super_cucumber, red_mullet, squid, pike, chub, dorado, salmon, midnightcarp, bullhead, large_mouth_bass, sturgeon, walleye, perch, ghostfish, stonefish, ice_pip, lava_eel, woodskip, sandfish, scorpion_carp, green_algae, white_algae, slimejack, void_salmon, blue_discusss, lionfish, tilapia, stingray, tuna]) 

# add bait instances to database  
session.bulk_save_objects([bait, magnet, wild_bait, magic_bait]) 
#adding location instances to database - location sessions
session.add(farm)  
session.add(pelican_town)  
session.add(cindersnap_forest)
session.add(beach)  
session.add(mountain)  
session.add(desert)
session.add(sewer)  
session.add(mines)  
session.add(secret_woods)
session.add(night_market)  
session.add(mutant_bug_lair)  
session.add(witch_swamp)
session.add(ginger_island)  
session.add(pirate_cove)  

session.commit()  
