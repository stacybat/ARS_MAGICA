from docx import Document
import json
from data_base import sqlite_db


def pars_docx():

    #This file lists all spells with description
    document = Document('Spells.docx') 

    #The json file lists all spell names
    with open('spell_name_file.json', 'r', encoding="utf-8") as f:
        names =json.load(f)

    #Names of spells are written in the list spells
    spells = []
    for i in names:
        spells.append(i)
        spell_run = 0

    #Declaring Variables
    name_of_the_spell = ''
    tech = ''
    form = ''
    req = ''
    level = 0
    spell_range = ''
    duration = ''
    target = ''
    spell_type = ''
    base_of_spell = ''
    spell_mod = ''
    description = ''
    source = ''
    p_2 = ''

    #Running through all paragraphs with content parsing to write to appropriate variables
    for para in document.paragraphs:

        #Removing extra spaces in paragraphs
        p = ''
        for w in para.text.split():
            p += w + ' '
        p = p.strip()

        #If the paragraph is empty, then we skip it
        if len(p) <= 1:
            continue

        #If we discover a paragraph from the name of a spell, then we start defining the spell's parameters in subsequent paragraphs.
        if p.lower() in spells:

            #After detecting the next spell name, we write the parameters of the previous spell to the database
            if spell_run == 4:
                sqlite_db.insert_db(name_of_the_spell, tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, description, source)
                
                '''print('name_of_the_spell:', name_of_the_spell)
                print('tech:', tech)
                print('form:', form)
                print('level:', level)
                print('req:', req)
                print('spell_range:', spell_range)
                print('duration:', duration)
                print('target:', target)
                print('description:', description)
                print('base_of_spell:', base_of_spell)
                print('spell_mod:', spell_mod)            
                print("spell_note:", spell_note)
                print('source:', source)'''
                
            #Determine the name of the spell
            name_of_the_spell = p.capitalize()

            #Determine the step in the spell run
            spell_run = 1

            #Reset variables
            tech = ''
            form = ''
            level = ''
            p_2 = ''
            req = ''
            spell_range = ''
            duration = ''
            target = ''
            spell_type = ''
            description = ''
            base_of_spell = ''
            spell_mod = ''
            spell_note = ''
            source = ''

        
        elif len(p) >= 6 and spell_run == 1:
            
            #Determine the technique, form, level and req. of the spell
            if len(p.split()) >= 2 and p.split()[0][0:2].capitalize() in ['Cr', 'In', 'Mu', 'Pe', 'Re']:
                j = 0
                while j in range(len(p) - 1 - len(p.split()[-1])):
                    p_2 = p[j] + p[j+1]
                    if p_2 in ['Cr', 'In', 'Mu', 'Pe', 'Re']:
                        tech = p_2                   
                        j +=2
                        continue
                    elif p[j] == '(':
                        j +=1
                        for r in p[j:]:
                            j += 1                        
                            if r == ')':
                                break
                            else:
                                req += r
                    elif p_2 in ['An', 'Aq', 'Au', 'Co', 'He', 'Ig', 'Im', 'Me', 'Te', 'Vi', 'Ae']:
                        form= p_2                   
                        j +=2
                        continue
                    else: continue
                level = p.split()[-1]
                spell_run = 2

        #Determine the spell range, duration, and target of the spell
        elif spell_run == 2 and len(p) > 3:
            i = 0
            spell_range = ''
            duration = ''
            target = ''

            while i in range(len(p.split())):
                if p.split()[i] == 'R:' or p.split()[i] == 'R':
                    spell_run = 3
                    i +=1
                    mod = p.split()[i:]
                    for m in mod:
                        if ':' in m:
                            break
                        spell_range += m
                        i += 1
                elif p.split()[i] == 'D:' or p.split()[i] == 'D':
                    spell_run = 3
                    i +=1
                    mod = p.split()[i:]
                    for m in mod:
                        if ':' in m:
                            break
                        duration += m
                        i += 1
                elif p.split()[i] == 'T:' or p.split()[i] == 'T':
                    spell_run = 3
                    i +=1
                    mod = p.split()[i:]
                    for m in mod:
                        if ':' in m:
                            break
                        if m == 'Ritual':
                            spell_type = m
                        else:
                            target += m
                        i += 1

            if spell_range[-1]==',':
                spell_range = spell_range[:-1]        
                duration = duration[:-1]

            if target[-1]==',':
                target = target[:-1]

            #Determine whether to look for requisite in the next paragraph
            if req == '':
                spell_run = 4
            elif req != '':            
                spell_run = 3

        #Determine the req. of the spell
        elif spell_run == 3:
            if p.split()[0] == 'Req:':
                req = p[5:]
                spell_run = 4
            else:
                spell_run = 4

        #Determine what is in the paragraph: base definition with modifiers or source or spell description or spell notes
        elif spell_run == 4 and not (p.isdigit()):

            if p.split()[0] == '(Base':
                if p.split()[1][-1] == ',':
                    base_of_spell = p.split()[1][:-1]
                else:
                    base_of_spell = p.split()[1]
                mod = p.split()[2:]
                for m in mod:
                    spell_mod += m + ' '
                spell_mod = spell_mod.strip()
                spell_mod = spell_mod[:-1]

            elif p.split()[0] == 'Source:':
                source = p[7:].strip()

            elif p.split()[0] == 'Note:':
                spell_note = p[5:].strip()
                
            elif not (len(p.split()) == 2 and p.split()[0]=='LEVEL') and not(len(p.split()) == 3 and p.split()[2]=='Spells'):            
                description += p

    #We write the parameters of the last spell to the database
    # sqlite_db.insert_db(name_of_the_spell, tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, description, source) 
    '''print('name_of_the_spell:', name_of_the_spell)
    print('tech:', tech)
    print('form:', form)
    print('level:', level)
    print('req:', req)
    print('spell_range:', spell_range)
    print('duration:', duration)
    print('target:', target)
    print('description:', description)
    print('base_of_spell:', base_of_spell)
    print('spell_mod:', spell_mod)            
    print("spell_note:", spell_note)
    print('source:', source)
    '''
