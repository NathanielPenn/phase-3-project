from app import db  
from models import Fish, Location, Bait
Session = sessionmaker(bind=engine)

session = Session()

# create fish instances  - Pelican Town - Spring
smallmouth_bass = Fish(name='Smallmouth Bass', season='Spring', time='Day')
shad = Fish(name='Shad', season='Spring', time='Rain')
bream = Fish(name='Bream', season='Spring', time='Day')

# create fish instances  - Pelican Town - Summer
catfish = Fish(name='Catfish', season='Summer', time='Rain')  
sunfish = Fish(name='Pike', season='Summer', time='Day')

# create fish instances  - Pelican Town - Fall  
tiger_trout = Fish(name='Tiger Trout', season='Fall', time='Day')

# create fish instances  - Pelican Town - Winter
lingcod = Fish(name='Lingcod', season='Winter', time='Day')  
pike = Fish(name='Pike', season='Winter', time='Day')

# create fish instances - Beach - Spring
flounder = Fish(name='Flounder', season='Spring', time='Day')
eel = Fish(name='Eeel', season='Spring', time='Rain')  
herring = Fish(name='Herring', season='Spring', time='Day')

# create fish instances  - Beach - Summer
red_snapper = Fish(name='Red Snapper', season='Summer', time='Rain')  
pufferfish = Fish(name='Pufferfish', season='Summer', time='Day')

# create fish instances  - Beach - Fall
sardine = Fish(name='Sardine', season='Fall', time='Day')  
albacore = Fish(name='Albacore', season='Fall', time='Day')
super_cucumber = Fish(name='Super Cucumber', season='Fall', time='Rain')

# create fish instances  - Beach - Winter
red_mullet = Fish(name='Red Mullet', season='Winter', time='Day')  
squid = Fish(name='Squid', season='Winter', time='Day')
pike = Fish(name='Pike', season='Winter', time='Day')



#create fish instances Cindsnap Forest - Spring
chub = Fish(name='Chub', season='Spring', time='Day')

#create fish instances Cindsnap Forest - Summer
dorado = Fish(name='Dorado', season='Summer', time='Day')

#create fish instances Cindsnap Forest - Fall
salmon = Fish(name='Salmon', season='Fall', time='Day')

#create fish instances Cindsnap Forest - Winter
midnight_carp = Fish(name='Midnight Carp', season='Winter', time='Day') 

#create fish instances Mountain - Spring
bullhead = Fish(name='Bullhead', season='Spring', time='Day')
large_mouth_bass = Fish(name='Large Mouth Bass', season='Spring', time='Day')

#create fish instances Mountain - Summer
sturgeon = Fish(name='Sturgeon', season='Summer', time='Day')

#create fish instances Mountain - Fall
walleye = Fish(name='Walleye', season='Fall', time='Rain')

#create fish instances Mountain - Winter
perch = Fish(name='Perch', season='Winter', time='Day') 



#create fish instances Mine - Null

ghostfish = Fish(name='Ghostfish', season='Null', time='Day') 
stonefish = Fish(name='Stonefish', season='Null', time='Day') 
ice_pip = Fish(name='Ice Pip', season='Null', time='Day') 
lava_eel = Fish(name='Lava Eel', season='Null', time='Day') 


#create fish instances Secret Woods - Null
woodskip = Fish(name='Woodskip', season='Null', time='Day') 

#create fish instances The Desert - Null
sandfish = Fish(name='Sandfish', season='Null', time='Day')
scorpion_carp = Fish(name='Scorpion Carp', season='Null', time='Day')

#create fish instances Sewers - Null
green_algae = Fish(name='Green Algae', season='Null', time='Day')
white_algae = Fish(name='White Algae', season='Null', time='Day')

#create fish instances Mutant Bug Lair - Null
slimejack = Fish(name='Slimejack', season='Null', time='Day') 

#create fish instances Witch Swamp - Null
void_salmon = Fish(name='Void Salmon', season='Null', time='Day') 


#create fish instances Ginger Island - Null
blue_discus = Fish(name='Blue Discus', season='Null', time='Day')
lionfish = Fish(name='Lionfish', season='Null', time='Day')
tilapia = Fish(name='Tilapia', season='Null', time='Day')


#create fish instances Pirate Cove - Null
stingray = Fish(name='Stingray', season='Null', time='Day')
tuna = Fish(name='Tuna', season='Null', time='Day')




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
bait = Bait(name='Bait', live= 1, cost=5)
magnet = Bait(name='Magnet', live= 0, cost=1000)
wild_bait = Bait(name='Wild Bait', live= 1, cost=10)  
magic_bait = Bait(name='Magic Bait', live= 1, cost=5000)  

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
