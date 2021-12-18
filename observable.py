from abc import ABC, abstractmethod


class Observable(ABC):

    @abstractmethod
    def add_observer(self, observer):
        pass

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
