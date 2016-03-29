# key function notes:
#   Tree class should stay focussed (it's a data structure, should be clean of traversal functionality)
#   it should be easy to add new traversal methods

# ik wil de tree data structure scheiden van de interface
# als ik dan een wil aanspreken op een andere manier (bijvoorbeeld met de . notatie)
# dus root.leftArm.leftHand.leftPinky
# ipv root.find_child('leftArm').find_child('leftHand')

import walktree
import treesettings
import validtree
import findtree
import ordertree

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
        return walktree.ChildTraverser(self)

    @children.setter
    def children(self, children):
        '''sets children for this tree'''
        self._children = validtree.ChildValidator(self, children).items

        for child in self._children:
            if not child.parent == self:
                child.parent = self

    def add_children(self, children):
        '''appends provided tree to children or extends it with provided list'''
        self.children = self._children + validtree.ChildValidator(self, children).items

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
        return treesettings.TreeSettings()

    @property
    def find(self):
        return findtree.TreeFinder()

    @property
    def sort(self):
        return ordertree.TreeSorter()

    @property
    def reverse(self):
        return ordertree.TreeReverser()

    @property
    def view(self):
        return viewtree.TreeViewer()


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
