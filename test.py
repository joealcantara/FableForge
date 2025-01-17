import random
import time

world = {
    "player_influence" : 50,
    "tension" : 5,
    "ai_influence": 50
}

def playerTurn():
    decision = rollDice(20)
    if decision < 5:
        world["player_influence"] += 1
        world["ai_influence"] -= 1
        print("Player Gains Influence")
    elif decision < 15:
        world["tension"] += 1
        print("Tension Increases")
    else:
        world["player_influence"] -= 1
        world["ai_influence"] += 1
        print("AI gains Influence")

def AITurn():
    decision = rollDice(20)
    if decision < 5:
        world["player_influence"] += 1
        world["ai_influence"] -= 1
        print("Player Gains Influence")
    elif decision < 15:
        world["tension"] -= 1
        print("Tension Decreases")
    else:
        world["player_influence"] -= 1
        world["ai_influence"] +=1
        print("AI gains Influence")


running = True
count = 0

while running:
    if count < 60:
        count += 1
        print('Player Turn: ' + str(count))
        playerTurn()
        time.sleep(1)
        print('AI Turn: ' + str(count))
        AITurn()
        time.sleep(1)

    else:
        running = False
        print("Player Influence = " + str(world['player_influence']))
        print("World Tension = " + str(world['tension']))
        print("AI Influence = " + str(world['ai_influence']))
        print('simulation ends')
