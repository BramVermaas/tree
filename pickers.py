
#   When certain elements are requested from the tree, we return an iterator
#   The itterator encapsulates the traversal algortihms for the Tree
#   But since there are so many different posibilities for traversal,
#   the iterator has a method to use the correct objects (strategy pattern)
#   the different objects an iterator uses are:
#   node_traverser, ordered_traverser, type_filter, level_filter, name_filter
#   path_filter and predicate_filter
#
#   TreeIterator contains a list of filters and traversers
#   init arguments are  **kwargs (we can make sure we can do find_child('name') in convenience method of tree)
#   use func.__code__.co_varnames?
#   When a next item of TreeIterator is requested, the traversers and filters in the list
#   are asked to evaluate on the items (they know themselves if they are applicable)
#



# Different traversal opperators (traversers and filters):
    # node_traverser:       children / descendants / ancestors
    # ordered_traverser:    width / depth
    #
    # name_filter:          'koos' / 'herbert' / ['koos', 'herbert'] / ...
    #       TreeIterator(self, 'children', name = 'koos')
    # rank_filter:          root / leaf / branch
    #       TreeIterator(self, 'descendants', rank = 'leaf')
    # depth_filter:         1 / 2 / 3 / [1, 2, 4]
    #       TreeIterator(self, 'descendats', depth = 2)
    # height_filter:        1 / 2 / 3 / [1, 2, 4]
    #       TreeIterator(self, 'ancestors', height = 3)
    # distance_filter:      1 / 2 / 3 / [1, 2, 4]
    #       TreeIterator(self, 'ancestors', distance = 4)
    # exclude_filter:       Tree / [Tree1, Tree2]
    # relative_path_filter: ['child_name', 'grandchild_name'] /
    #                       [ ['child_name1', 'grandchild_name1'], ['child_name2', 'grandchild_name2'] ]
    # absolute_path_filter: ['root', 'child1'] /
    #                       [ ['root', 'child1'], ['root', 'child2'] ]
    # predicate_filter:     lambda a: '_' in a.name
    # set_filter            ['union', Tree] / ex: [1,2,3] [1,2,4] >> [1,2,3,4]
    #                       ['self-other', Tree] / ex: [1,2,3] [1,2,4] >> [3]
    #                       ['other-self', Tree] / ex: [1,2,3] [1,2,4] >> [4]
    #                       ['intersection', Tree] / ex: [1,2,3] [1,2,4] >> [1,2]

# TreeIterator
# - kiest de juiste traverser
# - maakt een lijstje met filters
#    if applicable_filters:
#          traverser.filters = applicable_filters
# - applies the filters pre_traversal or post_traversal
#       als de filter_phase = 'pre_traversal' dan krijgt de traverser
#       de applicable filters

#       anders past de TreeIterator zelf filters toe (nadat de traverser klaar is)

import walktree

# IDEE:
# TreePicker heeft een method voor children, descendants, ancestors etc
# aan elk van die kan je je filters geven via *args en **kwargs
# dan weten we in ieder geval dat daar alleen filters inzitten,
# en omdat we weten om welke traverser het moet gaan, hoeven we dat niet meer te checken.
# BOEM!

class TreePicker(object):
    '''An iterator using the strategy pattern to traverse a Tree in user specified way'''
    def __init__(self, tree = None, traverse_node_type = 'children',
                 traverse_order = None, **kwargs):

        self.tree = tree
        self.traverse_node_type = traverse_node_type
        self.traverse_order = traverse_order
        self.filter_args = kwargs

        self.traverser = self.init_traverser()
        self.filters = self.init_filters()

    def init_traverser(self):
        '''Returns applicable traverse itterator for traverse_node_type and traverse_order'''
        traversers = [walktree.ChildTraverser(self.tree),
                      walktree.DescendantWidthTraverser(self.tree),
                      walktree.DescendantDepthTraverser(self.tree),
                      walktree.AncestorTraverser(self.tree)]
        # hier wil ik dus eigenlijk een lijstje met traversers maken,
        # liefst automatisch alle classes uit de walktree
        # en die: self.tree, self.traverse_node_typem en self.traverser_order meegeven
        # dus deze method moet even overnieuw
        return next(t for t in traversers
                    if t.is_applicable(traverse_node_type = self.traverse_node_type,
                                       traverse_order = self.traverse_order) )

    def init_filters(self):
        '''Returns applicable filters from provided keyword argument list'''
        pass

    def __iter__(self):
        return self

    def next(self):
        return self.traverser.next()

        
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
