from observable import Observable


class EyeOfSauron(Observable):

    def __init__(self, observer):
        self.observer = []
        self.observer = observer

    def add_observer(self, observer):
        self.observer.append(observer)

    def remove_observer(self, observer):
        self.observer.remove(observer)

    def notify_observer(self, observer):
        for observer in self.observer:
            observer.notify_observer(self.observer)

    def list_observer(self, observer):
        observer.list_observer(self.observer)

    def set_changed(self, observer):
        observer.set_changed(self.observer)

    def has_changed(self, observer):
        observer.has_changed(self.observer)

    def clear_changed(self, observer):
        observer.clear_changed(self.observer)

    def set_enemies(self, hobbit_count, dwarf_count, elf_count, human_count):
        self.hobbit_count = hobbit_count
        self.dwarf_count = dwarf_count
        self.elf_count = elf_count
        self.human_count = human_count
        self.notify_observer(self.observer)
        print("Troop Leader has confirmed reports that the advancing enemy force contains", {hobbit_count}, "hobbits,",
              {dwarf_count}, "dwarfs,", {elf_count}, "elfs, and", {hobbit_count}, "humans.")
