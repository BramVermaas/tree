
import collections
import tree

class ChildValidator(object):
    '''Validates and prepares input before use by Tree'''
    def __init__(self, tree, items):
        self.tree = tree
        self.items = self._cast_to_list(items)

        self._check_items_type()
        self._check_for_circular_hierarchy()
        self._check_for_identical_items()
        self._check_for_identical_children()
        

    def _cast_to_list(self, items):
        '''returns items as a list'''
        if not type(items) == list:
            if not items:
                items = []
            if isinstance(items, collections.Iterable):
                items = list(items)
            else:
                items = [items]
        return items

    def _check_items_type(self):
        '''raise error if any item is not of type Tree class or subclass'''
        for item in self.items:
            if not issubclass(type(item), tree.Tree):
                raise TypeError('{tree} is trying to add the child: {item} ' \  
                                'with unexpected type: {item_type}. ' \
                                'Only an instance of the Tree class or its subclasses ' \
                                'are allowed as children.' \
                                .format(tree = self.tree, item = item, item_type = type(item)))


    def _check_for_circular_hierarchy(self):
        '''raise error if any item has the same identity as the tree itself'''
        if [i for i in self.items if i is self.tree]:
            raise ValueError( '{tree} is trying to add itself as a child. ' \
                              'Circular hierarchies are not allowed.' \
                              .format(tree = self.tree))

                    
    def _check_for_identical_items(self):
        '''raise error if items contains trees with the same identity'''
        checked_items = []
        for item in self.items:
            if [c for c in checked_items if c is item]:
                raise ValueError('{tree} is trying to add multiple children ' \
                                 'in which several copies of {item} ' \
                                 'have the same identity. ' \
                                 .format(tree = self.tree, item = item))
            checked_items.append(item)
            
    def _check_for_identical_children(self):
        '''raise error if items contains trees with the same identity as existing children'''
        if self.tree.children:
            for item in self.items:
                if [c for c in self.tree.children if c is item]:
                    raise ValueError('{item} is allready a child of {tree}. ' \
                                     'Children with the same identity are not allowed.' 
                                     .format(item = item, tree = self.tree))
            




