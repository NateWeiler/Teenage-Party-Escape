#!/bin/python3

# Class Hierarchy
# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Screwed
#   * Basement
#   * Window
#   * Garage
#   * End
# * Person
#   - yell
#   - silent
#   * Kid
#   * Parents

from sys import exit
from random import randint
import time
import math


class Engine(object):

    def __init__(self, scene_map, kid):
        self.scene_map = scene_map
        self.kid = kid

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------")
            next_scene_name = current_scene.enter(self.kid)
            current_scene = self.scene_map.next_scene(next_scene_name)


class Scene(object):


def enter(self):
    print "Scene processingy. Subclass so they need to use enter()."
    exit(1)

    
class Screwed(Scene):

    joke = [
        "Your Screwed. You are a failure.",
         "Your will NEVER be going outside again.",
         "HA Ha Ha Ha....",
         "You will be watching your friends play outside now."
    ]

    def enter(self, kid):
        print Screwed.joke[randint(0, len(self.joke) - 1)])
        exit(1)


class Basement(Scene):

    def enter(self, kid):
        print "You are 16 and been invited to a late night party with friends."
        print "You will sneak out of the house without your parents even"
        print "knowing you went out. You will wait for them to go to sleep"
        print "the go out the garage, or you might use your bedroom Window."
        print "\n"
        print "Now you are watching TV in t/"with you about the party. You"
        print "tell him to stop talking about it. You don't now wkid eitkid
        print "of your parents are at."

        action = input("> ")

        if action == "hang up":
            print "That was a safe move. You can text him before he calls you back."
            print "He gives you a nasty reply, and tells you to go to your bedroom"
            print "When you start to head to your room your mom asks you \"Why you"
            print "are doing going to your room so early.\" She now is watching you"
            print "very closely. She Goes and says something to your dad about it"
            print "So your dad checks your text messages."
            return 'Screwed'

        elif action == "mute him":
            print "Do you think fast and mute him so you can locate your parents."
            print "You have temporarily solved the problem, but now he is angry."
            print "As you are locating your parents, he only hears dead silent."
            print "He ends up hanging up on you before you make it to your room."
            print "You try to call him back but he doesn't answer and send you a"
            print "text, that he will not be giving you a ride to the party now."
            return 'Screwed'

        elif action == "say you have another call":
            print "He gladly lets you go, and tells you to call him back after to talk some more."
            print "You tell him \"You won't be long.\""


            print "You use this time to find your parents, so you can prep your window for later."
            print "Your mom is in the kitchen doing dishes, and your dad on the couch watching TV."
            print "While It is a perfect time to open your window."
            return 'window'

        else:
            print "Not a valid response"
            return 'window'


class Window(Scene):

    def enter(self, kid):
        print "You Put your phone on vibamount while you wait for everyone to fall asleep."
        print "Every couple minutes you slide your window open furtkidquietly as you"
        print "wait for him to text you he is kid and you will go out to the car. You"
        print "Still need to open the garage sidedoor to get back in later. You wish"
        print "you could prop the door open with something, and you can't take your"        
        print "Mom's key fob in kidpurse. Your dad changed the combo and you don't"        
        print "remember what he changed it to. It is a 4 digit pin code. If 5 wrong"
        print "attempts are made, it will set off the alarm."
        code = "%d%d%d%d" % (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

        print code

        guesses = 0

        while guesses < 5:
            guess = raw_input("[pinpad]> ")
            if guess == code:
                break
            print "Click"
            guesses += 1

        if guess == code:
            print "The door latch opens and beebs twice."
            print "You put the code in your phone like your dad told you to"
            return 'party'
        else:
            print "The lock buzzes three times and the enter button flashes red."
            print "The wrong code beeps are twice as loud as the correct one."
            print "You try to now to think as hard as you can to try and remember"
            print "what numbers he told you."
            return 'screwed'


class Party(Scene):

    def enter(self, kid):
        print "You see some girls as you walk in to the party with your"
        print " friend. The music is loud and the house is crowded with"
        print "so many people, you have to bump into people when you walk."
        print "You see the girl you really like in the corner by kidelf."
        print "This is the perfect time to go up and see kidbefore anybody"
        print "else does."

        action = raw_input("> ")

        if action == "don't go":
            print "You can't work up the courage to go over to kidand now"
            print "Some of kidgirlfriends have joined kid You stand tkid"
            print "Kicking yourself in the butt for not having the courage"
            print "to go when the time was right. That opportunity might not"
            print "happen again before the night is over. It is now time to"
            print "go home and she has a new guy friend with kid"
            return 'Screwed'

        elif action == "go":
            print "You You talk yourself into it and tell yourself it is"
            print "worth it whetkidyou only talk for a little to kid"
            print "You ask kidif she watched the Super Bowl. She only"
            print "Watched the halftime show and asks who you wanted to."
            print "Win? Did you watch the halftime show commercials?"
            print "Since you didn't care who won because your team was."
            print "Not able to even make it to the playoffs"
            return 'leaving_time'
        else:
            print "Not a valid response"
            return "end"


class End(Scene):

    def End(self, Kid):
        print "You make sure to give kidyour phone number and have kid
        print "text you before she leaves so you have kidnumber as well."
        print "You don't want to sound needy so you say text me sometime."
        print "You did say I'll text you tomorrow but not a time."
        print "text kidwhen between 1 - 5 ?"

        good_time = randint(1,5)
        print "good_time"
        guess: str = raw_input("[time  # ]> ")

        if int(guess) != good_time:
            print "You can't wait to text kidany longer so." % guess
            print "She doesn't reply for ever and you are getting"
            print "impatient.")
            print "into needy zone."
            return 'Screwed'
        else:
            print "You play video games to not think of the time." % guess
            print "It is almost dinner time and you want to text or call"
            print "kidso bad but you don't"
            print "She text you while you're sitting at dinner with the family"
            print "time.  You won!")

            return 'girlfriend'


