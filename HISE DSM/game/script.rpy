# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hise = Character("Ms. Hise")
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

    "I sit down in the seat"

   



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

    menu:

        "I will shake your hand":
            jump tavern

        "I will not shake your hand":
            jump death


    scene merchant shack
    
    show almost brit at right

    show hise smile at left

    brit "Hello traveler, what can I do for you"

    hise "We're lost... yo usee wh're not exactly from here"

    brit "There there, the homesick feeling is one I know all to well"

    brit "So, blue eyes, medium frame, stunning smile... you must be from the north. "

    hise "Well, not exactly"

    hise "We were attacked by someone... and ended up in your world."

    brit "well, im not too acquainted in world to world travel..."

    brit "but a customer is a customer all the same, so i'll se if I have anything for ya."

    "Brit rummages through droors and cabinets."

    brit "I know it's here somewhere."

    brit "hmmm... here we are"

    hise "what is it?"

    brit "Its a scroll I recieved, not too long ago actually."

    "Brit unrolls the scroll"

    brit "I think this could maybe help you guys"

    hise "So... whats it say."

    brit "It reads \"To whom it may concern: \""

    brit "\"Ive been traveling for some time, with beastly opponents challenging me after every turn\" "

    brit "\"Throughout the heavens and earth, I alone am the honored one\""

    brit "\"With eternal power I am renowned\""

    brit "\"This all through the fabrics of the {i} ELDER CODE {/i} \""

    brit "\"located at the Joestar catacombs, it holds unruly amounts of power, capable of controlling ALL REALITIES\""

    brit "Its signed Trevor Packer"

    hise "Ok... sorry but who is that"

    brit "Its "






    label tavern:
    
    label death:

    scene death





    












    



    return