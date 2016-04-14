import settings
import validator
import picker
import traits
import organizer
import converter

class Tree(object):
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
        new_children = self.child_validator.validate(children)
        self._change_lineage(new_parent = self, children = new_children)

    def add_children(self, children):
        '''appends provided tree to children or extends it with provided list'''
        self.children = self._children + self.child_validator.validate(children, is_additional = True)
        
    def remove_children(self, children):
        '''removes provided tree from children or removes the provided list of children'''
        children_to_remove = self.child_validator.validate(children)
        self._children = [c for c in self._children if not c in children_to_remove]

        
    @property
    def parent(self):
        '''returns parent of tree'''
        return self._parent

    @parent.setter
    def parent(self, parent):
        '''sets parent of tree'''
        parent = self.parent_validator.validate(parent)
        self._change_lineage(new_parent = parent, children = [self])
    
    
    
    def _change_lineage(self, new_parent, children):
        '''Performs all necesarry attribute updates for changing parent or children'''
        if new_parent:
            old_parent = new_parent.parent
        
        
        for child in children:
            old_parent = adoptee.parent
            
            
            if old_parent != new_parent:
                if old_parent:
                    old_parent._children.remove(child)
                child._parent = new_parent
        
        if new_parent:        
            new_parent._children = children
            
        
    
    @property
    def name_validator(self):
        return validator.NameValidator(self)
        
    @property
    def child_validator(self):
        return validator.ChildValidator(self)
        
    @property
    def parent_validator(self):
        return validator.ParentValidator(self)
        
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
    def loads(self):
        return converter.TreeLoader(self)
    
    @property
    def dumps(self):
        return converter.TreeDumper(self)
        
    @property
    def view(self):
        return viewers.TreeViewer(self)


        
    def __repr__(self):
        ''' returns "Tree('name') '''
        return "Tree('{name}')".format(name = self.name)

    def __eq__(self, other):
        '''returns whether trees are equal'''
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        '''returns if trees are unequal'''
        return not self.__eq__(other)
