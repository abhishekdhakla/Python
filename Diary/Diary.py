#!user/bin/env Python3

import os
import sys
from collections import OrderedDict
import datetime
from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)
    
    class Meta:
        database = db
        
        
def initilize():
    """Create a database and Table"""
    db.connect()
    db.create_tables([Entry], safe = True)
    

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

        
def menu_loop():
    """Show the Menu"""
    choice = None
    
    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()
        
        if choice in menu:
            clear()
            menu[choice]()
    
    
def add_entry():
    """Add an Entry"""
    print("Enter your entry. Press CTRL + D when done!")
    data = sys.stdin.read().strip()
    
    if data:
        if input("Save Entry? Y/n").lower() != 'n':
            Entry.create(content = data)
            print("Saved Successfully :)")
    
def view_entries(search_query = None):
    """View previous Entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    if search_query:
        entries = entries.where(Entry.content.contain(search_query))
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %I: %M %p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n' + '='*len(timestamp))
        print('N) Next Entry')
        print('D) Delete Entry')
        print('q) quit')
        
        action = input("Action: N/q/D ").lower().strip()
        if action == 'q':
            break
        elif action == 'd':
            delete_entry(entry)

def search_entries():
    """Search entries for a string."""
    view_entries(input('Search Query: '))


def delete_entry(entry):
    """Delete an Entry"""
    if input("Are you sure? Y/n ").lower().split() == 'y':
        entry.delete_instance()
        print("Entry Deleted Successfully!!")

    
menu = OrderedDict([
        ('a', add_entry),
        ('v', view_entries),
        ('s', search_entries),
])

    
if __name__ == '__main__':
    initilize()
    menu_loop()
