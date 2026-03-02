name = input("What's ypur name? ")

match name:
    case "Harry" | "Marto":
        print("Gryffindor")
    case "Darin":
        print("Slitheryn")
    case _:
        print("Who?")