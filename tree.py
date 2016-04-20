
import abstracttree

import validator
import settings
import picker
import traits
import organizer
import converter

class Tree(abstracttree.AbstractTree):
    '''A composite data structure that represents hierarchical relations'''
    def __init__(self, name='', children = [], parent = None):
        self._name = ''
        self._children = []
        self._parent = None
        
        self.name = name
        self.children = children
        self.parent = parent

    @property
    def name(self):
        '''returns tree name in unicode '''
        return self._name

    @name.setter
    def name(self, name):
        '''sets tree name '''
        self._name = self.name_validator.validate(name)

        
    @property
    def children(self):
        '''returns iterator with children of tree'''
        return iter(self._children)

    @children.setter
    def children(self, children):
        '''sets children for this tree'''
        self._change_relatives(new_parent = self, children = children)

    def add_children(self, children):
        '''appends provided tree to children or extends it with provided list'''
        additional_children = self.child_validator.validate_additional(self, children)
        self.children = self._children + additional_children
        
    def remove_children(self, children):
        '''removes provided tree from children or removes the provided list of children'''
        for child in children: child.parent = None
        
    @property
    def parent(self):
        '''returns parent of tree'''
        return self._parent

    @parent.setter
    def parent(self, parent):
        '''sets parent of tree'''
        self._change_relatives(new_parent = parent, children = [self])
    
    def _change_relatives(self, new_parent, children):
        '''Performs all necesarry attribute updates for switching parent or children'''
        children = self.child_validator.validate(new_parent, children)
        for child in children:
            new_parent = self.parent_validator.validate(new_parent, child)
            
            old_parent = child.parent
            if old_parent:
                old_parent._children.remove(child)
            child._parent = new_parent          
            
        if new_parent:
            if children:
                new_parent._children += children
            else:
                new_parent._children = []

                
    @property
    def name_validator(self):
        return validator.NameValidator()
        
    @property
    def child_validator(self):
        return validator.ChildValidator()
        
    @property
    def parent_validator(self):
        return validator.ParentValidator()
        
    @property
    def traits(self):
        return traits.TreeTraits(self)
    
    @property
    def settings(self):
        return settings.TreeSettings(self)

    @property
    def find(self):
        return picker.TreePicker(self)

    @property
    def sort(self):
        return organizer.TreeSorter(self)

    @property
    def reverse(self):
        return organizer.TreeReverser(self)

    @classmethod
    @property
    def convert_from(self):
        return converter.TreeFrom(self)
    
    @property
    def convert_to(self):
        return converter.TreeTo(self)
        
    @property
    def view(self):
        return viewers.TreeViewer(self)


        
    def __repr__(self):
        ''' returns "classname('name') '''
        return "{type}('{name}')".format( type = str(self.__class__.__name__), name=self.name)

    def __eq__(self, other):
        '''returns whether trees are equal'''
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        '''returns if trees are unequal'''
        return not self.__eq__(other)
