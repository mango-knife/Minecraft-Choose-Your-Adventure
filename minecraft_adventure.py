import time
import pygame
import sys

try:
    import questionary
except ImportError:
    print("The 'questionary' library is required. Please install it using the instructions below.")
    print("If you do not have pip, install it with:")
    print("  sudo apt update && sudo apt install python3-pip")
    print("Then install questionary with:")
    print("  pip3 install questionary")
    sys.exit(1)

def typewriter(text, delay=0.003):
    import sys
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def loading_screen():
    typewriter("LOADING...")
    for percent in [10, 20, 30, 50, 65, 85, 99]:
        typewriter(f"{percent}%")
        time.sleep(0.1)
    typewriter("DONE!")

def game_over(message):
    typewriter(message)
    sys.exit()

def intro():
    typewriter("Hello, and welcome to Minecraft Survival Mode: Choose Your Own Adventure!")
    start = questionary.confirm("Would you like to get started?").ask()
    if start:
        loading_screen()
    else:
        sys.exit()

def fall_sequence():
    typewriter("You find yourself falling. Just... falling. You wonder why, but oddly, you don't panic. In fact, you can't remember ever feeling so calm. Or anything else, for that matter.")
    choice = questionary.select(
        "What do you do?",
        choices=[
            "Look around.",
            "Examine yourself.",
            "Convince yourself it's a dream and try to wake up."
        ]).ask()
    if choice == "Look around.":
        typewriter("You glance around and see clouds—blocky, pixelated clouds. That's definitely not normal.")
    elif choice == "Examine yourself.":
        typewriter("You look at your hands. They're rectangles. Your feet, your torso—everything is blocky. This is weird.")
    else:
        game_over("You squeeze your eyes shut, willing yourself to wake up. Suddenly, you sit bolt upright in bed. Was it all a dream? (You win? Try again and pick something else!)")

def landing_sequence():
    typewriter("You fall faster, bursting through the clouds. Below, you spot a huge blue patch beside a sprawling green field.")
    choice = questionary.select(
        "Where do you aim?",
        choices=["The blue area.", "The green area."]
    ).ask()
    if choice == "The blue area.":
        typewriter("You angle your body toward the blue. Splash! You hit water, and the impact stings, but you're alive. Good call.")
    else:
        game_over("You aim for the green, but the ground rushes up and everything goes black. At least it was quick. Game over.")

def tool_choice():
    typewriter("You drag yourself out of the water, soaked and shivering. You remember a trick your grandma taught you: grab some long grass, find two trees, and make a makeshift clothesline. You hang your clothes to dry and turn your attention to survival. You'll need tools.")
    choice = questionary.select(
        "What tool do you craft first?",
        choices=["Axe (for wood)", "Sword (for defense)", "Hoe (for farming)"]
    ).ask()
    if choice == "Axe (for wood)":
        game_over("You try to chop a tree, but realize you need an axe to get wood for an axe. In frustration, you punch the tree. It gives a little, so you keep punching until you have a block of wood. Night falls quickly. Suddenly—SSSS... BOOM! A creeper. Game over.")
    elif choice == "Sword (for defense)":
        typewriter("You decide safety comes first. You punch a tree, collect wood, and fashion a crafting table. You make sticks, then a wooden sword. As night fades, you feel a bit safer.")
    else:
        game_over("You try to make a hoe for farming, but night falls before you finish. An arrow whizzes past—skeleton! Game over.")

def farming_sequence():
    choice = questionary.select(
        "What do you do next?",
        choices=["Craft a hoe and start farming.", "Go back to the forest for more wood."]
    ).ask()
    if choice == "Craft a hoe and start farming.":
        typewriter("You use your wood to craft a hoe, gather seeds from tall grass, and plant them by the water. You feel a small sense of accomplishment.")
    else:
        game_over("You head into the forest, but hunger overtakes you. You collapse. Game over.")

def shelter_sequence():
    choice = questionary.select(
        "Do you build a shelter?",
        choices=["Yes, build a shelter.", "No, relax for a bit."]
    ).ask()
    if choice == "No, relax for a bit.":
        typewriter("You lie down to rest. When you wake, it's nearly night, but your crops are ready. You harvest wheat and bake bread. Suddenly, you spot a figure with a big nose approaching. You quickly put on your clothes.")
    else:
        game_over("You head into the woods for supplies, but collapse from hunger before you get far. Game over.")

def villager_encounter():
    choice = questionary.select(
        "How do you react to the approaching figure?",
        choices=["Prepare to defend yourself.", "Wait and see—maybe it's friendly?"]
    ).ask()
    if choice == "Wait and see—maybe it's friendly?":
        typewriter("The figure introduces himself as Villager #37. He saw you fall from the sky and offers to help. He gestures for you to follow.")
    else:
        game_over("You swing your sword at the stranger. Suddenly, you hear a hiss behind you—creeper! You're blasted into the air. Game over.")

