# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:12:07 2021

@author: new
"""

"""dictionary methods"""

owndict = {
  "1": "prasanth",
  "2": "srini",
  "3": "rakesh"
} #myDictionary

owndict.clear() #clear

print (owndict)

owndict = {
  "1": "prasanth",
  "2": "srini",
  "3": "rakesh"
}

print (owndict)

x = owndict.copy() #copy

y = 0

thisdict = dict.fromkeys(owndict, y) #fromkeys

print (thisdict)

owndict = {
  "1": "prasanth",
  "2": "srini",
  "3": "rakesh"
}

g = owndict.get("1") #get

print (g)

i = owndict.items() #return items

print (i)

k = owndict.keys() #return keys

print (k)

owndict = {
  "1": "prasanth",
  "2": "srini",
  "3": "rakesh"
}

owndict.pop("3") #pop

print (owndict)

owndict.popitem() #popitems

print (owndict)

owndict = {
  "1": "prasanth",
  "2": "srini",
  "3": "rakesh"
}

set_ = owndict.setdefault("3", "mani") #set default

print (owndict)

owndict.update({"3": "gajini"}) #update

v = owndict.values() #values

print (v)




