#!/usr/bin/env python3

# run cli.py
#   Select Location
#       Choose a Season
#           select a Fish
#               prints row from the fishes table 


# print message "here are the locations "

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Fish, Location, Bait
from helpers import (create_location_table, create_fish_table, final_f_string)
#fill_cart, show_cart, remove_from_cart, collect_payment)

engine = create_engine('sqlite:///db/stardew.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    # Intro: welcome to the CLI, pick a Fishing Location
    print('''\n\n\n
    ___     _                         _                            __   __            _       _              _  _  
/ __|   | |_    __ _      _ _   __| |    ___   __ __ __   o O O \ \ / /  __ _     | |     | |     ___    | || | 
\__ \   |  _|  / _` |    | '_| / _` |   / -_)  \ V  V /  o       \ V /  / _` |    | |     | |    / -_)    \_, | 
|___/   _\__|  \__,_|   _|_|_  \__,_|   \___|   \_/\_/  TS__[O]  _\_/_  \__,_|   _|_|_   _|_|_   \___|   _|__/  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_| """"|_|"""""|_|"""""|_|"""""|_|"""""|_| """"| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'

''')
    print('Hello! Welcome to Stardew Valley. \n\n')
while True:
    print('Here is a list of fishing spots:')
    locations = session.query(Location)
    create_location_table(locations)

    # Get a choice of location, retrieve an object from the DB
    location = None
    #we need to increase scope of location_id
    location_id = None
    while not location:
        location_id = input('Please enter the ID of the location you would like to go fishing: ')
        location = session.query(Location).filter(Location.id == location_id).one_or_none()
            
    
    # Display list of items at the store
    # needs to show list of fish available at the location
    print('\n\nHere are all the fish you can catch at this location:')
    #this is where we need to put our filter
    fishes = session.query(Fish).filter(Fish.location_id == location_id)
    create_fish_table(fishes)

    
    fish = None
    while not fish:
        fish_id = input('Please enter the ID of the Fish you would like to catch:')
        fish = session.query(Fish).filter(Fish.id == fish_id).one_or_none()
        if fish not in fishes:
            fish_id = input('That fish is not available at this location. Please try again: ')
            fish = session.query(Fish).filter(Fish.id == fish_id).one_or_none()
            
            baits = session.query(Bait).filter(Bait.id == fish.bait_id)
            final_f_string(baits, fish)
            
        else:
            baits = session.query(Bait).filter(Bait.id == fish.bait_id)
            final_f_string(baits, fish)
            
 


    # prompt the user to start again
    restart = input("Are you done fishing for the day? (Y/N): ")
    if restart.upper() != "N":
        print('Thank you for fishing with us in Stardew Valley!\n\n')
        print(''' __   __            _       _               ___                                      ___                     _               _  _                      _    
 \ \ / /  __ _     | |     | |      o O O  / __|    ___    _ __     ___      o O O  | _ )   __ _     __     | |__     o O O | \| |    ___   __ __ __  | |   
  \ V /  / _` |    | |     | |     o      | (__    / _ \  | '  \   / -_)    o       | _ \  / _` |   / _|    | / /    o      | .` |   / _ \  \ V  V /  |_|   
  _|_|_  \__,_|   _|_|_   _|_|_   TS__[O]  \___|   \___/  |_|_|_|  \___|   TS__[O]  |___/  \__,_|   \__|_   |_\_\   TS__[O] |_|\_|   \___/   \_/\_/  _(_)_  
_| """ |_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_| """ | 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' \n\n ''')
        break
        
