# Jose Capestany
# CS126 2-105
# HW 4/3/2016


# Throwing a party requires the Party() class!
class Party:

    # Intializing the party!
    def __init__(self):
        self._attendance = ['Jose']
        self._food = []
        self._owner = ['Jose']

    # We need to know who is attending!
    def attendance(self):
        return self._attendance

    # Wanna come? No problem! Sign up here!
    def attend(self, x):
        self._attendance.append(x)
        
    # What food do we have you may ask?
    def food(self):
        return self._supplies

    # Want to bring something?
    def bring(self, x):
        self._supplies.append(x)

    # Who's throwing this shingding?
    def owner(self):
        return self._owner

# self._attendance and self._owner are equal, but not the same object.
# Unless someone else decides to show up, then they're not equal.
