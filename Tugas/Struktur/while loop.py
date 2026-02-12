Loop = True
while Loop:
    print("Anda sedang berada dalam infinite loop")
    choice = input("Apakah anda ingin keluar? (y/n) : ")
    if choice == "y":
        Loop = False
    elif choice == "n":
        print("...")