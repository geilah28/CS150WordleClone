from struct import pack
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.colors import GREEN, GRAY, ORANGE 
import random

class WordleClone(toga.App):

    guesses=0
    game_over=False
    
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        #Get word guess
        prefix=self.paths.app
        prefix=prefix.__str__()
        file= prefix + '\words.txt'
        
        with open(file) as f:
            lines=[line.rstrip() for line in f]

        self.wordguess=random.choice(lines)

        #Put Guess input box
        name_label = toga.Label(
            'Guess: ',
            style=Pack(padding=(0, 5))
        )
        self.guess_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(
            style=Pack(direction=ROW, padding=5)
        )
        name_box.add(name_label)
        name_box.add(self.guess_input)

        #Add Guess button
        buttonguess = toga.Button(
            'Guess',
            on_press=self.guess,
            style=Pack(padding=5)
        )

        #Add alphabet label box
        alphabet_label = toga.Label(
            'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z', 
            style=Pack(padding=(0, 60),flex=1, alignment="center")
        )
        alphabet_box = toga.Box(style=Pack(direction=COLUMN, alignment="center"))
        alphabet_box.add(alphabet_label)

        #Add box for guess 1
        self.button1a = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button1b = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button1c = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button1d = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button1e = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))

        guess_box1 = toga.Box(style=Pack(direction=ROW, padding=(0, 185)))

        #Add box for guess 2
        self.button2a = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button2b = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button2c = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button2d = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button2e = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))

        guess_box2 = toga.Box(style=Pack(direction=ROW, padding=(0, 185)))

        #Add box for guess 3
        self.button3a = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button3b = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button3c = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button3d = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button3e = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))

        guess_box3 = toga.Box(style=Pack(direction=ROW, padding=(0, 185)))

        #Add box for guess 4
        self.button4a = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button4b = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button4c = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button4d = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button4e = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))

        guess_box4 = toga.Box(style=Pack(direction=ROW, padding=(0, 185)))

        #Add box for guess 5
        self.button5a = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button5b = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button5c = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button5d = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button5e = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))

        guess_box5 = toga.Box(style=Pack(direction=ROW, padding=(0, 185)))

        #Add box for guess 6
        self.button6a = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button6b = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button6c = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button6d = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))
        self.button6e = toga.Button('', style=Pack(padding=(1,1), width=50, height=50))

        guess_box6 = toga.Box(style=Pack(direction=ROW, padding=(0, 185)))

        guess_box1.add(self.button1a)
        guess_box1.add(self.button1b)
        guess_box1.add(self.button1c)
        guess_box1.add(self.button1d)
        guess_box1.add(self.button1e)

        guess_box2.add(self.button2a)
        guess_box2.add(self.button2b)
        guess_box2.add(self.button2c)
        guess_box2.add(self.button2d)
        guess_box2.add(self.button2e)

        guess_box3.add(self.button3a)
        guess_box3.add(self.button3b)
        guess_box3.add(self.button3c)
        guess_box3.add(self.button3d)
        guess_box3.add(self.button3e)

        guess_box4.add(self.button4a)
        guess_box4.add(self.button4b)
        guess_box4.add(self.button4c)
        guess_box4.add(self.button4d)
        guess_box4.add(self.button4e)

        guess_box5.add(self.button5a)
        guess_box5.add(self.button5b)
        guess_box5.add(self.button5c)
        guess_box5.add(self.button5d)
        guess_box5.add(self.button5e)

        guess_box6.add(self.button6a)
        guess_box6.add(self.button6b)
        guess_box6.add(self.button6c)
        guess_box6.add(self.button6d)
        guess_box6.add(self.button6e)

        #Add restart button
        buttonrestart = toga.Button(
            'Restart',
            on_press=self.restart,
            style=Pack(padding=5)
        )
        #put on main box
        main_box.add(name_box)
        main_box.add(buttonguess)
        main_box.add(alphabet_box)
        main_box.add(guess_box1)
        main_box.add(guess_box2)
        main_box.add(guess_box3)
        main_box.add(guess_box4)
        main_box.add(guess_box5)
        main_box.add(guess_box6)
        main_box.add(buttonrestart)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def dispbox1(self,word):
        #Responsible for updating the first guess buttons

        self.button1a.label = word[0].upper()
        self.button1b.label = word[1].upper()
        self.button1c.label = word[2].upper()
        self.button1d.label = word[3].upper()
        self.button1e.label = word[4].upper()

        wordguesslist= [x for x in self.wordguess]
        guesslist= [x for x in word]
    
        result=[0]*len(self.wordguess)
        for a, b in enumerate(guesslist):
            if wordguesslist[a] == b:
                wordguesslist[a]=""
                result[a]=2
        for a, b in enumerate(guesslist):
            if result[a]==2:
                continue
            for c, d in enumerate(wordguesslist):
                if b==d:
                    wordguesslist[c]=""
                    result[a]=1
        
        if (result[0]==2):
            self.button1a.style.update(background_color=GREEN)
        elif (result[0]==1):
            self.button1a.style.update(background_color=ORANGE)
        else:
            self.button1a.style.update(background_color=GRAY)
        
        if (result[1]==2):
            self.button1b.style.update(background_color=GREEN)
        elif (result[1]==1):
            self.button1b.style.update(background_color=ORANGE)
        else:
            self.button1b.style.update(background_color=GRAY)
        
        if (result[2]==2):
            self.button1c.style.update(background_color=GREEN)
        elif (result[2]==1):
            self.button1c.style.update(background_color=ORANGE)
        else:
            self.button1c.style.update(background_color=GRAY)

        if (result[3]==2):
            self.button1d.style.update(background_color=GREEN)
        elif (result[3]==1):
            self.button1d.style.update(background_color=ORANGE)
        else:
            self.button1d.style.update(background_color=GRAY)
        
        if (result[4]==2):
            self.button1e.style.update(background_color=GREEN)
        elif (result[4]==1):
            self.button1e.style.update(background_color=ORANGE)
        else:
            self.button1e.style.update(background_color=GRAY)

    def dispbox2(self,word):
        #Responsible for updating the second guess buttons

        self.button2a.label = word[0].upper()
        self.button2b.label = word[1].upper()
        self.button2c.label = word[2].upper()
        self.button2d.label = word[3].upper()
        self.button2e.label = word[4].upper()
    
        wordguesslist= [x for x in self.wordguess]
        guesslist= [x for x in word]
    
        result=[0]*len(self.wordguess)
        for a, b in enumerate(guesslist):
            if wordguesslist[a] == b:
                wordguesslist[a]=""
                result[a]=2
        for a, b in enumerate(guesslist):
            if result[a]==2:
                continue
            for c, d in enumerate(wordguesslist):
                if b==d:
                    wordguesslist[c]=""
                    result[a]=1
        
        if (result[0]==2):
            self.button2a.style.update(background_color=GREEN)
        elif (result[0]==1):
            self.button2a.style.update(background_color=ORANGE)
        else:
            self.button2a.style.update(background_color=GRAY)
        
        if (result[1]==2):
            self.button2b.style.update(background_color=GREEN)
        elif (result[1]==1):
            self.button2b.style.update(background_color=ORANGE)
        else:
            self.button2b.style.update(background_color=GRAY)
        
        if (result[2]==2):
            self.button2c.style.update(background_color=GREEN)
        elif (result[2]==1):
            self.button2c.style.update(background_color=ORANGE)
        else:
            self.button2c.style.update(background_color=GRAY)

        if (result[3]==2):
            self.button2d.style.update(background_color=GREEN)
        elif (result[3]==1):
            self.button2d.style.update(background_color=ORANGE)
        else:
            self.button2d.style.update(background_color=GRAY)
        
        if (result[4]==2):
            self.button2e.style.update(background_color=GREEN)
        elif (result[4]==1):
            self.button2e.style.update(background_color=ORANGE)
        else:
            self.button2e.style.update(background_color=GRAY)

    def dispbox3(self,word):
        #Responsible for updating the third guess buttons

        self.button3a.label = word[0].upper()
        self.button3b.label = word[1].upper()
        self.button3c.label = word[2].upper()
        self.button3d.label = word[3].upper()
        self.button3e.label = word[4].upper()

        wordguesslist= [x for x in self.wordguess]
        guesslist= [x for x in word]
    
        result=[0]*len(self.wordguess)
        for a, b in enumerate(guesslist):
            if wordguesslist[a] == b:
                wordguesslist[a]=""
                result[a]=2
        for a, b in enumerate(guesslist):
            if result[a]==2:
                continue
            for c, d in enumerate(wordguesslist):
                if b==d:
                    wordguesslist[c]=""
                    result[a]=1
        
        if (result[0]==2):
            self.button3a.style.update(background_color=GREEN)
        elif (result[0]==1):
            self.button3a.style.update(background_color=ORANGE)
        else:
            self.button3a.style.update(background_color=GRAY)
        
        if (result[1]==2):
            self.button3b.style.update(background_color=GREEN)
        elif (result[1]==1):
            self.button3b.style.update(background_color=ORANGE)
        else:
            self.button3b.style.update(background_color=GRAY)
        
        if (result[2]==2):
            self.button3c.style.update(background_color=GREEN)
        elif (result[2]==1):
            self.button3c.style.update(background_color=ORANGE)
        else:
            self.button3c.style.update(background_color=GRAY)

        if (result[3]==2):
            self.button3d.style.update(background_color=GREEN)
        elif (result[3]==1):
            self.button3d.style.update(background_color=ORANGE)
        else:
            self.button3d.style.update(background_color=GRAY)
        
        if (result[4]==2):
            self.button3e.style.update(background_color=GREEN)
        elif (result[4]==1):
            self.button3e.style.update(background_color=ORANGE)
        else:
            self.button3e.style.update(background_color=GRAY)

    def dispbox4(self,word):
        #Responsible for updating the fourth guess buttons

        self.button4a.label = word[0].upper()
        self.button4b.label = word[1].upper()
        self.button4c.label = word[2].upper()
        self.button4d.label = word[3].upper()
        self.button4e.label = word[4].upper()
    
        wordguesslist= [x for x in self.wordguess]
        guesslist= [x for x in word]
    
        result=[0]*len(self.wordguess)
        for a, b in enumerate(guesslist):
            if wordguesslist[a] == b:
                wordguesslist[a]=""
                result[a]=2
        for a, b in enumerate(guesslist):
            if result[a]==2:
                continue
            for c, d in enumerate(wordguesslist):
                if b==d:
                    wordguesslist[c]=""
                    result[a]=1
        
        if (result[0]==2):
            self.button4a.style.update(background_color=GREEN)
        elif (result[0]==1):
            self.button4a.style.update(background_color=ORANGE)
        else:
            self.button4a.style.update(background_color=GRAY)
        
        if (result[1]==2):
            self.button4b.style.update(background_color=GREEN)
        elif (result[1]==1):
            self.button4b.style.update(background_color=ORANGE)
        else:
            self.button4b.style.update(background_color=GRAY)
        
        if (result[2]==2):
            self.button4c.style.update(background_color=GREEN)
        elif (result[2]==1):
            self.button4c.style.update(background_color=ORANGE)
        else:
            self.button4c.style.update(background_color=GRAY)

        if (result[3]==2):
            self.button4d.style.update(background_color=GREEN)
        elif (result[3]==1):
            self.button4d.style.update(background_color=ORANGE)
        else:
            self.button4d.style.update(background_color=GRAY)
        
        if (result[4]==2):
            self.button4e.style.update(background_color=GREEN)
        elif (result[4]==1):
            self.button4e.style.update(background_color=ORANGE)
        else:
            self.button4e.style.update(background_color=GRAY)
            
    def dispbox5(self,word):
        #Responsible for updating the fifth guess buttons

        self.button5a.label = word[0].upper()
        self.button5b.label = word[1].upper()
        self.button5c.label = word[2].upper()
        self.button5d.label = word[3].upper()
        self.button5e.label = word[4].upper()

        wordguesslist= [x for x in self.wordguess]
        guesslist= [x for x in word]
    
        result=[0]*len(self.wordguess)
        for a, b in enumerate(guesslist):
            if wordguesslist[a] == b:
                wordguesslist[a]=""
                result[a]=2
        for a, b in enumerate(guesslist):
            if result[a]==2:
                continue
            for c, d in enumerate(wordguesslist):
                if b==d:
                    wordguesslist[c]=""
                    result[a]=1
        
        if (result[0]==2):
            self.button5a.style.update(background_color=GREEN)
        elif (result[0]==1):
            self.button5a.style.update(background_color=ORANGE)
        else:
            self.button5a.style.update(background_color=GRAY)
        
        if (result[1]==2):
            self.button5b.style.update(background_color=GREEN)
        elif (result[1]==1):
            self.button5b.style.update(background_color=ORANGE)
        else:
            self.button5b.style.update(background_color=GRAY)
        
        if (result[2]==2):
            self.button5c.style.update(background_color=GREEN)
        elif (result[2]==1):
            self.button5c.style.update(background_color=ORANGE)
        else:
            self.button5c.style.update(background_color=GRAY)

        if (result[3]==2):
            self.button5d.style.update(background_color=GREEN)
        elif (result[3]==1):
            self.button5d.style.update(background_color=ORANGE)
        else:
            self.button5d.style.update(background_color=GRAY)
        
        if (result[4]==2):
            self.button5e.style.update(background_color=GREEN)
        elif (result[4]==1):
            self.button5e.style.update(background_color=ORANGE)
        else:
            self.button5e.style.update(background_color=GRAY)

    def dispbox6(self,word):
        #Responsible for updating the sixth guess buttons

        self.button6a.label = word[0].upper()
        self.button6b.label = word[1].upper()
        self.button6c.label = word[2].upper()
        self.button6d.label = word[3].upper()
        self.button6e.label = word[4].upper()

        wordguesslist= [x for x in self.wordguess]
        guesslist= [x for x in word]
    
        result=[0]*len(self.wordguess)
        for a, b in enumerate(guesslist):
            if wordguesslist[a] == b:
                wordguesslist[a]=""
                result[a]=2
        for a, b in enumerate(guesslist):
            if result[a]==2:
                continue
            for c, d in enumerate(wordguesslist):
                if b==d:
                    wordguesslist[c]=""
                    result[a]=1
        
        if (result[0]==2):
            self.button6a.style.update(background_color=GREEN)
        elif (result[0]==1):
            self.button6a.style.update(background_color=ORANGE)
        else:
            self.button6a.style.update(background_color=GRAY)
        
        if (result[1]==2):
            self.button6b.style.update(background_color=GREEN)
        elif (result[1]==1):
            self.button6b.style.update(background_color=ORANGE)
        else:
            self.button6b.style.update(background_color=GRAY)
        
        if (result[2]==2):
            self.button6c.style.update(background_color=GREEN)
        elif (result[2]==1):
            self.button6c.style.update(background_color=ORANGE)
        else:
            self.button6c.style.update(background_color=GRAY)

        if (result[3]==2):
            self.button6d.style.update(background_color=GREEN)
        elif (result[3]==1):
            self.button6d.style.update(background_color=ORANGE)
        else:
            self.button6d.style.update(background_color=GRAY)
        
        if (result[4]==2):
            self.button6e.style.update(background_color=GREEN)
        elif (result[4]==1):
            self.button6e.style.update(background_color=ORANGE)
        else:
            self.button6e.style.update(background_color=GRAY)

    def guess(self,widget):
        #print(self.wordguess)
        
        #Open allowed guesses txt file
        prefix=self.paths.app
        prefix=prefix.__str__()
        file= prefix + '\guesses.txt'
        with open(file,'r') as f:
            lines=[line.rstrip() for line in f]
            
        if (self.game_over==True):
            #If game-over, do nothing
            self.guess_input.clear()
            self.main_window.info_dialog('Game over','Game over! Restart the game to retry')
            return
        
        word=self.guess_input.value
        if (self.guess_input.value==""):
            #Check if guess input is empty
            self.guess_input.clear()
            self.main_window.error_dialog('Error!','Please type in a word')
            return
        
        if (self.guess_input.value.isalpha()==False):
            #Check if it contains non-alphabet characters
            self.guess_input.clear()
            self.main_window.error_dialog('Error!','Contains non-Alphabet characters')
            return

        if (len(self.guess_input.value)<5):
            #Check if less than five characters 
            self.guess_input.clear()
            self.main_window.error_dialog('Error!','Less than Five Characters')
            return

        if (len(self.guess_input.value)>5):
            #Check if more than five characters 
            self.guess_input.clear()
            self.main_window.error_dialog('Error!','More than Five Characters')
            return

        if (word.lower() not in lines):
            #Check if in allowed guesses
            self.guess_input.clear()
            self.main_window.error_dialog('Error!','Word not in dictionary')
            return

        self.guesses+=1
        if self.guesses==1:
            #first guess
            self.dispbox1(word=self.guess_input.value.lower())
            self.guess_input.clear()
        if self.guesses==2:
            #second guess
            self.dispbox2(word=self.guess_input.value.lower())
            self.guess_input.clear()
        if self.guesses==3:
            #third guess
            self.dispbox3(word=self.guess_input.value.lower())
            self.guess_input.clear()
        if self.guesses==4:
            #fourth guess
            self.dispbox4(word=self.guess_input.value.lower())
            self.guess_input.clear()
        if self.guesses==5:
            #fifth guess
            self.dispbox5(word=self.guess_input.value.lower())
            self.guess_input.clear()
        if self.guesses==6:
            #sixth guess
            self.dispbox6(word=self.guess_input.value.lower())
            self.guess_input.clear()
        
        if (word.lower()==self.wordguess):
            #Check if guess is equal to the word
            self.game_over=True
            self.guess_input.clear()
            self.main_window.info_dialog('Victory!','Congratulations you win the game')
            return
        
        if (self.game_over==False and self.guesses==6):
            #Check if guesses is over 6 and game is failed
            self.guess_input.clear()
            self.main_window.info_dialog('Game over','You fail! The correct answer is ' + self.wordguess)
            self.game_over=True
            return
            
    def restart(self,widget):
        #Restart button

        #Update the letter labels
        self.button1a.label= ''
        self.button1b.label= ''
        self.button1c.label= ''
        self.button1d.label= ''
        self.button1e.label= ''

        self.button1a.style.update(background_color="transparent")
        self.button1b.style.update(background_color="transparent")
        self.button1c.style.update(background_color="transparent")
        self.button1d.style.update(background_color="transparent")
        self.button1e.style.update(background_color="transparent")

        self.button2a.label= ''
        self.button2b.label= ''
        self.button2c.label= ''
        self.button2d.label= ''
        self.button2e.label= ''

        self.button2a.style.update(background_color="transparent")
        self.button2b.style.update(background_color="transparent")
        self.button2c.style.update(background_color="transparent")
        self.button2d.style.update(background_color="transparent")
        self.button2e.style.update(background_color="transparent")

        self.button3a.label= ''
        self.button3b.label= ''
        self.button3c.label= ''
        self.button3d.label= ''
        self.button3e.label= ''

        self.button3a.style.update(background_color="transparent")
        self.button3b.style.update(background_color="transparent")
        self.button3c.style.update(background_color="transparent")
        self.button3d.style.update(background_color="transparent")
        self.button3e.style.update(background_color="transparent")

        self.button4a.label= ''
        self.button4b.label= ''
        self.button4c.label= ''
        self.button4d.label= ''
        self.button4e.label= ''

        self.button4a.style.update(background_color="transparent")
        self.button4b.style.update(background_color="transparent")
        self.button4c.style.update(background_color="transparent")
        self.button4d.style.update(background_color="transparent")
        self.button4e.style.update(background_color="transparent")

        self.button5a.label= ''
        self.button5b.label= ''
        self.button5c.label= ''
        self.button5d.label= ''
        self.button5e.label= ''

        self.button5a.style.update(background_color="transparent")
        self.button5b.style.update(background_color="transparent")
        self.button5c.style.update(background_color="transparent")
        self.button5d.style.update(background_color="transparent")
        self.button5e.style.update(background_color="transparent")

        self.button6a.label= ''
        self.button6b.label= ''
        self.button6c.label= ''
        self.button6d.label= ''
        self.button6e.label= ''

        self.button6a.style.update(background_color="transparent")
        self.button6b.style.update(background_color="transparent")
        self.button6c.style.update(background_color="transparent")
        self.button6d.style.update(background_color="transparent")
        self.button6e.style.update(background_color="transparent")

        #Reset word
        prefix=self.paths.app
        prefix=prefix.__str__()
        file= prefix + '\words.txt'
        with open(file, 'r') as f:
            lines=[line.rstrip() for line in f]
        self.wordguess=random.choice(lines)

        #Reset number of guesses
        self.guesses=0

        #Reset game-over status
        self.game_over=False

def main():
    return WordleClone()
