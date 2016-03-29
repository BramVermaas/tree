# key function notes:
#   Tree class should stay focussed (it's a data structure, should be clean of traversal functionality)
#   it should be easy to add new traversal methods
#
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
#   TraversersalOpperator (Traversers & filters)
#   type:                   nodeTraverser / orderedTraverser / filter
#   is_applicable()         if 'name' in **kwargs
#   evaluate()              only return if provided name in **kwargs

# Different traversal opperators:
    # node_traverser:       children / descendants / ancestors
    # ordered_traverser:    width / depth
    #
    # type_filter:          root / leaf / branch
    # depth_filter:         1 / 2 / 3 / [1, 2, 4]
    # height_filter:        1 / 2 / 3 / [1, 2, 4]
    # name_filter:          'koos' / 'herbert' / ['koos', 'herbert'] / ...
    # path_filter:          'child_name/grandchild_name' /
    #                       ['child_name1/grandchild_name1', 'child_name2/grandchild_name2']
    # predicate_filter:     lambda a: '_' in a.name)



# unresolved problems:
#   if I define the convenience methods that wrap the static factor in the Tree itself
#   we again get a lot of traversal methods defined (although only as wrapper) in Tree
#
#   Also, every time we add another traversal method, we have to add a convenience wrapper
#   for it in the Tree class.
#
#   Optie 1) inheritance
#   AbstractTreeIter (relatives, level, name, path, predicate)
#       TreeChildIter
#       TreeDescendantIter
#       TreeAncestorIter
#       TreeDepthIter
#       TreeWidthIter
#           TreeAncestorDepthIter
#           TreeAncestorWdithIter
#           etc...
#   Nadelen: Hoop subclasses met erg beperkte functionaliteit
#            Alle filters (die ik later wil toevoegen) zitten in abstractTree
#
#   Optie 2) static factory / Strategy
#   iterator creates objects based on provided arguments
#   TreeIter(nodes = 'descendants', order = 'width', type = 'leaf')
#       node_traverser(nodes)
#       ordered_traverser(order)
#       filter('type', type)    # voordeel: kan nieuwe soort filter maken
#                                zonder dat ik ze expliciet hoef te definieren
#                                in iterator
#   misschien kan node_traverser en ordered_traverser 1 class zijn
#   De convienence methods hoeven zelf alleen maar *args en **kwargs te kunnen ontvangen
#   De iterator moet maar weten wat hij met die arguments kan





# Key Structure notes
    # Tree is a DATA STRUCTURE
    #   stores name (id), parent, children
    #   stores some settings
    #       default_traversal
    #   basic methods to access and change stored data
    #       .name = 'x', .parent = Tree(), .children = [], .add_children()
    #   basic methods that reveal info about Tree
    #       is_root(), is_leaf(), is_branch(), depth(), height()
    #   complex traversal methods that are convenience wrappers to create an iterator

    # TreeIterator is an ALGORITHM
    # has the methods to traverse a Tree (the Tree itself doesn't have any of these)

    #




# AbstractTree
# AttrTree
# Tree (the normal tree)




