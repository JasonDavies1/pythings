import sys

args = sys.argv
supported_languages = ["English", "Spanish", "French"]

if len(args) == 1 :
    print("No Arguments supplied, run with '-help'")
    sys.exit()

if args[1] == "-help" :
    print("Help enabled, enter a language from below")
    for i in supported_languages :
        print(i)
