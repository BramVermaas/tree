import collections
import abc

import abstracttree

class AbstractValidator(object):
    @abc.abstractmethod
    def validate(self, parent, children):
        '''Determines whether children are usuable by Tree'''
        raise NotImplementedError
    

class NameValidator(AbstractValidator):
    '''Validates and prepares name before use by Tree'''
    def validate(self, name):
        return name

        
class ChildValidator(AbstractValidator):
    '''Validates and prepares children before use by parent'''

    def validate(self, parent, children):
        '''Returns validated Tree children'''
        self.parent = parent
        self.children = self.cast_to_list(children)
        
        self.check_children_type()
        self.check_for_child_self_refrence()
        self.check_for_duplicate_children()
        
        return self.children
        
    def validate_aditional(self, parent, children):
        '''Returns validated additonal Tree children'''
        self.parent = parent
        self.children = self.cast_to_list(children)
        
        self.check_for_duplicates_with_existing_children()
        return self.children
    
    def cast_to_list(self, children):
        '''returns children as a list'''
        if not type(children) == list:
            if not children:
                children = []
            elif isinstance(children, collections.Iterable):
                children = list(children)
            else:
                children = [children]
        return children

    def check_children_type(self):
        '''raise error if any child is not of type AbstractTree or subclass'''
        for child in self.children:
            if not issubclass(type(child), abstracttree.AbstractTree):
                raise TypeError('{parent} is trying to add or remove the child: {child} ' \
                                'with unexpected type: {child_type}. ' \
                                'Only an instance of the AbstractTree class or its subclasses ' \
                                'are valid children.' \
                                .format(parent = self.parent, child = child, child_type = type(child)))


    def check_for_child_self_refrence(self):
        '''raise error if any child has the same identity as the parent itself'''
        if [c for c in self.children if c is self.parent]:
            raise ValueError( '{parent} is trying to add or remove itself as a child. ' \
                              'Circular hierarchies are not allowed.' \
                              .format(parent = self.parent))

                    
    def check_for_duplicate_children(self):
        '''raise error if children contains a tree with the same name'''
        checked_children = []
        for child in self.children:
            if [c for c in checked_children if c.name == child.name]:
                raise ValueError('{parent} is trying to add or remove multiple children ' \
                                 'in which one or more copies of {child} ' \
                                 'have the same name. ' \
                                 'Children with the identical names are not allowed.' \
                                 .format(parent = self.parent, child = child))
            checked_children.append(child)
            
    def check_for_duplicates_with_existing_children(self):
        '''raise error if children contains a tree with the same name as existing children'''
        if self.parent and self.parent.children:
            for parent_child in self.parent.children:
                if [c for c in self.children if c.name == parent_child.name]:
                    raise ValueError('{child} is allready a child of {parent}. ' \
                                     'Children with the identical names are not allowed.' 
                                     .format(child = parent_child, parent = self.parent))
            

class ParentValidator(AbstractValidator):
    def validate(self, parent, child):
        self.parent = parent
        self.child = child
        
        self.check_parent_type()
        return parent

    def check_parent_type(self):
        '''raise error if parent is not of type AbstractTree or subclass'''
        if self.parent and not issubclass(type(self.parent), abstracttree.AbstractTree):
            raise TypeError('{child} is trying to set as parent: {parent} ' \
                            'with unexpected type: {parent_type}. ' \
                            'Only an instance of the AbstractTree class or its subclasses ' \
                            'is a valid parent.'.format(parent = self.parent, 
                            child = self.child, parent_type = type(self.parent)))


