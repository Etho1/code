print('You went camping with your friends. You wake up and no one is around...')
choice_1 = input('grab your bag and HIKE to the river? or GET READY and wait at camp?')
if choice_1.lower() == 'hike':
    print('About halfway there, you hear rustling in a bush 20 feet off the path, you remember you packed a hatchet in your backpack...')
    choice_2 = input('GO investigate? // KEEP walking? // STOP and grab the hatchet?')
    if choice_2.lower() == 'go':
        print('You start walking through the brush; suddenly you feel a crazy stinging on your ankles, stinging nettle!')
        choice_3 = input('TURN around, head back to camp and treat the poison? // Darn it! I\'m gonna FIND out what is in that bush!')
        if choice_3.lower() == 'turn':
            print('You get back to camp, and put ointment on your ankles. Your friends show up a bit later, one covered in hives, who says "Hey, could I get some of that ointment?" (THE END)')
        elif choice_3.lower() == 'find':
            print('You run at the bush, and you hear a yelp, and your friend stands up out of the bush and says "What? were you trying to scare me?" (THE END)')
        else:
            print('Invalid choice, please restart.')
    elif choice_2.lower() == 'keep':
        print('You get closer to the river, and you think you hear laughter, however you hear that rustling even closer to you now...')
        choice_4 = input('KEEP going toward the laughter? // Spin on the rustling and THROW a rock at it?')
        if choice_4.lower() == 'keep':
            print('You find your friends at the river, one of your friends shows up a few minutes later, covered in hives, saying "I found some berries to snack on!" (THE END)')
        elif choice_4.lower() == 'throw':
            print('You throw the rock, and you hear a cry from the bush "OW!" a few seconds later your friend stands up with a bump on his head to add to those from the stinging nettle. (THE END)')
        else:
            print('Invalid choice, please restart.')
    elif choice_2.lower == 'stop':
        print('As you unzip your bag and grab the hatchet, the rustling gets louder. You stand up, and you definitley see something in the bush right off the path.')
        choice_5 = input('YELL at it to show itself? // KICK the bush?')
        if choice_5.lower() == 'yell':
            print('"Oh! didn\'t see you there, where you been?" your friend says as he stands up out of the bush covered in hives (THE END)')
        elif choice_5.lower() == 'kick':
            print('"Hey man! can\'t a guy look for berries in peace?" your friend says, rolling our of the bush clutching his head. (THE END)')
        else:
            print('Invalid choice, please restart.')
elif choice_1.lower() == 'get ready':
    print('You get to the bathroom, but the power seems to be out...')
    choice_6 = input('GRAB your flashlight and continue on? // LOOK for a way to turn on the power?')
    if choice_6.lower() == 'grab':
        print('You enter the bathroom, and you hear bumping and banging from one of the stalls...')
        choice_7 = input('ASK if they\'re okay? // CONTINUE on with your business')
        if choice_7.lower() == 'ask':
            print('"huh? oh yeah, I just can\'t see anything, say... could I borrow that light?"')
            choice_8 = input('GIVE him the light? // "Let me CONTINUE getting ready first and then you can"')
            if choice_8.lower() == 'give':
                print('"Thanks a ton man." he takes a minute, and hands you back your flashlight, and you continue getting ready and head back to camp (THE END)')
            elif choice_8.lower() =='CONTINUE':
                print('"Fine man..." You get ready, and pass your flashlight to the stranger. A minute later he passes it back soaking wet and warm! You drop the flashlight, wash your hands and run back to camp (THE END)')
            else:
                print('Invalid choice, please restart.')
        elif choice_7.lower() == 'continue':
            print('You finish getting ready in silence, and head back to camp, your friends are waiting there, cooking breakfast. (THE END)')
        else:
            print('Invalid choice, please restart.')
    elif choice_6.lower() =='look':
        print(' You round the side of the building and you see a breaker box with a lock on it...')
        choice_9 = input('Pull out your hatchet and BREAK the lock? // FIND the campsite managers and ask them to help?')
        if choice_9.lower() == 'break':
            print('It takes a few tries, but you smash the lock, and flip the breaker. You head back into the bashroom, and find an old man washing up. He says "Didje fix the lights lad?" "Yup" you relpy, and continue getting ready. (THE END)')
        elif choice_9.lower() == 'find':
            print('You find their cabin and knock on the door. An older woman answers and you tell her the dillemma, she grabs a key and you follow her over to the bathroom. She unlocks the lock and flips the breaker, and you continue on getting ready. (THE END)')
        else:
            print('Invalid choice, please restart.')
    
