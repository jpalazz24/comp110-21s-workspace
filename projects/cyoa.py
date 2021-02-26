"""An interactive adventure program exploring a birthday night out!"""
"""Above and beyond #9: Loop in main allowing you to drink more at pregame, go home, or go to franklin."""
"""Above and beyond #10: Uber function utilizes a list that is appended and randomly selected from.""" 

from random import randint

__author__ = "730242533"

player: str = str()
points: int = 0
PARTYING_FACE: str = str("\U0001F973")
CAKE: str = str("\U0001F382")
UNAMUSED: str = str("\U0001F612")
CHEERS: str = str("\U0001F37B")
SICK: str = str("\U0001F922")
MUSIC: str = str("\U0001F3B6")

def main() -> None:
    """The entrypoint for the program."""
    escape: bool = False
    global points
    greet()
    print("Enough talk, lets get going!")
    print("First things first, are you staying in, pregaming with friends, or hitting up Franklin?")
    entrance: str = str(input("Enter \"staying in\", \"pregame\", or \"franklin\": "))
    if entrance == "staying in":
        print(f"Boringggg {UNAMUSED}")
        gameover()
    elif entrance == "pregame":
        print("\nPregaming is always fun! Lets do it.")
        pregame()
        while points < 10:
            if input(f"\nYou're feeling good {player}, what's next? Enter \"stay\" or \"leave\": ") == "stay":
                print(f"Ok, but don't go too crazy, this is how many drinks you've had: {points}")
                pregame()   
            else:
                points += 10
                escape: bool = True
                if input ("\nGood thinking. Do you want to go home or head to Franklin? Choose \"home\" or \"out\": ") == "home":
                    print("\nAlthough I'm a little sad the night is over, I understand. Your friends will walk you home.")
                else:
                    uber()
        if escape:
            points -= 10
        gameover()
    elif entrance == "franklin":
        points = franklin(points)
        gameover()

def greet() -> None:
    """An introduction where the player can input their name."""
    print(f"Happy birthday! {PARTYING_FACE}{CAKE} Tonight is your big night.")
    print("With COVID being a distant memory, you can finally celebrate in style!\n")
    global player
    player = str(input("To get the night started, please enter your name: "))
    print(f"\nPleasure to meet you, {player}. Tonight is a celebration of you, so the drinks will be flowing!")
    print("To help you survive the night, we'll be keeping track of how many drinks you have.")
    print("Don't go too crazy though, or your birthday will be quite forgettable, literally.\n")

def gameover() -> None:
    """Function to return game over message."""
    print(f"\nGame over. \nDrinks consumed: {points}")

def franklin(drinks: int) -> int:
    """Let's go to the bars and return the number of drinks to the global variable afterwards."""
    print(f"\nGreat choice {player}! We're heading to MAW.")
    print("You and a group of friends sit down and all order a drink.")
    print("To your surprise, when the drinks arive, the restaurant also gave you a free birthday shot!\n")
    drinks += 2
    print(f"Cheers! {CHEERS} \nDrinks consumed: {drinks}\n")
    print("The night continues and your friend challenges you a game of odds out of 3 for another two shots.")
    print("Pick a number 1-3 and if it's the same as you friend, you have to take another two shots!\n")
    odds: int = int(input("Enter your number: "))
    friend_odds: int = randint(1, 3)
    if odds == friend_odds:
        drinks += 2
        print(f"\nYou picked the same number! Two more drinks. {CHEERS} \nDrinks consumed: {drinks}\n")
    else:
        print(f"\nYou got lucky this time, no more drinks.")
    print("\nYou've had plenty to drink and are feeling great!")
    food: str = str(input("Do you want to order some food to soak up some of the alcohol? \nChoose \"yes\" or \"no\": "))
    if food == "yes":
         drinks -= 1
         print(f"\nYou'll be thankful for this decision tomorrow. \nDrinks consumed: {drinks}")
    else:
        print("\nAlthough I wouldn't recommend, I understand.")
    print(f"\nHope you had a great birthday dinner, {player}, but unfortunately MAW is closing and it's time to go home.")
    return drinks

def pregame() -> None:
    """It's time to pregame the night out while directly reassigning the global points variable."""
    game: str = str(input(f"\nAlright {player}, what game should we play? Enter \"beer pong\" or \"stack cup\": "))
    global points
    if game == "beer pong":
        points += 1
        if points >= 10:
             print(f"\nUh oh, you had one too many and ended the night on the toilet {SICK}.")
        else: 
            print("\nWho doesn't love beer pong? You and your partner dominated, so you only had to drink once.")
            print(f"Drinks consumed: {points}")  
    else: 
        points += 3
        if points >= 10:
             print(f"\nUh oh, you had one too many and ended the night on the toilet {SICK}.")
        else: 
            print("\nStack cup was fun, but you didn't bring your A-game so you had to drink a lot.")
            print(f"Drinks consumed: {points}")
        
def uber() -> None:
    """A program simulating an uber ride where a list function is used."""
    print(f"\nI like the way you think, {player}. Time to call an uber!")
    print(f"Your uber arrived and, because it's your birthday, you are able to add a song to the driver's playlist! {MUSIC}")
    playlist: list[str]
    playlist = ["Eye of the Tiger", "Bohemian Rhapsody", "Don't Stop Believin\'", "Livin\' on a Prayer"]
    your_song: str = str(input("\nEnter a song to be added to the playlist: "))
    playlist.append(your_song)
    song_choice: int = randint(0,4)
    print(f"\nThe playlist is shuffled and {playlist[song_choice]} is played!")
    print(f"Unfortunately, one of your friends feels the music a little bit too much and throws up in the uber {SICK}.")
    print("You all get kicked out and are forced to walk home.")

if __name__ == "__main__":
    main()
