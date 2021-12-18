from abc import ABC, abstractmethod


class Observer(ABC):

    # this will be inherited by bad_guy
    def __init__(self, observable, observer_name):
        observable.add_observer(self)
        self.attached = observable
        self.name = observer_name

    @abstractmethod
    def update(self, observable):
        pass
