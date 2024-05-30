from abc import abstractmethod


class Processor:
    @abstractmethod
    def process(self):
        raise RuntimeError("'process' method must be overridden for all Processors")
