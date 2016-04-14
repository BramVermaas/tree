
import itertools
import abc

class AbstractTraverser(object):
    '''Abstract base class for Tree traversers'''
    def __init__(self, tree, *args, **kwargs):
        self.tree = tree
        self.args = args
        self.kwargs = kwargs
        
        self.filters = kwargs.get('applicable_filters')
        self.stack = self.init_stack()

    def __iter__(self):
        return self

    @property
    def is_applicable(self):
        '''Return True if traverser domain matches args or kwargs'''
        domain_in_args = set(self.domain.values()).issubset(self.args)
        domain_in_kwargs = set(self.domain.iteritems()).issubset(self.kwargs.iteritems())
        return domain_in_args or domain_in_kwargs
        
    def apply_filters(self, items):
        '''Returns filtered items'''
        if self.filters:
            for f in self.filters:
                items = itertools.ifilter(f.predicate, items)
            return items
        return items

    @abc.abstractproperty
    def domain(self):
        '''Returns a dictionary specifying for which arguments the traverser is applicable'''
        raise NotImplementedError

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
    @property
    def domain(self):
        '''Returns a dictionary specifying for which arguments the traverser is applicable'''
        return {'traverse_node_type' : 'descendants',
                'traverse_order' : 'width'}

    def init_stack(self):
        '''Returns the initial stack, to start traversal from'''
        return self.apply_filters( iter(self.tree._children) )

    def next(self):
        '''Returns next item from stack'''
        descendant = self.stack.next()
        
        filtered_children = self.apply_filters( descendant.children )
        self.stack = itertools.chain(self.stack, filtered_children)
        
        return descendant
    
    
class DescendantDepthTraverser(object):
    '''Iterator that returns tree descendants in depth first order '''
    @property
    def domain(self):
        '''Returns a dictionary specifying for which arguments the traverser is applicable'''
        return {'traverse_node_type' : 'descendants',
                'traverse_order' : 'depth'}

    def init_stack(self):
        '''Returns the initial stack, to start traversal from'''
        return self.apply_filters( iter(self.tree._children) )

    def next(self):
        '''Returns next item from stack'''
        descendant = self.stack.next()
        
        filtered_children = self.apply_filters( descendant.children )
        self.stack = itertools.chain(filtered_children, self.stack)
        
        return descendant


class AncestorTraverser(object):
    '''Iterator that returns tree ancestors'''
    @property
    def domain(self):
        '''Returns a dictionary specifying for which arguments the traverser is applicable'''
        return {'traverse_node_type' : 'ancestors'}

    def init_stack(self):
        '''Returns the initial stack, to start traversal from'''
        return self.apply_filters( iter([tree.parent]) )

    def next(self):
        '''Returns next item from stack'''
        ancestor = self.stack.next()
        
        parent = ancestor.parent
        if parent:
            self.stack = itertools.chain(self.stack, self.apply_filters( iter([parent]) ))
            
        return ancestor


