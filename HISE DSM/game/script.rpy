# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hise = Character("Ms. Hise")
define trav = Character("Traveller")
define u = Character("Anon")
define ducky = Character("Rubber Duck")
define bray = Character("Brayden")
define nick = Character("NICK JOESTAR")
define jojo = Character("Polnareff, Giorno, Kira Yoshikage")
define brit = Character("Brit")


# The game starts here.

label start:

    $ u = renpy.input("Input name")

    $ u = u.strip()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene village

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hise smile

    # These display lines of dialogue.

    hise "Hello [u]."

    hise "Please take your steat."

    "takes seat"

    hise "I have some bad news and good news"

    u "I'll have the bad news"

    hise "Bad news is that you are going to have to retake this class"

    "Bashes her head into the desk"



    # hise "Im gonna take my top off."

    # This ends the game.

    trav "Hey, you're finally awake"

    hise "What happened"

    trav "You were trying to cross the border"

    "Ms. Hise is visably confused"

    trav "You are in Skyrim now"

    "True"

    scene guild 

    show hise smile at right
    
    with fade

    hise "Where are we?"

    show duck at left with dissolve

    ducky "We welcome you humbly, humans."
    ducky "The council shall decide your fate." 





    



    return