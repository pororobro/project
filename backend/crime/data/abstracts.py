from abc import * #all
class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass
class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def csv(self):
        pass
    @abstractmethod
    def xls(self):
        pass
    @abstractmethod
    def json(self):
        pass