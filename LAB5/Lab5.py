# Jose Capestany
# Jackson Pergiel
# CS126L
# Lab 5: Undeadbook

import time


def update(book, status, audience, userid):
    # Sets the unique ID
    id = len(book)
    # Updates book with the new update
    book.append({"Time": time.time(), "Groups": audience, "Likes": [],
                 id: ["%s (mention with @%s) says:" % (userid, userid),
                 status]})
    # Prints the time the post was made
    print("Post made at %.6f by %s" % (time.time(), userid))
    # Returns the unique ID
    return id


def like(book, id, userid):
    # If user already liked, do nothing
    if userid in book[id]["Likes"]:
        return None
    # If user has not liked, like the post
    else:
        # Saves who has liked the post
        book[id]["Likes"].insert(0, userid)
    return None


def unlike(book, id, userid):
    # If user has liked the post, unlike it
    if userid in book[id]["Likes"]:
        # Remove users who have unliked the post
        book[id]["Likes"].remove(userid)
        return None
    # If the user has not liked the post, do nothing
    else:
        return None


def display(book, id):
    # Displays the time the post was made
    print("Time: %f" % (book[id]["Time"]))
    # Displays the groups for the post
    print("Groups:", book[id]["Groups"])
    # Displays the # of likes for the post
    print("Likes: %d" % (len(book[id]["Likes"])))
    # Display the who posted the status
    print(book[id][id][0])
    # Displays the status
    print(book[id][id][1])
    # Empty Line
    print("")
    return None

# Code we have to run
book = []
barnabas_one = update(book, "Storming the village at 9. Anyone interested?",
                      ["Zombies", "Vampires"], "BarnabasCollins")

time.sleep(1)

casper_one = update(book, "Can I come?", ["Vampires"], "Casper")

time.sleep(1)

barnabas_two = update(book, "Forgot to include the ghosts! LOL",
                      ["Ghosts"], "BarnabasCollins")

time.sleep(1)

barnabas_three = update(book, "Lots of villagers with forks here...",
                        ["Vampires", "Zombies", "Ghosts"], "BarnabasCollins")

like(book, barnabas_one, "Edmund")
like(book, barnabas_one, "Grimm")
like(book, barnabas_one, "Edmund")
like(book, casper_one, "Edmund")
like(book, casper_one, "Grimm")
like(book, casper_one, "Harry")
like(book, casper_one, "Count Chocula")
like(book, barnabas_two, "Casper")
like(book, barnabas_three, "Casper")
like(book, barnabas_three, "Count Chocula")
like(book, barnabas_three, "Boo")

unlike(book, casper_one, "Edmund")
unlike(book, barnabas_three, "Casper")
unlike(book, casper_one, "Edmund")

display(book, barnabas_one)
display(book, barnabas_three)
print("---")
display(book, casper_one)
