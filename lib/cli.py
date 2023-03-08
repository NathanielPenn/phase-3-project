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
from helpers import (create_location_table, create_fish_table)
#fill_cart, show_cart, remove_from_cart, collect_payment)

engine = create_engine('sqlite:///db/stardew.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    # Intro: welcome to the CLI, pick a Fishing Location
    print('''
    ___     _                         _                            __   __            _       _              _  _  
  / __|   | |_    __ _      _ _   __| |    ___   __ __ __   o O O \ \ / /  __ _     | |     | |     ___    | || | 
  \__ \   |  _|  / _` |    | '_| / _` |   / -_)  \ V  V /  o       \ V /  / _` |    | |     | |    / -_)    \_, | 
  |___/   _\__|  \__,_|   _|_|_  \__,_|   \___|   \_/\_/  TS__[O]  _\_/_  \__,_|   _|_|_   _|_|_   \___|   _|__/  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_| """"|_|"""""|_|"""""|_|"""""|_|"""""|_| """"| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'

''')
    print('Hello! Welcome to Stardew Valley. \n\n')
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
        fish_id = input('\n\nPlease enter the ID of the Fish you would like to catch:')
        fish = session.query(Fish).filter(Fish.id == fish_id).one_or_none()
        print(fish)

    # Display list of items at the store
    # print('Here are all the fish you can catch at this location:')
    # create_fish_table(fish)

    # # Start adding items to cart
    # shopping_cart, cart_total = fill_cart(session, store)
    # print('Here are the items in your cart:')
    # show_cart(shopping_cart)

    # # Remove unwanted items from cart
    # remove_from_cart(session, shopping_cart, cart_total)

    # Collect payment
    # print(f'Your total is ${cart_total:.2f}\n')
    # collect_payment(cart_total)

    print('Thank you for using the grocery checkout CLI!\n')
