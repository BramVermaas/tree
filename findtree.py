#hierin komen allemaal classes van de findtree
#bijvoorbeeld descendants
# moet wel een goeie baseclass voor geschreven worden
# die waarschijnlijk itertree kan vervangen


    # methods dealing with multi level trees
    # dit kan eigenlijk ook dan allemaal via find
    # hoewel het fijn is om descendants enzo als wrapper te houden
    # tree.find.descendants()
    # de TreeIterator is dan niet echt meer nodig
    @property
    def descendants(self):
        '''returns a iterator of all children (children, grandchildren, greatgrandchildren etc)'''
        return itertree.TreeIterator(self, 'descendants', self.default_traversal_order)

    @property
    def ancestors(self):
        '''returns an iterator with all parents [parent, grandparent, great-grandparent, root]'''
        return itertree.TreeIterator(self, 'ancestors')

    @property
    def siblings(self):
        '''returns iterator of the other children that the parent of this tree has'''
        # daarvoor de exclude filter gebruiken
        pass



    # filtering
    # dit zou zelfs ook onder find kunnen vallen.
    # tree.find.root
    @property
    def root(self):
        '''returns top most parent of tree'''
        pass

    @property
    def leafs(self):
        '''returns iterator containing all children of tree that have no children of their own'''
        pass

    @property
    def branches(self):
        '''returns iterator containing all non-leaf children of this tree'''
        pass

    # appart object voor gebruiken: tree.find.child()
    def find_child(self, *args, **kwargs):
        '''returns first child matching specified criteria

        examples:

        .find_child('Bert') -> Tree('Bert')
        .find_child(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        pass


    def find_children(self, *args, **kwargs):
        '''returns list of children matching specified criteria

        examples:
        .find_children('Bert') -> [Tree('Bert')]
        .find_children(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        pass


    def find_ancestor(self, *args, **kwargs):
        '''returns first ancestor matching specified criteria

        examples:
        .find_ancestor('Bert') -> Tree('Bert')
        .find_ancestor(level=2) -> Tree('grandparent')
        .find_ancestor(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        pass


    def find_ancestors(self, *args, **kwargs):
        '''returns list of ancestors matching specified criteria

        examples:
        .find_ancestors('Bert') -> [Tree('Bert')]
        .find_ancestors(level=range(1,2)) -> [Tree('parent'), Tree('grandparent')]
        .find_ancestors(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        pass


    def find_descendant(self, *args, **kwargs):
        '''returns first descendant matching specified criteria

        examples:
        .find_descendat('Bert') -> Tree('Bert')
        .find_descendat(level=2) -> [Tree('grandchild1'), Tree('grandchild2')]
        .find_descendat(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        pass

    def find_descendants(self, *args, **kwargs):
        '''returns list of descendants matching specified criteria

        examples:
        .find_ancestors('Bert') -> [Tree('Bert')]
        .find_ancestors(level=2) -> [Tree('parent'), Tree('grandparent')]
        .find_ancestors(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        pass
