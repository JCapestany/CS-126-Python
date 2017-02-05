# Jose Capestany
# CS126 ID: 2-105
# 4/14/2016
# Homework

# 9-3

class lock():

    # Sets the initial lock value to a random number 0-9
    def __init__(self):
        import random
        self._lock = random.randint(0,9)
        
    # Change the lock value
    def change(self, x):
        self._lock = x

    # Attempt to open the lock, returns True if succesful
    def open(self, x):
        if x == self._lock:
            return True
        else:
            return False


class big_lock():

    # Sets the initial lock value to a random number 0-999
    def __init__(self):
        import random
        self._lock = random.randint(0,999)
        
    # Change the lock value
    def change(self, x):
        self._lock = x

    # Attempt to open the lock, returns True if succesful
    def open(self, x):
        if x == self._lock:
            return True
        else:
            return False
