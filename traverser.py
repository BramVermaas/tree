
import itertools
import abc

class AbstractTraverser(object):
    '''Abstract base class for Tree traversers'''
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, tree, *args, **kwargs):
        self.tree = tree
        self.args = args
        self.kwargs = kwargs
        
        self.filters = []
        self.stack = self.init_stack()

    def __iter__(self):
        return self
        
    def apply_filters(self, items):
        '''Returns filtered items'''
        if self.filters:
            for f in self.filters:
                items = f.filter(items)
            return items
        return items

    @abc.abstractmethod
    def init_stack(self):
        '''Returns the initial stack, to start traversal from'''
        raise NotImplementedError

    @abc.abstractmethod
    def next(self):
        '''Returns next item from stack'''
        raise NotImplementedError


class DescendantWidthTraverser(AbstractTraverser):
    '''Iterator that returns tree descendants in width first order '''
    def init_stack(self):
        '''Returns the initial stack, to start traversal from'''
        return self.apply_filters( self.tree.children )

    def next(self):
        '''Returns next item from stack'''
        descendant = self.stack.next()
        
        filtered_children = self.apply_filters( descendant.children )
        self.stack = itertools.chain(self.stack, filtered_children)
        
        return descendant
    
    
class DescendantDepthTraverser(AbstractTraverser):
    '''Iterator that returns tree descendants in depth first order '''
    def init_stack(self):
        '''Returns the initial stack, to start traversal from'''
        return self.apply_filters( self.tree.children )

    def next(self):
        '''Returns next item from stack'''
        descendant = self.stack.next()
        
        filtered_children = self.apply_filters( descendant.children )
        self.stack = itertools.chain(filtered_children, self.stack)
        
        return descendant


class AncestorTraverser(AbstractTraverser):
    '''Iterator that returns tree ancestors'''
    def init_stack(self):
        '''Returns the initial stack, to start traversal from'''
        if self.tree.parent:
            return self.apply_filters( iter([self.tree.parent]) )
        return iter([])

    def next(self):
        '''Returns next item from stack'''
        ancestor = self.stack.next()
        
        if ancestor:
            parent = ancestor.parent
            if parent:
                self.stack = itertools.chain(self.stack, self.apply_filters( iter([parent]) ))
            
        return ancestor


