from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    #content
    #timestamp
    
    class Meta:
        database = db
        
        
def menu_loop():
    """Show the Menu"""
    
    
def add_entry():
    """Add an Entry"""
    
    
def view_entries():
    """View previous Entries"""
    
    
def delete_entry(entry):
    """Delete an Entry"""
    
    
if __name__ == '__main__':
    menu_loop()
    
    
