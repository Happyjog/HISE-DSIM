# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hise = Character("Ms. Hise")
define u = Character("Anon")
define ducky = Character("Rubber Duck")
define bray = Character("Brayden")
define nick = Character("NICK JOESTAR")
define stands = Character("Polnareff, Giorno, Kira Yoshikage")
define brit = Character("Brit")
define john = Character("Jonathan")




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
    hise "Please take your seat."
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
    "Ms. Hise smirks bitterly and looks at the duck."
    ducky "Welcome, to Coderym!"
    "The duck announces with great pride."
    "Ms. Hise smiles at the duck and claps for him."
    hise "Now, Sir Rubber Duck, could you generously tell us what you need us to do now that [u] is up?"
    ducky "Oh... of course. *ahem*, first, I've seen how the woman can program. I need you two to get the Elder Code and change the world."
    "My mouth hangs down off of my chin. This is ridiculous."
    "I look over at Ms. Hise and her eye twitches. It has to be in disbelief."
    hise "Sir... we aren't very familiar with the \"Elden Code\"."
    "The big duck's eyes light up."
    ducky "We have prepared, since we summoned you here and all."
    "Another revelation. These stupid ducks summoned us here?"
    u "Woah, who said we wanted to be summoned?"
    "Ms. Hise pinches my leg."
    hise "*whispering* {i}You're gonna antagonize the rubber ducks? What are you doing? AND they're cute!{/i} Sorry sir, he's still confused."
    "The big dumb duck sighs and clears his throat again."
    ducky "As I was going to explain, we are in a world where the very foundation of Law, Order, and Principle has been fractured."
    ducky "Nick Jojo the Puppetmaster and Braydon the Horrible fractured the Elden Code and took the halves."
    ducky "Your job is to retrieve the Elden Code and restore order to this world once again!"
    ducky "Here is a map to Brit the Wise Shopkeeper's market. Confide with him and retrieve the code!"
    "The duck shoves us out of the tavern and leaves us with nothing but a map to Brit's shop."
    u "That dumb..."
    hise "Okay! It's time to go!"
    "Pointing toward the direction of the shop, she starts striding toward it. She seems awfully enthusiastic huh."
    "And so we start our journey toward a shopkeeper we have never heard of in a land we have never seen before."
    
    #menu:

    #   "I will shake your hand":
    #      jump tavern

    # "I will not shake your hand":
        #    jump death




    




    

    
    

    scene jojo meadow

    show hise smile at left

    with dissolve

        

    hise "Look [u], it seems theres a local... lets go talk to him."

    u "Ok Ms. Hise, but be careful... remember how we got here."

    hise "Right."

    show nick jojo 2 at right

    hise "Hey... can you help us?"

    nick "Hmph... How impudent of you."

    hise "Im sorry, we need directions to a city... or maybe a guide?"

    nick "I dont waste my time with filth like you two."

    nick "I shall teach grime like you a lesson."

    "Nick jojo joestar summons his three puppets "

    show giorno 2 at right

    show polnareff 2 at topleft

    show kira 2 at topright

    nick "My Name is Nick Jojo Joestar, remember as the man who game ended you"

    nick "Now my divine children, rid the land of these parasytes"

    stands "Yes father, we serve you and only you."

        

    "The puppets attack left right and center."

    "Mrs hise and [u] take various blows, one after another"

    u "Ms Hise... what do we do?!?"

    hise "Im at a loss [u], we have to find a weak spot of some sort"

    u "Well you're still my teacher, teach me how to beat him!"

    nick "Ignorant fools, I have no weaknesses."

    nick "My puppets were a gift from the gods, they know no bounds and have no limits."

    "*[u] whispers to Ms Hise*"

    u "Ms Hise, he only mentioned his puppets."

    u "What if directly attack him, and just evade his puppets attacks."

    hise "We can try... its your call though"

    menu:

        "We'll attack Nick jojo directly":
            jump jojosuccess

        "We'll wait for an opening and attack then":
            jump jojodeath







    














    return

