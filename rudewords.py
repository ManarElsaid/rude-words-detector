rude_words["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]

with open("my_story.txt") as myfile:
    contents = myfile.read()
    rude_count = 0
    for word in rude_words:
        if word in contents:
            rude_count += 1
            print(f"found rude word {word}")
if rude_count == 0:
    print("congratulations, your file has in rudewords.")
    print("At least, no rude words I know.")            
