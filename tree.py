# key function notes:
#   Tree class should stay focussed (it's a data structure, should be clean of traversal functionality)
#   it should be easy to add new traversal methods

# ik wil de tree data structure scheiden van de interface
# als ik dan een wil aanspreken op een andere manier (bijvoorbeeld met de . notatie)
# dus root.leftArm.leftHand.leftPinky
# ipv root.find_child('leftArm').find_child('leftHand')

import traversers
import settings
import validators
import pickers
import organizers

class Tree(object):
    '''A composite data structure that represents hierarchical relations'''
    def __init__(self, name='', children = [], parent = None):
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
        self._name = unicode(name)

    #children methods
    @property
    def children(self):
        '''returns iterator with children of tree'''
        return traversers.ChildTraverser(self)

    @children.setter
    def children(self, children):
        '''sets children for this tree'''
        self._children = validators.ChildValidator(self, children).items

        for child in self._children:
            if not child.parent == self:
                child.parent = self

    def add_children(self, children):
        '''appends provided tree to children or extends it with provided list'''
        self.children = self._children + validator.ChildValidator(self, children).items
        
    def remove_children(self, children):
        # moet dit by name, of heb je echt de tree zelf nodig?
        pass

    #parent methods
    @property
    def parent(self):
        '''returns parent of tree'''
        return self._parent

    @parent.setter
    def parent(self, parent):
        '''sets parent of tree'''
        self._parent = parent
        if parent and not self in parent.children:
            parent.add_children(self)

    # characteristic attributes
    @property
    def is_leaf(self):
        '''returns True if tree has no children'''
        if not self._children:
            return True
        return False

    @property
    def is_root(self):
        '''returns True if tree has no parents'''
        if not self._parents:
            return True
        return False

    @property
    def is_branch(self):
        '''returns True if tree has children and parents'''
        if not self.is_root and not self.is_leaf:
            return True
        return False

    @property
    def depth(self):
        '''returns number of parents between this tree and root '''
        return len( list(self.descendants) )

    @property
    def height(self):
        '''returns number of parents between this tree and deepest leaf node'''
        return len( list(self.ancestors) )


    # advanced methods
    @property
    def settings(self):
        # wel zorgen dat alleen een root object de settings heeft
        return settings.TreeSettings()

    @property
    def find(self):
        return pickers.TreePicker()

    @property
    def sort(self):
        return organizers.TreeSorter()

    @property
    def reverse(self):
        return organizers.TreeReverser()

    @property
    def view(self):
        return viewers.TreeViewer()


    # magic methods
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
