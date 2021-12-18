from observer import Observer
from eye_of_sauron import EyeOfSauron


class BadGuy(Observer):

    def __init__(self, observable, troop_lead):
        self.observable = observable
        self.bad_guy = troop_lead
        EyeOfSauron.add_observer(self)

    def update(self, observable):
        pass

    def defeated(self):
        EyeOfSauron.remove_observer(self)
