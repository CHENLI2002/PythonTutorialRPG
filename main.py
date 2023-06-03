from classes.game import Person, bcolor

magic = [{"name": "SuperDuperFireBall", "cost": 1, "dmg": 100},
         {"name": "NothingHappens", "cost": 30, "dmg": 0},
         {"name": "HitWithWand", "cost": 0, "dmg": 50}]
player = Person(400, 40, 50, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolor.FAIL + bcolor.BOLD + "Enemy Attacks!" + bcolor.ENDC)

while running:
    print("================================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_dmg(dmg)
        print("You hit the monster with your fragile bare hands, and it did ", str(dmg), " Damage!")
        print("Enemy Remaining HP: " + str(enemy.get_hp()))
    elif index == 1:
        player.choost_spell()
        m_chocie = int(input("Choose your Magic: ")) - 1
        m_dmg = player.generatge_spell_dmg(m_chocie)
        spell = player.get_spell_name(m_chocie)
        cost = player.get_spell_cost(m_chocie)
        c_mp = player.get_mp()

        if cost > c_mp:
            print(bcolor.WARNING, bcolor.BOLD, "You swung your wand and realized that you have no Mana!", bcolor.ENDC)
        else:
            player.reduce_mp(cost)
            enemy.take_dmg(m_dmg)
            print(bcolor.OKBLUE, "You used - ", spell, " - and did ", str(m_dmg), " to the Monster", bcolor.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_dmg(enemy_dmg)

    print("You got the monster mad, and it slap you in the face, dealing ", str(enemy_dmg), " Damage!")

    print("================================")
    print("Your HP: ", str(player.get_hp()))
    print("Your MP: ", str(player.get_mp()))
    print("Enemy HP: ", str(enemy.get_hp()))

    if enemy.get_hp() == 0:
        print(bcolor.BOLD, bcolor.OKGREEN, "You Win!", bcolor.ENDC)
        break
    elif player.get_hp() == 0:
        print(bcolor.FAIL, bcolor.BOLD, "You lost, and the monster teared you open and ate your organs!",bcolor.ENDC)
        break