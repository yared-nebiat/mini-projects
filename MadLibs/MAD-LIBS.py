import random

print("\t\t\tA game of Mad Libs.")
try:
    with open("games.txt") as games:
        stories = list()
        for game in games:
            stories.append(game)
        (story_name, rest) = random.choice(stories).split(':', 1)
        story_name = story_name.strip()
        (story,placeholders) = rest.split("|",1)
        story = story.strip()
        placeholders = placeholders.strip().split(',')
except (IOError, IndexError) as err:
    print("Error: ", err)
            
print("\t\tThis story is called", story_name)
print("It requires", story.count('%s'), 'inputs, please be patient.')
print("Enter the required information.")

inputs = []
for i in range(story.count("%s")):
	inputs.append(input("%s: " % placeholders[i]).strip())
print(story % tuple(inputs))

input()
