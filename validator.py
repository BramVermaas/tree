import collections
import abc

import tree

class AbstractValidator(object):
    def __init__(self, tree):
        self.tree = tree
    
    @abc.abstractproperty
    def validate(self):
        '''Determines whether items are usuable by Tree'''
        raise NotImplementedError
    

class NameValidator(AbstractValidator):
    '''Validates and prepares name before use by Tree'''
    def validate(self, name):
        return name

        
class ChildValidator(AbstractValidator):
    '''Validates and prepares children before use by Tree'''
    def __init__(self, tree):
        self.tree = tree
    
    
    def validate(self, items, is_additional = False):
        '''Returns validated Tree items'''
        items = self.cast_to_list(items)
        
        self.check_items_type(items)
        self.check_for_circular_hierarchy(items)
        self.check_for_duplicate_names(items)
        
        if is_additional:
            self.check_for_duplicates_with_children(items)
        
        return items
        
    
    def cast_to_list(self, items):
        '''returns items as a list'''
        if not type(items) == list:
            if not items:
                items = []
            if isinstance(items, collections.Iterable):
                items = list(items)
            else:
                items = [items]
        return items

    def check_items_type(self, items):
        '''raise error if any item is not of type Tree class or subclass'''
        for item in items:
            if not issubclass(type(item), tree.Tree):
                raise TypeError('{tree} is trying to add or remove the child: {item} ' \
                                'with unexpected type: {item_type}. ' \
                                'Only an instance of the Tree class or its subclasses ' \
                                'are valid children.' \
                                .format(tree = self.tree, item = item, item_type = type(item)))


    def check_for_circular_hierarchy(self, items):
        '''raise error if any item has the same identity as the tree itself'''
        if [i for i in items if i is self.tree]:
            raise ValueError( '{tree} is trying to add or remove itself as a child. ' \
                              'Circular hierarchies are not allowed.' \
                              .format(tree = self.tree))

                    
    def check_for_duplicate_names(self, items):
        '''raise error if items contains trees with the same name'''
        checked_items = []
        for item in items:
            if [c for c in checked_items if c.name == item.name]:
                raise ValueError('{tree} is trying to add or remove multiple children ' \
                                 'in which one or more copies of {item} ' \
                                 'have the same name. ' \
                                 'Children with the identical names are not allowed.' \
                                 .format(tree = self.tree, item = item))
            checked_items.append(item)
            
    def check_for_duplicates_with_children(self, items):
        '''raise error if items contains trees with the same name as existing children'''
        if self.tree.children:
            for item in items:
                if [c for c in self.tree.children if c.name == item.name]:
                    raise ValueError('{item} is allready a child of {tree}. ' \
                                     'Children with the identical names are not allowed.' 
                                     .format(item = item, tree = self.tree))
            

class ParentValidator(AbstractValidator):
    def validate(self, items):
        return items


