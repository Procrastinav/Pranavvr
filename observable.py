from abc import ABC, abstractmethod


class Observable(ABC):
    # will be inherited by eyeOfSauron
    def __init__(self):
        self.observers_list = []

    # will be inherited by eyeOfSauron. Do not make abstract method
    def add_observer(self, observer):
        self.observers_list.append(observer)

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observer(self, observer):
        pass

    @abstractmethod
    def list_observer(self, observer):
        pass

    @abstractmethod
    def set_changed(self, observer):
        pass

    @abstractmethod
    def has_changed(self, observer):
        pass

    @abstractmethod
    def clear_changed(self, observer):
        pass
