from db.models import Fish, Location, Bait

#   "Welcome!"
#       Give list of locations
#           "Select Location by ID"
#               we take input => Give list of fish from that location.id
#                   "select a Fish by ID"
#                       we take input =>
#                           prints f"you selected ${fish.name}! If you catch one it'll be worth PRICE. You need to use {bait.name} to catch it! Good luck!"


YES = ['y', 'ye', 'yes']
NO = ['n', 'no', 'nn']

# this will print out the locations
def create_location_table(locations):
    print('-' * 50)
    print(f'|ID  |LOCATION NAME{" " * 30}|')
    print('-' * 50)
    for location in locations:
        id_spaces = 4 - len(str(location.id))
        name_spaces = 43 - len(location.name)
        print(f'|{location.id}{" " * id_spaces}|{location.name}{" " * name_spaces}|')
    print('-' * 50)


# this will print out the filtered fish
def create_fish_table(fishes):
    print('-' * 50)
    print(f'|ID  |FISH NAME{" " * 34}|')
    print('-' * 50)
    for fish in fishes:
            id_spaces = 4 - len(str(fish.id))
            name_spaces = 43 - len(fish.name)
            print(f'|{fish.id}{" " * id_spaces}|{fish.name}{" " * name_spaces}|')
    print('-' * 50)



def final_f_string(baits, fish):
    for bait in baits:
        print(f"\n\nTo catch a {fish.name} you will need to use bait: {bait.name} and you will get {fish.price} Gold if you sell it! \n\n" )