class Tree(object):
    '''Tree is a composite object that can represent hierarchical data'''
    def __init__(self, name='', children = [], parent = None):
        self.name = name
        self.children = children
        self.parent = parent

        self.default_traversal = 'width'

    @property
    def hierarchy_name(self):
        '''concatenates names of all parents into a complete name '''

    # basic children methods
    @property
    def children(self):
        '''returns itterator with children of tree'''
        return self._children

    @children.setter
    def children(self, children):
        '''sets children for this tree'''
        # cast to list method here
        self._children = children

    def add_children(self, children):
        '''appends provided tree to children or extends it with provided list'''
        pass


    # basic parent methods
    @property
    def parent(self):
        '''returns parent of tree'''
        return self._parent

    @parent.setter
    def parent(self, parent):
        '''sets parent of tree'''
        self._parent = parent


    # methods dealing with ancestor trees
    @property
    def ancestors(self):
        '''returns an itterator with all parents [parent, grandparent, great-grandparent, root]'''
        pass

    def find_ancestor(self, name = None, path = None, level = None, predicate = None):
        '''returns first ancestor matching specified criteria

        examples:
        .find_ancestor('Bert') -> Tree('Bert')
        .find_ancestor(level=2) -> Tree('grandparent')
        .find_ancestor(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        pass
# level accepts a list (so also [1,4,5] would be vallid)
    def find_ancestors(self, name = None, level = None, predicate = None):
        '''returns list of ancestors matching specified criteria

        examples:
        .find_ancestors('Bert') -> [Tree('Bert')]
        .find_ancestors(level=range(1,2)) -> [Tree('parent'), Tree('grandparent')]
        .find_ancestors(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        pass


    @property
    def root(self):
        '''returns top most parent of tree'''
        pass

    @property
    def depth(self):
        '''returns a count of parents to root '''
        return len(self.descendants())





    def find_child(self, name = None, predicate = None):
        '''returns first child matching specified criteria

        examples:
        .find_child('Bert') -> Tree('Bert')
        .find_child(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        pass

    def find_children(self, name = None, predicate = None):
        '''returns list of children matching specified criteria

        examples:
        .find_children('Bert') -> [Tree('Bert')]
        .find_children(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        pass

    @property
    def siblings(self):
        '''returns list of the other children that the parent of this tree has'''
        pass



    # methods dealing with sibling trees
    @property
    def descendants(self):
        '''returns a list of ALL children (children, grandchildren, greatgrandchildren etc)'''
        pass

# onderscheid maken tussen level en to_level
    def find_descendat(self, name = None, level = None, predicate = None):
        '''returns first descendant matching specified criteria

        examples:
        .find_descendat('Bert') -> Tree('Bert')
        .find_descendat(level=2) -> [Tree('grandchild1'), Tree('grandchild2')]
        .find_descendat(predicate= lambda a: '_' in a.name) --> Tree('my_name')
        '''
        pass

    def find_ancestors(self, name = None, level = None, predicate = None):
        '''returns list of ancestors matching specified criteria

        examples:
        .find_ancestors('Bert') -> [Tree('Bert')]
        .find_ancestors(level=2) -> [Tree('parent'), Tree('grandparent')]
        .find_ancestors(predicate= lambda a: '_' in a.name) --> [Tree('my_name')]
        '''
        pass

    def find_descendant(self, name):
        '''returns first descendant matching specified name'''
        pass

    def find_descendants(self, name):
        '''Returns a list of descendants matching specified name '''
        pass

    def filter_descendant(self, predicate):
        '''returns first descendant matching specified predicate '''
        pass

    def filter_descendants(self, predicate):
        '''returns list of descendants matching specified predicate '''
        pass

    def descendants_from_level(self, level):
        '''Returns a list containing all children of this tree, up to a specified depth

        examples:
        descendants_from_level(1) -> [child1, child2]
        descendants_from_level(2) -> [child1, child2, grandchild1, grandchild2]
        '''
        pass

    # special methods dealing with children
    @property
    def leafs(self):
        '''returns list containing all children of tree that have no children of their own'''
        pass

    @property
    def branches(self):
        '''returns list containing all non-leaf children of this tree'''
        pass

    @property
    def height(self):
        '''returns number of parents between this tree and deepest leaf node'''
        pass

    # tree setting related methods
    @property
    def default_traversal(self):
        '''returns default traversal method used when getting children'''
        return self._default_traversal

    @ default_traversal.setter
    def default_traversal(self, traversal=''):
        '''sets default traversal used when getting children'''
        if not type(traversal) == str:
            raise TypeError('Unexpected traversal type. Method can only be of type str')
        if not traversal in ['depth', 'width']:
            raise ValueError("Unexpected traversal value. Allowed methods are only 'depth' or 'width'")

        self._default_traversal = traversal

    def sort_children(self, key=None):
        '''sorts children by name, unless key function is specified'''
        # handle situations in which you sort on an attribute that not all nodes have
        pass

    def sort_descendants(self, key=None):
        '''sorts descendants by name, unless key function is specified'''
        pass

    def reverse_children(self):
        pass

    def reverse_descendants(self):
        pass

    def __repr__(self):
        ''' returns "Tree('name') '''
        pass

    # as and from methods we create wrappers for, but we use a converter
    # to do the actual work
    # do we need them anyway, now we have the iterator
    #def as_dict
    #def as_string
    #def as_list
    #def as_json
    #def from_dict
    #def from_string
    #def from_list
    #def from json

    # def pickle
    # def copy
    # def deepcopy

    # plotting should be done by seperate Display
    # def plot(type='ascii')
    # tree(1)
    #   tree(2)
    #       tree(3)
    #   tree(4)
    # as should writing out an hierarchy name
    #     @property
    #def hierarchy_name(self):
    #   '''concatenates names of all parents into a complete name '''
    #   pass









    # deze kan weg, de traverse functionaliteit is verantwoordelijkheid van de itterator
    # de tree geeft alleen maar een default mee (die gebruikt wordt bij het aanmaken van de juiste itterator)
    def _get_traverse(self, method = ''):
        '''for specified traverse method, returns function used to traverse tree '''
        # inplaats hiervan de walkType en walkMethod in een dict opslaan
        # {order: method} depth, breadth, pre of post
        # {walkType (depth or breadth): walkMethod (function)}
        if method == 'depth':
            def traverse_function(expansion, queue):
                return queue[1:] + expansion
            self._traverse = traverse_function
        elif method == 'breadth':
            def traverse_function(expansion, queue):
                return expansion + queue[1:]

        return traverseFunction



# custom visit function (that uses walkOrder), which users can define
# misschien toch gewoon een dictionary gebruiken (voor snelheid) en als er een gesorteerd resultaat gegeven moet worden,
# alleen dan de elementen sorteren (dus eerst een lijst van maken, dan sorteren?)

# of kan ik een find method schrijven die toestaat om op basis van level=2 of predicate=lambda x: x.age>10, of name='test'
# als argument een string is, gaat hij er van uit dat het een naam is, als het een functie is een predicate,
# als het een integer is, dan is het een level,
# je kan ze ook combineren
# wel onderscheid houden in find_child en find_children

# en eigenlijk zijn find_parent en find_child specifieke toepassingen van find_node (met ingebakken argument)
# find_node kan zelf wel weer gebruik maken van nodes_from_level, nodes_with_name, nodes_filtered_by

# eigenlijk behoort het zoeken van dingen in de tree niet tot de verantwoordelijkheid van de tree.
# de tree is een data structuur (puur)
# daarbij kan (volgens het visitor pattern) een traverser of walker komen, die het doorzoeken van de tree doet
# find(nodeType, name, path, level, predicate)
# nodeType is child, descendants, parents etc
# name kan een string zijn, of een list van strings (die allemaal gematched worden)
# path is een string parent/grandparent/great-grandparent om een geneste descendant of ancestor te vinden
# level mag een integer of list aan integers zijn (om meerdere, of een range aan levels te pakken)
# predicate is een functie

# tree moet een itterator functie hebben, zodat ik kan doen: for item in Tree
# de itterator returned objecten in volgorde gedefinieerd in traverser
