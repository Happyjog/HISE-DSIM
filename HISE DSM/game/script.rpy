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



image purptint:
    Solid("#ca1aca")
    alpha 0.3
    additive 1.0


# The game starts here.

label start:

    $ u = renpy.input("Input name")

    $ u = u.strip()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hise smile

    # These display lines of dialogue.

    hise "Hello [u]."
    hise "Please take your steat."
    "I sit down."
    u "What's this about Ms. Hise?"
    "She slips a paper labled unit 9 test my way. It has the number \"46\" written in red at the top."
    hise "[u], I am extremely disappointed with this score. Why don't you put in any effort?"
    "You scowl and sit back in my chair."
    u "What's the point of this anyway? If I wanted to code, I don't need to answer any multiple choice questions that are this tedious."
    "You sit up and point your finger down on her desk."
    u "Besides, I don't think YOU can solve them either."
    "She glares at you, but retains her composure."
    hise "If you wanted to code, you would be able to answer the questions without a problem."
    "She swipes you hand off the desk and looks in your eyes."
    hise "Actually [u], there's something I wanted to show you. It might help you with your habits."
    "She tilts her computer screen as she clicks on an unnamed file."
    u "What is this, your home project? HA!"
    "She runs the code and immediately, the door of the room locks."
    u "What? How did that happen Ms. Hise?"
    "I point at the door, "
    hise "Wait! it might be..."
    "Suddenly, there is a hissing sound coming from above. Purple smoke starts to release from the water sprinklers."
    
    show purptint

    hise "[u], get on the ground and cover your nose and mouth with your shirt."
    "Ms. Hise gets on the ground right next to me and covers her face."
    u "uh... I... will check the door..."
    "I crawl toward the door and see that there was a tiny circular metal sheet covering the keyhole."
    u "What? How intricate are the defense mechanisms in this room Ms. Hise?"
    hise "I didn't even know this existed until today!"
    "I'm light headed now. My vision starts to blur."
    hise "Stay with me [u]! Stay... with... me..."
    "Ms. Hise's vague outline is panicking, but her speech becomes sluggish."
    
    "And with that, I lose consiousness."




   




    # This ends the game.


    scene guild 

    show hise smile at right
    
    with fade

    hise "Where are we?"

    show duck at left with dissolve

    ducky "We welcome you humbly, humans."
    ducky "The council shall decide your fate." 

    #menu:

    #   "I will shake your hand":
    #      jump tavern

    # "I will not shake your hand":
        #    jump death


    #label tavern:
    
    
    












    



    return

    label death:

    scene death

    "Done, Finished."