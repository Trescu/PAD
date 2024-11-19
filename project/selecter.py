import os


def select(opt_one, opt_two, name_one, name_two):
    """
    szimpla kétopciós választó

    paraméterek:
    - opt_one (any): első opció
    - opt_two (any): második opció
    - name_one (any): első opció neve
    - name_two (any): második opció neve
    """
    ret = opt_one
    i = True
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(name_one if i else name_two)
        print("'s' - > select")
        k = input("> ")
        if k == "s":
            return ret
        else:
            i = not i
            ret = opt_one if i else opt_two


#pl
#s = select(12, 32, "tizenkettő", "harminckettő")
#print("selected: ", s)
        
    


