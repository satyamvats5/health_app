import simplejson
import os.path

class DBHelper(object):
    def __init__(self):
        if os.path.isfile("./db.json"):
            with open("./db.json", "rb") as db:
                self._cursor = simplejson.load(db)
        else:
            print("Not found db")
            self._cursor = []

    def load(self):
        print("Loading")
        return self._cursor   