def trust_villager():
    choice = questionary.select(
        "Do you trust the villager?",
        choices=["Yes, follow him.", "No, keep your distance."]
    ).ask()
    if choice == "Yes, follow him.":
        typewriter("You follow Villager #37 to his village. He offers you a spare bed and some bread. As you settle in, you notice a slip of paper sticking out of a loaf.")
    else:
        game_over("You hand the bread back to the villager and keep your distance. Life is peaceful, but uneventful. You never learn the secrets of this world. Game over.")

def paper_sequence():
    choice = questionary.select(
        "What do you do with the paper?",
        choices=["Read it yourself.", "Show it to the villager."]
    ).ask()
    if choice == "Read it yourself.":
        game_over("You pull out the paper and start reading. The villager catches you and his face darkens. 'You shouldn't have done that,' he whispers. Game over.")
    else:
        typewriter("You hand the paper to the villager. He nods solemnly and tells you it's a wanted poster for the Ender Dragon. The reward? 100,000,000🜚. He offers to help you on your quest.")

def ask_villager_for_help():
    choice = questionary.select(
        "Do you accept the villager's help?",
        choices=["Yes, I need all the help I can get.", "No, I'll go alone."]
    ).ask()
    if choice == "Yes, I need all the help I can get.":
        typewriter("The villager gives you a map and explains that the Ender Dragon lives in a place called 'The End.' To get there, you'll need to find a portal and craft Eyes of Ender.")
    else:
        game_over("You set out alone, but are quickly overwhelmed by monsters. Game over.")

def ender_pearl_sequence():
    typewriter("You gather resources and build a shelter for the night. Suddenly, a tall, shadowy figure appears. You look it in the eyes. It charges! You swing your sword. The creature vanishes, leaving behind a strange black pearl.")
    choice = questionary.select(
        "Do you keep the pearl?",
        choices=["Yes, it might be useful.", "No, leave it."]
    ).ask()
    if choice == "Yes, it might be useful.":
        typewriter("You pocket the pearl, wondering what it might do.")
    else:
        game_over("You leave the pearl behind. Without it, you never discover the secret to reaching The End. Game over.")

def villager_explains_ender_eyes():
    typewriter("You return to the village and show the pearl to Villager #37. He explains it's an Ender Pearl, and you'll need Blaze Powder from the Nether to craft Eyes of Ender. To reach the Nether, you'll need obsidian for a portal and a flint and steel to light it.")
    typewriter("You mine, upgrade your tools, and finally craft a diamond pickaxe. You find lava, pour water over it, and collect obsidian. Soon, a swirling purple portal stands before you.")
    choice = questionary.select(
        "Do you enter the Nether?",
        choices=["Yes, step through.", "No, stay here."]
    ).ask()
    if choice == "Yes, step through.":
        typewriter("You step into the portal and emerge in a world of fire and brimstone. Piglins eye you hungrily. You spot a fortress in the distance.")
    else:
        game_over("You stay behind, but the adventure passes you by. Game over.")

def nether_fortress_sequence():
    typewriter("You sneak past Piglins and make your way to the fortress. Inside, you battle Blazes and finally collect enough Blaze Rods. You return to the Overworld, combine Blaze Powder with your Ender Pearl, and craft Eyes of Ender.")
    typewriter("You toss an Eye of Ender into the air. It floats east. You follow, braving forests, mountains, and oceans, until you find a hidden stronghold.")
    typewriter("Deep underground, you find the End Portal. You place the Eyes of Ender into the frame. The portal roars to life.")
    choice = questionary.select(
        "Do you enter The End?",
        choices=["Yes, face the Ender Dragon!", "No, not yet."]
    ).ask()
    if choice == "Yes, face the Ender Dragon!":
        typewriter("You leap into the portal and land on a floating island. The Ender Dragon circles above. You fight bravely, dodging fireballs and destroying crystals. With a final swing, you defeat the dragon. The world is saved!")
        typewriter("Congratulations! You've completed Minecraft Survival Mode: Choose Your Own Adventure.")
    else:
        game_over("You hesitate, and the portal closes. The adventure ends here. Game over.")

def main():
    intro()
    fall_sequence()
    landing_sequence()
    tool_choice()
    farming_sequence()
    shelter_sequence()
    villager_encounter()
    trust_villager()
    paper_sequence()
    ask_villager_for_help()
    ender_pearl_sequence()
    villager_explains_ender_eyes()
    nether_fortress_sequence()

if __name__ == "__main__":
    main()

