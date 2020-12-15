def raise_to_debug(level, file):
    # traitsui/traitsui/api.py  raise_to_debug()
    # caller pass in level range 1..3
    noBreak=4
    doBreak=3
    moreBreak=2
    one = "1"
    import os
    env = os.getenv("PYTHONBREAKPOINT")
    if env == one and level >= noBreak:
        print("Debug break: ", file)
        breakpoint()
    elif level == 0:
        print("Debug INFO: ", file)