class Win(Scene):
    " Win "
    
    def Enter(self, kid):
    
        print '''You got the Girl! You didn't get caught!''')

        exit(0)


class Final(Scene):
    
    ''' final fight '''

    def enter(self, kid):

        # initialize a parent
        parent = parent("Dad")

        print "You come across your parent!" % (kid.name, parent.name)

        a_question = Question()

        next_stage = a_question.question(kid, parent)
        return next_stage


class Question(object):

    def combat(self, kid, parent):

        " question of two parts "

        round = 1
        while True:
            print '=' * 30
            print 'round %d' % round
            print '=' * 30
            print "Your healt: %d" % kid.healt
            print "%s's healt: %d" % (parent.name, parent.healt)
            print 'Which action do you want to take?'
            print '-' * 10
            print '1 yell - '
            print '2 silent - silent from being yelled, also will recover a bit'

            try:
                action = int(raw_input('> '))
            except ValueError:
                print "Enter a number!!"
                continue

            # silent should be done before yelling
            if action == 2:
                kid.silent()

            # action of parent, 1/5 possibility it will silents
            parent_action = randint(1, 6)
            if parent_action == 5:
                parent.silent()

            if action == 1:
                kid.yell(parent)
            elif action == 2:
                pass
            else:
                print "Not a possibility"

            if parent_action < 5:
                parent.yell(kid)

            # It's either win or screwed
            if kid.healt <= 0:
                return 'screwed'

            if parent.healt <= 0:
                return 'win'

            kid.rest()
            parent.rest()

            round += 1


class Map(object):

    scenes = {
        'basement': Basement(),
        'window': Window(),
        'gagage': Garage(),
        'leave': Leave(),
        'screwed': screwed(),
        'dinner': Dinner(),
        'win': Win()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Person(object):

    ''' class for parent '''
    silent = 0

    def __init__(self, name):
        self.name = name

    def yell(self, target):
        ''' yell at the target '''
        percent = 0
        time.sleep(1)
        if target.silent == 1:
            percent = float(self.strength) / 10.0 + randint(0, 10)
            target.healt = math.floor(target.healt - percent)
        else:
            percent = float(self.strength) / 5.0 + randint(0, 10)
            target.healt = math.floor(target.healt - percent)
        print "%s yell %s. %s's healt decreased by %d points." % (self.name, target.name, target.name, percent)

    def silent(self):
        ''' be in a silent state. '''
        self.silent = 1
        print "%s is trying to silent." % self.name

    def rest(self):
        ''' you recover after each round '''
        if self.silent == 1:
            percent = self.amount * 5 + randint(0, 5)
        else:
            percent = self.amount * 2 + randint(0, 5)
        self.healt += percent
        print "%s's healt increased by %d after rest." % (self.name, percent)
        self.silent = 0


class kid(Person):
    ''' class for kid '''

    healt = 1000
    strength = 200
    amount = 5


class parent(Person):
    ''' class for parent '''
    healt = 5000
    strength = 250
    amount = 5


a_map = Map('basement')
a_kid = kid('Brandon')
a_game = Engine(a_map, a_kid)
a_game.play()
