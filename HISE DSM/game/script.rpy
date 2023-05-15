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
define john = Character("Johnathan")




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

    scene black
    with dissolve
    
    "And with that, I lose consiousness."



    scene guild 

    show hise smile
    
    with fade
    "With heavy eyelids, I open my eyes. My eyes swim awound to scan the room. "

    hise "-how are we going to... [u]!"
    "Ms. Hise looks at me with concern."
    hise "How do you feel?"
    u "I feel... fine."
    "My body seemed to be fine, just sluggish."
    "I look over to my left to see a big yellow figure."

    show hise smile at right with moveoutright

    show duck at left with dissolve

    ducky "Hey, you're finally awake."
    "Wha-"
    u "A... rubber duck?"
    ducky "That's SIR RUBBER DUCK to you!"
    "I really doubt it."
    u "Where is this Ms. Hise?"
    ""
    #menu:

    #   "I will shake your hand":
    #      jump tavern

    # "I will not shake your hand":
        #    jump death


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


    

    scene death
    
    








    














    return

    label death:
    scene death

    "Done, Finished."



    brit "Look, its Braydon's army"

        "You peer over to the organized army and realize who is leading it"

    john "Its Mrs. Heis..."

    u "We proceed with the plan as intended"

    brit "This makes no sense how could a person so good turn evil?"

    john "I know this is a longshot but I think she might be controlled"

    "You take a closer look with binoculars"

    u "Johnathan you are right! Her eyes are glazed over as if she's a zombie"

    brit "Oh no"

    john "What?"

    brit "Braydon must be using his dark code to control Mrs. Heis"

    "All characters set up a camp, cold without fire in fear of being spotted in the upcoming battle"

    "Timeskip to nightime with moon out in the sky"

    brit "As you all know I won't be able to participate in the upcoming battle; however, if I may over some adive"

    "Slight pause as everyone leans in to listen"

    brit "As the moon shines illuminating their camp in such a horrible light, an attack is in order"

    "Brit stands up"

    brit "Braydon has fought yet with only dirty dihonorable tatics, he does so with great success. Attacking at night provides you with free fatalities before a real fight begins giving an advantage to your outnumbered group"

    #Choice to agree or disagree next lines will be agreeable lines

    john "I absolutley agree, we will strike in 5"

    u "Farewell Brit and safe travels"

    "Brit leaves as you and Johnathan prepare to scout upon a nearby ledge"

    john "This is the time to strike, they are full of beer and food sleeping well"

    u "The guards are barley awake swaying at their posts we take them out first. Next, we take out those in outermost tents working our way in."

    john "And if we get caught?"

    u "We countinue in, more urgently. We will finish what we start"

    john "Mrs. Heis..."

    u "Reserve hope, do not cause injure in prayers she returns to normal"

    "Slight time skip to entrance of camp hiding behind some trees"

    "You countinue to the right of the first guard and Johnathan moves to the left of the second guard"

    "After taking the guards out you and Johnathan countinue to the tents"

    "Exiting the umptenth tent with bloody hands you hear a scream. Its Johnathan"

    u "I'm about to come!"

    john "Hel..."

    "His cry for help turns into a gargle as he is dispatched by Mrs. Heis, Braydon standing behind her"

    "You go numb, an eternity passes as his body hits the ground"

    #You get a choice to charge Mrs. Heis or retreat to a better position I am writing the ending of you retreating

    "You run to the gate as countless soliders come out of tents"

    "Sliding to a stop at the entrance you unsheathe your sword"

    u "Come at me you cowards! No amount of men will rivial my strength!"

    "You swing a mighty greatsword with the strength of ten men. Standing in the wake of your gruesome strokes stand men with half missing"

    "Endless men come to you, spotlighted in moonlight you do nothing but rage against the tide"

    "The first injury came after as a throb, quickly followed by serveral more"

    "They had been there the whole time, just masked through by adreniline"

    "By the time you finish off the waves of men a wall of flesh seperate you and Mrs. Heis"

    u "Braydon, I won't let you win"

    bray "I already have, Mrs. Heis has no choice but to kill you under my control"

    "She dashes at you in a frenzied sword storm"

    "You dodge missing the blunt of the attack, but are too late to react the recovery of Mrs. Heis"

    "And yet this is exactly what you wanted as you sit on the ground defenceless"

    bray "I TOLD you winning was never acheivable"

    "He walks over to look you in the eye"

    bray "You shall die"

    "You unleashe a hidden dagger and stab braydon in the heart"

    #End of fighting


     


