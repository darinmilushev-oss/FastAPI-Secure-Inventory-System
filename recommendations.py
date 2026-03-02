def main():
    def recommend():
        difficulty = input("Difficult or Casual? ").strip().lower()
        player = input("Multiplayer or Single-player? ").strip().lower()

        if difficulty == "difficult":
            if "multiplayer" in player:
                print("Try a challenging multiplayer game with cooperative or competitive modes.")
            else:
                print("Try a difficult single-player game with a deep story or mechanics.")
        else:
            if "multiplayer" in player:
                print("Try a casual multiplayer party or co-op game.")
            else:
                print("Try a relaxing single-player game or puzzle.")

    recommend()            