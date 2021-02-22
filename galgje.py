# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:31:56 2021

@author: Rocco
"""
import random

def verborgen_woord_start(woord): #het te raden woord heeft nu nog alleen vraagtekens
    verborgen_lijst = []
    for letter in woord:
        verborgen_lijst.append('?')
    return(verborgen_lijst)





def doe_poging(): #je geeft een letter
    poging = input()
    while poging not in ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o', 'p', 'q', 'r', 's',\
                         't', 'u','v','w', 'x','y', 'z']:
        print('geef een geldige invoer')
        poging = input()
    return(poging)


def plaatsen(letter_keus, woord): #bijv plaatsen(lala,a) geeft output 1,3
    letter_op_plaatsen = []
    plaats = 0
    for letter in woord:
        if letter != letter_keus:
            plaats += 1
        else:
            letter_op_plaatsen.append(plaats)
            plaats += 1
    return(letter_op_plaatsen)
  
            


    
def spelverloop(woord):  
    galg_stand = 0 #in het begin is er nog niks van de galg getekend
    verborgen_woord = verborgen_woord_start(woord) #in het begin staat er '......' en moet je de puntjes raden
    
    pogingen_gehad = [] #hier komen de letters die je hebt geroepen en er niet in voor bleken te komen
    
    while (galg_stand <11) and ('?' in verborgen_woord): #zolang je niet af bent of er nog puntjes open staan:
        
        poging = doe_poging() #je roept een letter
        
        if woord.count(poging) == 0: #als de letter niet voorkomt...
            if poging in pogingen_gehad: #en als je die al geroepen hebt...
                print('die heb je al gehad, hij kwam niet voor')
            else: #als je 'm nog niet gehad hebt...
                galg_stand += 1 #dan wordt een deel van de galg getekend en slaan we de letter op als 'gehad'
                print(galg_stand)
                pogingen_gehad.append(poging)
                print(pogingen_gehad)
        else:
            for i in plaatsen(poging, woord): #als de letter wél voorkomt, dan bijv. 'h...a.' wordt 'h..lal'
                verborgen_woord[i] = poging
            print(verborgen_woord)
            
    if galg_stand == 11:
        return('je hangt')
    else:
        return('je hebt het woord geraden, gefeliciteerd!')

woordenlijst = ['bananenschaal', 'cocacolakoffie', 'cyclochemicaliegas', 'flikkegentenpets',\
                'locomokipkaravitae', 'mechalomanolisch', 'pesterostoide', 'zenuwpezenkat']

gekozen_woord = random.choice(woordenlijst)

print(spelverloop(gekozen_woord))

#print(spelverloop(woord))
        

    
    
            
            


        
