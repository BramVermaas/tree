class TreeTraits(object):
    '''Contains all kinds of info on the traits of a given Tree'''
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
        return len( list(self.find.descendants) )

    @property
    def height(self):
        '''returns number of parents between this tree and deepest leaf node'''
        return len( list(self.tree.find.ancestors) )
    
    @property
    def degree(self):
        '''returns number of children this tree has'''
        return len( list(self.tree.children) )