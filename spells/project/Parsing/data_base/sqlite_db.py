import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('spells_full.db')
    cur = base.cursor()
    if base:
        print('Data base connected')

def create_bd():
    base.execute('CREATE TABLE IF NOT EXISTS spells_with_desc \
        (name_of_the_spell, tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, description, source)')
        
def insert_db(name_of_the_spell, tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, description, source):
    cur.execute('INSERT INTO spells_with_desc VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', \
        (name_of_the_spell, tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, description, source))
    base.commit()



