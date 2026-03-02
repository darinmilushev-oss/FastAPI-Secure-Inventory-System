import random

player_hp = 100
enemy_hp = 100

def player_turn():
    print("\nТвой ход:")
    print("1. Атака")
    print("2. Силен удар (риск)")
    print("3. Лечение")

    choice = input("Избери (1/2/3): ")

    if choice == "1":
        dmg = random.randint(10, 20)
        print(f"Нанасяш {dmg} щети.")
        return dmg, 0

    elif choice == "2":
        if random.random() < 0.5:
            dmg = random.randint(25, 40)
            print(f"💥 Силен удар! {dmg} щети.")
            return dmg, 0
        else:
            self_dmg = random.randint(5, 15)
            print(f"❌ Пропуск. Получаваш {self_dmg} щети.")
            return 0, self_dmg

    elif choice == "3":
        heal = random.randint(15, 25)
        print(f"🩹 Лекуваш се за {heal}.")
        return 0, -heal

    else:
        print("Невалиден избор. Губиш хода.")
        return 0, 0

def enemy_turn():
    action = random.choice(["attack", "attack", "heal"])

    if action == "attack":
        dmg = random.randint(8, 18)
        print(f"Врагът те удря за {dmg}.")
        return dmg, 0
    else:
        heal = random.randint(10, 20)
        print(f"Врагът се лекува за {heal}.")
        return 0, -heal

print("🥊 STREET FIGHT")
print("Победи врага.")

while player_hp > 0 and enemy_hp > 0:
    print(f"\nТи: {player_hp} HP | Враг: {enemy_hp} HP")

    dmg, self_effect = player_turn()
    enemy_hp -= dmg
    player_hp -= self_effect

    if enemy_hp <= 0:
        break

    dmg, self_effect = enemy_turn()
    player_hp -= dmg
    enemy_hp -= self_effect

if player_hp > 0:
    print("\n🏆 Победи!")
else:
    print("\n💀 Загуби.")
