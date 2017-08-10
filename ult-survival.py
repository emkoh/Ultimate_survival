start = '''
Introduction: It's your first day off your new job and you decide you want to
start your day off with a nice hike on the trails. You notice that every tree
looks the same on the path and you feel lost. You start to panic. You do not have any
supplies with you, just a bottle of water. As you walk, you see a trail.
Do you a) take the trail or b) stay on your path? Type 'a' for a or 'b' for b.
'''
S1 = '''
You're walking along and start getting
really hungry, while you're walking you see some berries.
Do you want to a) eat them or b) keep walking even though you're really hungry?
'''
S11 = '''
So you keep walking, now you hear a rustle in the bush..
Do you want to a) investigate or b) to run away?
'''
S111 = '''
You only have a little bit of water left.
Do you want to a) drink it now or b) save it for later?
'''
S1111 = '''
You drink the water and keep hiking up the trail. A nearby park ranger finds you
and leads you to the trail's exit. Great job, you survived!
'''
S1112 = '''
You are now feeling fuzzy and pass out on the dirt from dehydration. An animal
comes and gets you and you're now dead.
'''
S112 = '''
You find an animal that looks injured. Do you a) help or b) leave the poor
animal there suffering? :(
'''
S1121 = '''
You run away and you come across a group of people that were hiking there too
so they save you.
'''
S1122 = '''
You investigated the animal hidden in the bushes, only to find out that it was
playing dead! Unfortunately, it is a predator and it attacks you! You bleed to death.
'''
S12 = '''
You eat the berries! Your stomach starts to feel funny, and you are a little
skeptical.
Do you a) stop eating and keep walking or b) continue eating
'''
S2 = '''
You take the trail and fall into a hole that was covered by a bunch of bushes
and get an injury.
Do you want to a) stay and wait for help or b) keep going?
'''
S21 = '''
While you wait, you see a branch full of berries that fell with you. Do you
a) tough it up and crawl out of the hole, or b) eat the berries?
'''
S22 = '''
You get about halfway down the trail and realize nature is calling. You look
around and all you see is a bush. Do you want to a) relieve yourself by the bush
or b) keep going?
'''
S221 = '''
You decide to go, but you quickly realized that the bush was poison ivy! As you
keep walking along, and you see a beehive. Maybe some honey will help with the
unbearable itching. Do you a) grab some honey or b) keep walking?
'''
S222 = '''
You continue on the path. The sun is going down and you think it would be a good
idea to start a fire. Do use a) pine cones or b) pine needles?
'''
S2211 = '''
The hive is hanging in a tree. You see a branch lying on the ground. You grab
it and poke at the hive to knock it down. The angry bees come out and attack you.
You are now dead.
'''
S2212 = '''
You decided to continue on the trail. You turn the corner and you see a little
office with a park ranger in it. You walk over and the ranger cares for your
wound and takes you home. You're saved!
'''
S2221 = '''
The fumes from the pine cones ignite a nearby tree, which sets off a massive
forest fire! You are now dead!
'''
S2222 = '''
Your fire is safe and contained with the pine needles, so you stay warm.
Fortunately, people saw the smoke and came to find you. You're saved!
'''
S32 = '''
The berries were poisonous! You didn't realize this, and now you're dead.
Better luck next time.
'''
theend = '''
The end
'''
playagain = '''
Do you want to play again?
a) Yes
b)No
'''

def start_over(user_input):
    print(theend)
    print (playagain)
    user_input = input()
    if user_input == "a":
        print(start)
        user_input = input()
        trailpath = trail_path(user_input)
    else:
        print("ok, goodbye!")
        exit()



def bees_pr(user_input):

    if user_input == "a":
        print(S2211)
        startover = start_over(user_input)


    elif user_input == "b":
        print(S2212)
        startover = start_over(user_input)

    else:
        print("Type 'a' or 'b'")
        user_input = input()
        bees_pr(user_input)
    return user_input

def fire(user_input):
    if user_input == "a":
        print(S2221)
        startover = start_over(user_input)


    elif user_input == "b":
        print(S2222)
        startover = start_over(user_input)
    else:
        print("Type 'a' or 'b'")
        user_input = input()
        fire(user_input)
    return user_input

def animal_run(user_input):
    if user_input == "a":
        print(S1122)
        startover = start_over(user_input)


    elif user_input == "b":
        print(S1121)
        startover = start_over(user_input)
    else:
        print("Type 'a' or 'b'")
        user_input = input()
        animal_run(user_input)
    return user_input

def water(user_input):
    if user_input == "a":
        print(S1111)
        startover = start_over(user_input)

    elif user_input == "b":
            print(S1112)
            startover = start_over(user_input)
    else:
        print("Type 'a' or 'b'")
        user_input = input()
        water(user_input)
    return user_input

def fire_ivy(user_input):
    if user_input == "a":
        print(S221)
        user_input = input()

        bees_pr(user_input)

    elif user_input == "b":
        print(S222)
        user_input = input()
        fire(user_input)
    else:
        print("Type 'a' or 'b'")
        user_input = input()
        fire_ivy(user_input)
    return user_input

def water_invest(user_input):
    if user_input == "a":
        print(S112)
        user_input = input()

        animal_run(user_input)

    elif user_input == "b":
        print(S111)
        user_input = input()

        water(user_input)
    else:
        print("Type 'a' or 'b'")
        user_input = input()
        water_invest(user_input)
    return user_input

def nature_death(user_input):
    if user_input == "a":
        print(S22)
        user_input = input()

        fire_ivy(user_input)


    elif user_input == "b":
        print(S32)
        startover = start_over(user_input)
    else:
        print("Type 'a' or 'b'")
        user_input = input()
        nature_death(user_input)
    return user_input

def wait_go(user_input):
    if user_input=="a":
        print(S21)
        user_input = input()

        nature_death(user_input)

    elif user_input == "b":
        print(S22)
        user_input = input()
        fire_ivy(user_input)
        user_input = input()
    else:
        print("Type 'a' or 'b'")
        user_input = input()
        wait_go(user_input)
    return user_input

def berries_path(user_input):
    if user_input == "a":
        print(S12)
        user_input = input()
        nature_death(user_input)
    elif user_input == "b":
        print(S11)
        user_input = input()
        water_invest(user_input)
    else:
        print("Type 'a' or 'b'")
        user_input = input()
        berries_path(user_input)
    returstart = '''
