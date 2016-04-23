

import traverser

class TreePicker(object):
    '''Configures a TreeTraverser in requested way employing the strategy pattern'''
    def __init__(self, tree):
        self.tree = tree


    def init_filters(self):
        '''Returns all available filters'''
        pass
       

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
        '''returns first child matching specified criteria'''
        pass


    def children(self, *args, **kwargs):
        '''returns iterator with children matching specified criteria'''
        pass


    def ancestor(self, *args, **kwargs):
        '''returns first parent, grandparent, etc, matching specified criteria'''
        pass

    def ancestors(self, *args, **kwargs):
        '''returns iterator with parents, grandparents, etc, matching specified criteria'''
        return traverser.AncestorTraverser(self.tree, args, kwargs)

        
    def descendant(self, *args, **kwargs):
        '''returns first child, grandchild, etc, matching specified criteria'''
        return traverser.DescendantWidthTraverser(self.tree, args, kwargs).next()

    def descendants(self, *args, **kwargs):
        '''returns iterator with children, grandchildren, etc, matching specified criteria'''
        if self.tree.default_traversal_order == 'depth_first':
            return traverser.DescendantDepthTraverser(self.tree, args, kwargs)
        if self.tree.default_traversal_order == 'width_first':
            return traverser.DescendantWidthTraverser(self.tree, args, kwargs)
        
    def descendants_widthfirst(self, *args, **kwargs):
        '''returns iterator with children, grandchildren, etc, matching specified criteria in width first order'''
        return traverser.DescendantWidthTraverser(self.tree, args, kwargs)
        
    def descendants_depthfirst(self, *args, **kwargs):
        '''returns iterator with children, grandchildren, etc, matching specified criteria in depth first order'''
        return traverser.DescendantDepthTraverser(self.tree, args, kwargs)
        
    
