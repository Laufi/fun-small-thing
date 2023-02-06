EnemyMonsterName = "Hachoo"
EnemyMonsterHP = 25
EnemyMonsterMaxHP = 25
EnemyMonsterStrength = 0
EnemyMonsterDamage = 5

PlayerMonsterName = "Morty"
PlayerMonsterHP = 25
PlayerMonsterMaxHP = 25
PlayerMonsterStrength = 0

def PrintStatus():
    global EnemyMonsterName
    global EnemyMonsterHP
    global EnemyMonsterMaxHP
    global PlayerMonsterName
    global PlayerMonsterHP
    global PlayerMonsterMaxHP
    
    print(f"Your {PlayerMonsterName} HP: {PlayerMonsterHP} / {PlayerMonsterMaxHP} \n"
    f"Enemy {EnemyMonsterName} HP: {EnemyMonsterHP} / {EnemyMonsterMaxHP} \n")


def CalculateMove(MoveSelect):
    global EnemyMonsterHP
    global PlayerMonsterStrength

    if PlayerMonsterMoves[MoveSelect]["Type"] == "Subtract":
        TotalAttack = PlayerMonsterMoves[MoveSelect]["Power"] + PlayerMonsterStrength
        EnemyMonsterHP -= TotalAttack
        print(f"Your {PlayerMonsterName} attacks the {EnemyMonsterName} for {TotalAttack} damage! \n"
        f"The enemy {EnemyMonsterName} has {EnemyMonsterHP}/{EnemyMonsterMaxHP} HP! \n")
    
    elif PlayerMonsterMoves[MoveSelect]["Type"] == "Strengthen":
        PowerUp = PlayerMonsterMoves[MoveSelect]["Power"]
        PlayerMonsterStrength += PowerUp
        print(f"Your {PlayerMonsterName} strengthens itself by {PowerUp}! \n"
        f"Your {PlayerMonsterName} now has {PlayerMonsterStrength} strength! \n")

PlayerMonsterMoves = [
    {
     "MoveName": "Attacc",
     "MoveText": "Your boi attacks the enemy boi!",
     "Power": 5,
     "Type": "Subtract"
    },
    {
     "MoveName": "Gain Courage",
     "MoveText": "Your boi increases your own bois strength, boi!",
     "Power": 2,
     "Type": "Strengthen"   
    }
]


print(f"BATTLE START! GO, {PlayerMonsterName} !")

while True:
    PrintStatus()
    PossibleMoves = print(f"Possible Moves: \n"
    f"A - {PlayerMonsterMoves[0]['MoveName']} / {PlayerMonsterMoves[0]['Type']} / {PlayerMonsterMoves[0]['Power']} power \n"
    f"B - {PlayerMonsterMoves[1]['MoveName']} / {PlayerMonsterMoves[1]['Type']} / {PlayerMonsterMoves[1]['Power']} power \n")
    PlayerMove = input("Which Move Do You Pick?")
    PlayerMove = PlayerMove.upper()
    AntiInputBug = 1
    if PlayerMove == "A":
        AntiInputBug = 0
        CalculateMove(0)
    elif PlayerMove == "B":
        AntiInputBug = 0
        CalculateMove(1)
    
    if EnemyMonsterHP <= 0:
        print("You win!")
        break

    if AntiInputBug == 1:
        pass
    elif AntiInputBug == 0:

        PlayerMonsterHP -= EnemyMonsterDamage

        print(f"The enemy {EnemyMonsterName} attacks your {PlayerMonsterName} for {EnemyMonsterDamage}!\n"
        f"Your {PlayerMonsterName} now has {PlayerMonsterHP} / {PlayerMonsterMaxHP} HP!")

    if PlayerMonsterHP <= 0:
        print("You lose!")
        break
