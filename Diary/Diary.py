#!user/bin/env Python3

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
    
        
        
def menu_loop():
    """Show the Menu"""
    choice = None
    
    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()
        
        if choice in menu:
            menu[choice]()
    
    
def add_entry():
    """Add an Entry"""
    print("Enter your entry. Press CTRL + D when done!")
    data = sys.stdin.read().strip()
    
    if data:
        if input("Save Entry? Y/n").lower() != 'n':
            Entry.create(content = data)
            print("Saved Successfully :)")
    
def view_entries():
    """View previous Entries"""
    
    
def delete_entry(entry):
    """Delete an Entry"""

    
menu = OrderedDict([
        ('a', add_entry),
        ('v', view_entries),
])

    
if __name__ == '__main__':
    initilize()
    menu_loop()
    
    
