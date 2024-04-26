#!/usr/bin/python3
from models import storage
from models.state import State
all_obj = storage.all()
print("-----Reloaded object---")
for key in all_obj.keys():
    print(all_obj[key])
state = State()
state.name = "Osun"
state.save()
print("----new State---")
print(state)