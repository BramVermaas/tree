import itertools
import abc


class abstract_filter(object):

    __metaclass__ = abc.ABCMeta

    def init(self, **kwargs):
        self.kwargs = kwargs

    def filter(self, items):
        #hoeft niet perse met een predicate en ifilter te zijn, want we hebben ook slice
        return itertools.ifilter(self.predicate, items)

    def is_applicable(self):
        if self.characteristic in self.kwargs:
            return True
        return False

    @abc.abstractproperty
    def predicate(self):
        raise NotImplementedError

    @property
    @abc.abstractproperty
    def characteristic(self):
        raise NotImplementedError

        
