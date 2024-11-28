import abc


class Interface(metaclass=abc.ABCMeta):
    # abstract method は、継承先で必ず実装しなければならない
    @abc.abstractmethod
    def method(self):
        pass


# Interface を継承して、method を実装する
class Concrete(Interface):
    def method(self):
        return "Concrete"
