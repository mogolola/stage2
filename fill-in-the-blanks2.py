import os
def make_choice():
    user_choice=raw_input("Hi there, this is a fill-in-blank game, There are 3 objuects, it's all about video games and you can choose one to play on. For 'halo' please choose 1 ,for 'uncharted' choose 2 , for 'the lengends of zelda' choose 3")
    if user_choice==str(1):
        play_game(halo_answers,halo_text)
    elif user_choice==str(2):
        play_game(uncharted_answers,uncharted_text)
    elif user_choice==str(3):
        play_game(zelda_answers,zelda_text)
    else:
        print 'error, please type in again'
        make_choice()

def word_in_pos(word,current_attempt):         #this function checks if there is a blank in the word splited. If not it will return None. 
    if blanks[current_attempt] in word:
        return blanks[current_attempt]
    return None

def replace(content,answer,current_attempt): #this function will replace the current answered blank with the exact answer which was just made by users.
    replaced=[]
    content=content.split()
    for word in content:
        replacement=word_in_pos(word,current_attempt)
        if replacement!=None:
            word=answer[current_attempt]
            replaced.append(word)
        else:
            replaced.append(word)
    replaced=" ".join(replaced)
    return replaced

def judge(current_attempt,answers): #this function will judge if the input answer is right.
    option1=raw_input()
    if option1==answers[current_attempt]:
        return True
    else:
        return False
        

blanks=["__1__", "__2__", "__3__", "__4__"]

halo_answers=["The Master Chief","Cortana","Spartan-117","Guardians"]
halo_text='''__1__ often presents a fairly solitary figure in Halo. Even with the presence of his former AI companion, __2__, running and gunning has always been a pretty lonely affair. That is how things have always been for us Halo enthusiasts.As it turned out, __1__, also known as __3__, formed several key friendships in the early days of his training, and together they would evolve into Blue Team, the legendary Spartan-II unit that features in the forthcoming Halo 5: __4__. '''

uncharted_answers=["Naughty Dog","Nathan Drake","Elena Fisher","Victor Sully Sullivan"]
uncharted_text='''Uncharted is a famous action-adventure video game series produced by __1__. The series follows treasure hunter __2__ as he travels around the world to uncover various historical mysteries. The game also created many other characters,like  __1__'s love interest and later wife __3__, __1__'s partner and father figure __4__......'''

zelda_answers=["Nintendo","Link","Princess Zelda","Ganon"]
zelda_text='''The Legend of Zelda is a high-fantasy action-adventure video game series published by __1__. The series centers on __2__, the playable character and chief protagonist. __2__ is often given the task of rescuing __3__ and the kingdom of Hyrule from __4__. The games' plots commonly involve a relic known as the Triforce, a set of three omnipotent golden triangles. The protagonist in each game is usually not the same incarnation of __2__, but a few exceptions exist.'''


def play_game(answers,text):
    print 'You will get 4 guesses about a famous video game'
    count=0
    error_limit=4
    l=len(answers)
    for current_attempt in range(0,l):
        print 'The current paragraph reads as such:'
        print text
        print "What should be substituted in for",blanks[current_attempt],"?"
        while judge(current_attempt,answers)==False:
            count+=1
            if count>=error_limit:
                exit()
            print 'You got it wrong! You have ',str(error_limit-count),' trys left! Please try again'

        text=replace(text,answers,current_attempt)
        print "Correct!"
            

make_choice()
print 'congragulation! You have passed all the quiz'








