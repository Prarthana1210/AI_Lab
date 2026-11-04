def vacuumcleaner(room_a, room_b):
    position = "A"

    while room_a == "dirty" or room_b == "dirty":

        if position == "A":
            print("Vacuum cleaner is in room A")

            if room_a == "dirty":
                print("Room A is dirty")
                print("Suck")
                room_a = "clean"       

            else:
                print("Room A is clean")
                print("Move Right")
                position = "B"

        else:
            print("Vacuum cleaner is in room B")

            if room_b == "dirty":
                print("Room B is dirty")
                print("Suck")
                room_b = "clean"

            else:
                print("Room B is clean")
                print("Move Left")
                position = "A"

    print("Both rooms are clean")


room_a = "dirty"
room_b = "dirty"

vacuumcleaner(room_a, room_b)
