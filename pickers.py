

import walktree

class TreePicker(object):
    '''Configures a TreeTraverser in requested way employing the strategy pattern'''
    def __init__(self, tree = None, traverse_node_type = 'children',
                 traverse_order = None, **kwargs):

        self.tree = tree
        self.traverse_node_type = traverse_node_type
        self.traverse_order = traverse_order
        self.filter_args = kwargs

        self.filters = self.init_filters()


    def init_filters(self):
        '''Returns all available filters'''
        pass

    def __iter__(self):
        return self

    def next(self):
        return self.traverser.next()

       


    @property
    def siblings(self):
        '''returns iterator of the other children that the parent of this tree has'''
        pass



    def root(self):
        '''returns top most parent of tree'''
        pass

    def leafs(self, *args, **kwargs):
        '''returns iterator containing all children of tree that have no children of their own'''
        pass

    def branches(self, *args, **kwargs):
        '''returns iterator containing all non-leaf children of this tree'''
        pass


    def child(self, *args, **kwargs):
        '''returns first child matching specified criteria

        examples:

        .find_child('Bert') -> Tree('Bert')
        .find_child(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        pass


    def children(self, *args, **kwargs):
        '''returns list of children matching specified criteria

        examples:
        .find_children('Bert') -> [Tree('Bert')]
        .find_children(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        pass


    def ancestor(self, *args, **kwargs):
        '''returns first ancestor matching specified criteria

        examples:
        .find_ancestor('Bert') -> Tree('Bert')
        .find_ancestor(level=2) -> Tree('grandparent')
        .find_ancestor(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        pass


    def ancestors(self, *args, **kwargs):
        '''returns list of ancestors matching specified criteria

        examples:
        .find_ancestors('Bert') -> [Tree('Bert')]
        .find_ancestors(level=range(1,2)) -> [Tree('parent'), Tree('grandparent')]
        .find_ancestors(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        
        '''returns an iterator with all parents [parent, grandparent, great-grandparent, root]'''
        return itertree.TreeIterator(self, 'ancestors')
        pass


    def descendant(self, *args, **kwargs):
        '''returns first descendant matching specified criteria

        examples:
        .find_descendat('Bert') -> Tree('Bert')
        .find_descendat(level=2) -> [Tree('grandchild1'), Tree('grandchild2')]
        .find_descendat(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        
        '''returns a iterator of all children (children, grandchildren, greatgrandchildren etc)'''
        return itertree.TreeIterator(self, 'descendants', self.default_traversal_order)
        
        pass

    def descendants(self, *args, **kwargs):
        '''returns list of descendants matching specified criteria

        examples:
        .find_ancestors('Bert') -> [Tree('Bert')]
        .find_ancestors(level=2) -> [Tree('parent'), Tree('grandparent')]
        .find_ancestors(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        pass
