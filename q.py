from Character import Character
from Weapon import Weapon
import time

PRINT_LEVEL = 0

def w(level, s):
    if (level <= PRINT_LEVEL):
        print(s)

def run_sim():
    bob = Character('bob', stamina=20, strength=5, dexterity=5)
    jim = Character('jim', stamina=5, strength=20, dexterity=5)

    bob.weapon = Weapon(10, 15, '1h sword')
    jim.weapon = Weapon(15, 25, '2h sword')

    rounds = 0

    while(jim.hp_current > 0 and bob.hp_current > 0):

        rounds += 1

        w(2,f"Round #{rounds}:")

        w(2,"{} {}/{}".format(bob.name, bob.hp_current, bob.hp_max()))
        w(2,"{} {}/{}".format(jim.name, jim.hp_current, jim.hp_max()))

        if bob.hits(jim):
            bob_damage = bob.weapon.roll_weapon_damage(bob.strength)
            jim.hp_current -= bob_damage
            w(2,"{} hits {} for {} damage".format(bob.name, jim.name, bob_damage))
        else:
            w(2,"{} missed {}".format(bob.name, jim.name))

        if jim.hits(bob):
            jim_damage = jim.weapon.roll_weapon_damage(jim.strength)
            bob.hp_current -= jim_damage
            w(2,"{} hits {} for {} damage".format(jim.name, bob.name, jim_damage))
        else:
            w(2,"{} missed {}".format(jim.name, bob.name))

    w(2,f"Rounds #{rounds}:")
    w(2,"{} {}/{}".format(bob.name, bob.hp_current, bob.hp_max()))
    w(2,"{} {}/{}".format(jim.name, jim.hp_current, jim.hp_max()))

    if bob.hp_current <= 0 and jim.hp_current <= 0:
        w(2,"Both characters died")
        return 0
    elif(bob.hp_current <= 0):
        w(2,"{} is dead".format(bob.name))
        return -1
    else:
        w(2,"{} is dead".format(jim.name))
        return 1

def run_sim_profile(iterations = 100):
    bob_wins = 0
    jim_wins = 0
    ties = 0

    for i in range(0, iterations):
        result = run_sim()
        if result == 1:
            bob_wins += 1
            w(1, "Bob wins")
        elif result == -1:
            jim_wins += 1
            w(1, "Jim wins")
        else:
            ties += 1
            w(1, "Tie")

    total_sims = bob_wins + jim_wins + ties
    w(0, "Simulations: {}".format(total_sims))
    w(0, "Bob wins: {}".format(bob_wins))
    w(0, "Jim wins: {}".format(jim_wins))
    w(0, "Ties: {}".format(ties))

def main():
    start_time = time.time()
    run_sim_profile(10000)
    end_time = time.time()
    w(0, "Runtime: {}".format(round(end_time - start_time,3)))

if __name__ == '__main__':
    main()


