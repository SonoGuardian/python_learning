# ninja_belts = {"crystal": "red", "ryu": "black"}#, "":"", "":""}

# print(ninja_belts)

# print (ninja_belts['crystal'])

# #key in dict
# print("yoshi" in ninja_belts)
# print("ryu" in ninja_belts)

# print(list(ninja_belts.keys()))
# print('')
# #print(ninja_belts.values())

# vals = list(ninja_belts.values())
# print(vals)
# print('Black in vals:', vals.count('black'))
# print('Blue in vals:',vals.count('blue'))
# print('')

# ninja_belts["youshi"] = "red"
# print(ninja_belts)
# print('')
#=====================
# person = dict(name="shaun", age=27, height="6ft")
# print(person)
#=====================
def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f"I am {key} and I am a {val} belt")


ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name: ')
    ninja_belt = input('enter a belt color: ')
    ninja_belts[ninja_name] = ninja_belt
    
    another = input('Add another? (y/n): ')
    if another == 'y':
        continue
    else:
        print("")
        break


ninja_intro(ninja_belts)

#def even_or_odd(int(number))