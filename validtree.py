
import collections
import tree

class ChildValidator(object):
    '''Validates and prepares input before use by Tree'''
    def __init__(self, tree, items):
        self.tree = tree
        self.items = self._cast_to_list(items)

        self._check_items_type()
        self._check_for_circular_hierarchy()

    def _cast_to_list(self, item):
        '''returns item as a list'''
        if not type(item) == list:
            if not item:
                item = []
            if isinstance(item, collections.Iterable):
                item = list(item)
            else:
                item = [item]
        return item

    def _check_items_type(self):
        '''raise error if  is not of type Tree or subclass of Tree class'''
        for item in self.items:
            if not issubclass(type(item), tree.Tree):
                raise TypeError('Unexpected Tree child type: ' +
                                '{item_type}. '.format(item_type = type(item)) +
                                'Only Tree instances or ' +
                                'subclasses of Tree class are allowed.')


    def _check_for_circular_hierarchy(self):
        '''raise error if items contains the tree itself'''
        if self.tree in self.items:
            raise ValueError( '{tree} is trying to add itself as a child.'.format(
                              tree = self.tree) +
                              ' Circular hierarchies are not allowed.')

    # een circular dependency kan alleen onstaan als:
        # het item een parent heeft
        # zowel het item als de tree dezelfde root hebben

    #def _check_for_multiple_parents(self):
    #    '''raise error if items allready have parents'''
    #    for item in self.items:
    #        if item.parent:
    #            raise ValueError( '{item} allready has a parent: {parent}.'.format(
    #                              item = item, parent = item.parent) +
    #                              ' Multiple parents are not allowed.')




class TraversalValidator(object):
    def __init__(self, traversal_order = ''):
        self.traversal_order = traversal_order

    def check_traversal_order(self):
        traversal_order_type = type(self.traversal_order)
        if not traversal_order_type == str:
            raise TypeError('Unexpected traversal order type: ' \
                            '{traversal_type}. Can only be of type str.'.format(
                            traversal_type = traversal_order_type))
        if not self.traversal_order in ['depth', 'width']:
            raise ValueError("Unexpected traversal order value: {traversal_order}." \
                             "Allowed values are only 'depth' or 'width.'".format(
                             traversal_order = self.traversal_order))
