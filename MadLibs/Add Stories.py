
try:
    with open("games.txt", 'a') as games:
        title = input("Enter the name of the story: ")
        story = input("Enter the story using \"%s\" as a placeholder for the the blanks: ")
        placeholders = []
        print("Enter %d placeholders" % story.count("%s"))
        for i in range(1, story.count("%s")+1):
            placeholders.append(input("Enter placeholder[%d]: " % i))
        print('\n'+ title + ' : ',file=games,end='')
        print(story + ' | ',file=games,end='')
        for i in placeholders:
            print(i + ',',file=games,end='')
except (IOError, IndexError) as err:
    print("Error: ", err)

input("Completed.")
            