label jojosuccess:
    "Nick Jojo retaliates but you are easily able to overpower him. The puppets fall to the ground and cease all movement."
    hise "Quick, look for the shard of the Elden Code!"
    "You pat down Nick Jojo's body and find the shard inside of one of his bags."
    "She offers her open hand in front of her. I give it a smack, high-fiving her."
    scene jojo meadow
    show hise smile at center
    hise "[u], we beat him, all thanks to your quick thinking."

    u "Thanks, let's continue to ."

    # BRIT SCENE

    scene merchant 2
    
    show brit at truecenter

    show hise smile at left

    brit "Hello traveler, what can I do for you"

    hise "We're lost... yo usee whe're not exactly from here"

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

    brit "Its only the most powerful man in all of Coderym."

    brit "Its always been a mystery how that tyrant became ruler, but I guess the secret to his power was sitting in MY shop all along."

    brit "My shop huh?... im pretty awesome arent I?"

    hise "I-"

    "*sighs*"

    hise "I suppose so, but what does that information mean for us?"

    brit "It means you'll go to the deep dark depths of the Joestar catacombs and get that Elder Code."

    hise "Why us... dont you have some powerful ally to so this type of thing?"

    brit "Nope, im just a simple merchant, I can come if ya want"

    hise "If you insis-"

    brit "Of COURSE I'll go... I can show you how to get there and... well I always wanted to go on a grand quest!"

    hise "[u]... are we sure we want to take him with us?"

    u "I think it'll be alright, he probably knows the area better than we do."

    "We march down to the battlefield where Braydon the Horrible awaited us."

    
    scene brayden battle 

    show brit 
    show jon at left
    
    
    with dissolve








    brit "Look, its Braydon's army."

    "You peer over to the organized army and realize who is leading it."

    john "It's Ms. Hise..."

    u "We proceed with the plan as intended."

    brit "This makes no sense how could a person so pure turn evil?"

    john "I know this is a longshot but I think she might be controlled."

    "You take a closer look with binoculars."

    u "Jonathan you are right! Her eyes are glazed over as if she's a zombie."

    brit "Oh no..."

    john "What?"

    brit "Braydon must be using his dark code to control Ms. Hise"

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

    "Brit leaves as you and Jonathan prepare to scout upon a nearby ledge"

    john "This is the time to strike, they are full of beer and food sleeping well"

    u "The guards are barley awake swaying at their posts we take them out first. Next, we take out those in outermost tents working our way in."

    john "And if we get caught?"

    u "We countinue in, more urgently. We will finish what we start"

    john "Ms. Hise..."

    u "Reserve hope, do not cause injure in prayers she returns to normal"

    "Slight time skip to entrance of camp hiding behind some trees"

    "You countinue to the right of the first guard and Jonathan moves to the left of the second guard"

    "After taking the guards out you and Jonathan countinue to the tents"

    "Exiting the umptenth tent with bloody hands you hear a scream. It's Jonathan"

    u "I'm about to come!"

    john "Hel..."

    hide jon

    "His cry for help turns into a gargle as he is dispatched by Ms. Hise, Braydon standing behind her"

    "You go numb, an eternity passes as his body hits the ground"

    #You get a choice to charge Ms. Hise or retreat to a better position I am writing the ending of you retreating

    "You run to the gate as countless soliders come out of tents"

    "Sliding to a stop at the entrance you unsheathe your sword"

    u "Come at me you cowards! No amount of men will rivial my strength!"

    "You swing a mighty greatsword with the strength of ten men. Standing in the wake of your gruesome strokes stand men with half missing"

    "Endless men come to you, spotlighted in moonlight you do nothing but rage against the tide"

    "The first injury came after as a throb, quickly followed by serveral more"

    "They had been there the whole time, just masked through by adrenaline"

    "By the time you finish off the waves of men a wall of flesh seperate you and Ms. Hise"

    u "Braydon, I won't let you win"

    bray "I already have, Ms. Hise has no choice but to kill you under my control"

    "She dashes at you in a frenzied sword storm"

    "You dodge, missing the blunt of the attack, but are too late reacting to the recovery of Ms. Hise"

    "And yet this is exactly what you wanted as you sit on the ground defenseless"

    bray "I TOLD you winning was never acheivable"

    "He walks over to look you in the eye"

    bray "You shall die"

    "You unleashe a hidden dagger and stab Braydon in the heart"

    "We connect the peices. There is a flash of light."

    scene bg classroom

    "I'm sitting down, just as I was before all of the sleeping gas."

    u "Was that real?"

    hise "Yeah, it was real."

    "A moment of silence."

    hise "Let's forget this ever happened, all that matters is that we made it out safe."

    menu:

        "I think we need to live with that Ms. Hise.":
            jump goodending

        "Yeah, I'd like to forget that too. *Glaring*":
            jump badending




    #End of fighting
    

label jojodeath:
    "The puppets slam you to the ground at an incredible speed and knocks you unconcious."
    jump death

label death:
    scene death

    "Done, Finished."

    return



 







    #image of the rune

label badending:
    show hise smile at center
    
    u "How am I just supposed to forget?! I've killed people to stand where I stand today. YOU almost killed me!"

    "Ms. Hise looks up."

    hise "But I didn't."

    "You stare at her dumbfounded until realization hits you."

    "You can't forgive her even if it wasn't her falt, you can't look her in the eye even if its truley hers you are looking into."

    u "I don't want to see you again."

    "You walk to the door until you hear a voice."

    hise "I understand, I hope you won't grow resentful nonetheless."

    "You walk out."

    return

    #End of story


    #happy ending

    #image of the rune

label goodending:
    show hise smile at center
    u "I agree, that brought out the worst in both of us. Even so I see you in a better light despite your mind control."

    "Ms. Hise starts to cry"

    hise "I can't belive you can forgive me."

    u "It's alright, it wasn't really you anyway."

    "You get up to leave."

    hise "I can't thank you enough for being so stoic."

    u "Don't worry about it, I hope to see you soon."

    hise "You too."

    "You walk out of the classroom with your head up high."

    return

    #end of good ending




   