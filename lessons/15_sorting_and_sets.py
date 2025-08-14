# nums = [1,4,2,7,3,8,3,4,8,1]
# print(sorted(nums))
# names = ['shaun','ryu','abe','Apple','Brian','shaun']
# print(sorted(names))
# print()

# print(set(nums))
# print(set(names))
# print()

# ninjas = {'ryu':'black', 'yoshi':'red', 'crystal':'black'}
# print(set(ninjas.values()))
#=================================
def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belsts')


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

belt_count(ninja_belts)