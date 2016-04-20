import abc

class AbstractTree(object):
    '''An interface that defines required methods for the Tree composite data structure'''

    @abc.abstractproperty
    def name(self):
        '''returns tree name in unicode '''
        raise NotImplementedError

    @name.setter
    @abc.abstractmethod
    def name(self, name):
        '''sets tree name '''
        raise NotImplementedError
 
    @abc.abstractproperty
    def children(self):
        '''returns iterator with children of tree'''
        raise NotImplementedError

    @children.setter
    @abc.abstractmethod
    def children(self, children):
        '''sets children for this tree'''
        raise NotImplementedError

    @abc.abstractproperty
    def parent(self):
        '''returns parent of tree'''
        raise NotImplementedError

    @parent.setter
    @abc.abstractmethod
    def parent(self, parent):
        '''sets parent of tree'''
        raise NotImplementedError