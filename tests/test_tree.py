import unittest
import tree.tree as tree

def child_names(tree):
    '''Returns a list of child names for given tree'''
    return [c.name for c in tree.children]   
    

    
    
class Set_TreeChildren_Testcase(unittest.TestCase):
    def setUp(self):
        self.a = tree.Tree('A')
        self.b = tree.Tree('B')
        self.c = tree.Tree('C')
        self.d = tree.Tree('D')

    def test_empty_children(self):
        ''' Test if an empty iterator is returned when there are no children '''
        self.assertEqual( child_names(self.a), [])

    def test_set_children_from_keyword_argument(self):
        '''Test setting tree children with keyword argument'''
        e = tree.Tree('e', children = self.b)
        self.assertEqual(child_names(e), ['B'])  
        
    def test_set_children_from_positional_argument(self):
        '''Test setting tree children with positional argument'''
        e = tree.Tree('e', self.b)
        self.assertEqual( child_names(e), ['B'])  
        
    def test_set_children_from_single(self):
        '''Test setting tree children with a single tree'''
        self.a.children = self.b
        self.assertEqual( child_names(self.a), ['B'])

    def test_set_children_from_list(self):
        '''Test setting Tree children from a list'''
        self.a.children = [self.b, self.c, self.d]
        self.assertEqual( child_names(self.a), ['B', 'C', 'D'])

    def test_set_children_from_iterator(self):
        '''Test setting tree children from an iterator'''
        self.a.children = iter([self.b, self.c, self.d])
        self.assertEqual( child_names(self.a), ['B', 'C', 'D'])
        
    def test_set_childeren_from_traverser(self):
        '''Test setting tree children from a TreeTraverser'''
        self.a.children = [self.b, self.c, self.d]
        e = tree.Tree('E', children = self.a.children)
        self.assertEqual( child_names(e), ['B', 'C', 'D'])

class Clear_TreeChildren_Testcase(unittest.TestCase):
    def setUp(self):
        self.a = tree.Tree('A')
        self.b = tree.Tree('B')
        self.c = tree.Tree('C')
        self.d = tree.Tree('D')
        self.a.children = [self.b, self.c, self.d]
        
    def test_clear_children_with_none(self):
        ''' Test if setting children to None, clears the children'''
        self.a.children = None
        self.assertEqual( list(self.a.children), [])
        
    def test_clear_children_with_empty_list(self):
        ''' Test if setting children to empty list, clears the children'''
        self.a.children = []
        self.assertEqual( list(self.a.children), [])
        
    def test_clear_children_with_empty_iterator(self):
        ''' Test if setting children to empty iterator, clears the children'''
        self.a.children = iter([])
        self.assertEqual( list(self.a.children), [])
              
class Switch_TreeChildren_Testcase(unittest.TestCase):
    def setUp(self):
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #
        # tree('E')
        
        self.d = tree.Tree('D')
        self.c = tree.Tree('C', children = self.d)
        self.b = tree.Tree('B', children = self.c)
        self.a = tree.Tree('A', children = self.b)
        
        self.e = tree.Tree('E')
        
    def test_switch_leaf_to_orphan(self):
        '''Test set children equivalent to leaf.parent = orphan'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #
        # tree('E')
        #   tree('D')
        
        self.e.children = self.d
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), [])
        self.assertEqual( child_names(self.e), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.d.parent.name, 'E')
        
    def test_switch_leaf_to_branch(self):
        '''Test set children equivalent to leaf.parent = branch'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #     tree('D')
        
        self.b.children = [self.c, self.d]
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C', 'D'])
        self.assertEqual( child_names(self.c), [])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'B')
        
    def test_switch_leaf_to_root(self):
        '''Test set children equivalent to leaf.parent = root'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #   tree('D')
        
        self.a.children = [self.b, self.d]
        
        self.assertEqual( child_names(self.a), ['B', 'D'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'A')
        
    def test_switching_branch_to_orphan(self):
        '''Test set children equivalent to branch.parent = orphan'''
        # tree('A')
        #   tree('B')
        #
        # tree('E')       
        #   tree('C')
        #     tree('D')

        self.e.children = self.c
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.e), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.c.parent.name, 'E')
        self.assertEqual( self.d.parent.name, 'C')

    def test_switching_branch_to_root(self):
        '''Test set children equivalent to branch.parent = root'''
        # tree('A')
        #   tree('B')
        #   tree('C')
        #     tree('D')
        
        self.a.children = [self.b, self.c]
        
        self.assertEqual( child_names(self.a), ['B', 'C'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'A')
        self.assertEqual( self.d.parent.name, 'C')

    def test_switching_orphan_to_leaf(self):
        '''Test set children equivalent to orphan.parent = leaf'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #          tree('E')
        
        self.d.children = self.e
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), ['E'])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'D')
        
    def test_switching_orphan_to_branch(self):
        '''Test set children equivalent to orphan.parent = branch'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #     tree('E')
        
        self.b.children = [self.c, self.e]
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C', 'E'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'B')
        
    def test_switching_orphan_to_root(self):
        '''Test set children equivalent to orphan.parent = root'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #   tree('E')  
        
        self.a.children = [self.b, self.e]
        
        self.assertEqual( child_names(self.a), ['B', 'E'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'A')
        
    def test_switching_root_to_orphaned_tree(self):
        '''Test switching a root to a tree that is orphaned'''
        # tree('E')
        #   tree('A')
        #     tree('B')
        #       tree('C')
        #          tree('D')
        
        self.e.children = self.a
        
        self.assertEqual( child_names(self.e), ['A'])
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.a.parent.name, 'E')
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')


    def test_switch_multiple_to_orphan(self):
        '''Test set multiple children equivalent to orphan.parent = leaf'''
        # tree('E')
        #   tree('A')
        #   tree('B')
        #   tree('C')
        #   tree('D')
        
        self.e.children = [self.a, self.b, self.c, self.d]
        
        self.assertEqual( child_names(self.e), ['A', 'B', 'C', 'D'])
        self.assertEqual( child_names(self.a), [])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.c), [])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.a.parent.name, 'E')
        self.assertEqual( self.b.parent.name, 'E')
        self.assertEqual( self.c.parent.name, 'E')
        self.assertEqual( self.d.parent.name, 'E')
        
    def test_switch_multiple_to_root(self):
        '''Test set multiple children equivalent to leaf.parent = orphan'''
        # tree('A')
        #   tree('B')
        #   tree('C') 
        #   tree('D')
        #   tree('E')
        
        self.a.children = [self.b, self.c, self.d, self.e]
        
        self.assertEqual( child_names(self.a), ['B', 'C', 'D', 'E'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.c), [])
        self.assertEqual( child_names(self.d), [])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'A')
        self.assertEqual( self.d.parent.name, 'A')
        self.assertEqual( self.e.parent.name, 'A')
        
    def test_switch_multiple_to_branch(self):
        '''Test set multiple children equivalent to branch.parent = branch'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #       tree('D')
        #     tree('E')
        #       tree('F')
        #     tree('G')
        
        f = tree.Tree('F', parent = self.e)
        g = tree.Tree('G')
        self.b.children = [self.c, self.e, g]
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C', 'E', 'G'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        self.assertEqual( child_names(self.e), ['F'])
        self.assertEqual( child_names(f), [])
        self.assertEqual( child_names(g), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'B')
        self.assertEqual( f.parent.name, 'E')
        self.assertEqual( g.parent.name, 'B')
           
class Set_TreeParent_Testcase(unittest.TestCase):
    def setUp(self):
        self.a = tree.Tree('A')
        self.b = tree.Tree('B')

    def test_empty_parent(self):
        ''' Test if None is returned when there is no parent '''
        self.assertEqual( self.a.parent, None)

    def test_set_parent_from_keyword_argument(self):
        '''Test setting tree parent with keyword argument'''
        e = tree.Tree('e', parent = self.b)
        self.assertEqual(e.parent.name, 'B')  
        
    def test_set_parent_from_positional_argument(self):
        '''Test setting tree parent with positional argument'''
        e = tree.Tree('e', [], self.b)
        self.assertEqual( e.parent.name, 'B')  
        
    def test_set_parent_from_tree(self):
        '''Test setting tree parent'''
        self.a.parent = self.b
        self.assertEqual( self.a.parent.name, 'B') 

class Clear_TreeParent_Testcase(unittest.TestCase):
    def setUp(self):
        self.a = tree.Tree('A')
        self.b = tree.Tree('B')
        self.a.parent = self.b
        
    def test_clear_parent_with_none(self):
        ''' Test if setting parent to None, clears the parent'''
        self.a.parent = None
        self.assertEqual( self.a.parent, None)      
         
class Switch_TreeParent_Testcase(unittest.TestCase):
    def setUp(self):
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #
        # tree('E')
        
        self.d = tree.Tree('D')
        self.c = tree.Tree('C', children = self.d)
        self.b = tree.Tree('B', children = self.c)
        self.a = tree.Tree('A', children = self.b)
        
        self.e = tree.Tree('E')
        
    def test_switch_leaf_to_orphan(self):
        '''Test set leaf.parent = orphan'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #
        # tree('E')
        #   tree('D')
        
        self.d.parent = self.e
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), [])
        self.assertEqual( child_names(self.e), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.d.parent.name, 'E')
        
    def test_switch_leaf_to_branch(self):
        '''Test set leaf.parent = branch'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #     tree('D')
        
        self.d.parent = self.b
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C', 'D'])
        self.assertEqual( child_names(self.c), [])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'B')
        
    def test_switch_leaf_to_root(self):
        '''Test set leaf.parent = root'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #   tree('D')
        
        self.d.parent = self.a
        
        self.assertEqual( child_names(self.a), ['B', 'D'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'A')
        
    def test_switching_branch_to_orphan(self):
        '''Test set branch.parent = orphan'''
        # tree('A')
        #   tree('B')
        #
        # tree('E')       
        #   tree('C')
        #     tree('D')

        self.c.parent = self.e
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.e), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.c.parent.name, 'E')
        self.assertEqual( self.d.parent.name, 'C')

    def test_switching_branch_to_root(self):
        '''Test set branch.parent = root'''
        # tree('A')
        #   tree('B')
        #   tree('C')
        #     tree('D')
        
        self.c.parent = self.a
        
        self.assertEqual( child_names(self.a), ['B', 'C'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'A')
        self.assertEqual( self.d.parent.name, 'C')

    def test_switching_orphan_to_leaf(self):
        '''Test set orphan.parent = leaf'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #          tree('E')
        
        self.e.parent = self.d
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), ['E'])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'D')
        
    def test_switching_orphan_to_branch(self):
        '''Test set orphan.parent = branch'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #     tree('E')
        
        self.e.parent = self.b
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C', 'E'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'B')
        
    def test_switching_orphan_to_root(self):
        '''Test set orphan.parent = root'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #   tree('E')  
        
        self.e.parent = self.a
        
        self.assertEqual( child_names(self.a), ['B', 'E'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'A')
        
    def test_switching_root_to_orphaned_tree(self):
        '''Test switching a root to a tree that is orphaned'''
        # tree('E')
        #   tree('A')
        #     tree('B')
        #       tree('C')
        #          tree('D')
        
        self.a.parent = self.e
        
        self.assertEqual( child_names(self.e), ['A'])
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.a.parent.name, 'E')
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
      
class Add_Children_Testcase(unittest.TestCase):
    def setUp(self):
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #
        # tree('E')
        
        self.d = tree.Tree('D')
        self.c = tree.Tree('C', children = self.d)
        self.b = tree.Tree('B', children = self.c)
        self.a = tree.Tree('A', children = self.b)
        
        self.e = tree.Tree('E')
    
    def add_none_as_child_to_orphan(self):
        '''Test if adding a None object to children of an orphan returns None'''
        self.e.add_children(None)
        self.assertEqual( child_names(self.e), [])
        
    def add_single_child_to_orphan(self):
        '''Test adding a single child to an orphan'''
        self.e.add_children(tree.Tree('F'))
        self.assertEqual( child_names(self.e), ['F'])
        
    def add_multiple_childrem_to_orphan(self):
        '''Test adding multiple children to an orphan'''
        self.e.add_children([tree.Tree('F'), tree.Tree('G')])
        self.assertEqual( child_names(self.e), ['F','G'])
        
    def add_none_as_child_to_branch(self):
        '''Test if adding a None object to children of a branch doesn't change children'''
        self.b.add_children(None)
        self.assertEqual( child_names(self.b), ['C'])
        
    def add_empty_list_as_child_to_branch(self):
        '''Test if adding a empty list to children of a branch doesn't change children'''
        self.b.add_children([])
        self.assertEqual( child_names(self.b), ['C'])
        
    def add_single_child_to_branch(self):
        '''Test adding a single child to a branch'''
        self.b.add_children(self.e)
        self.assertEqual( child_names(self.b), ['C', 'E'])
        
    def add_multiple_childrem_to_branch(self):
        '''Test adding multiple children to a branch'''
        self.b.add_children([self.e, tree.Tree('F')])
        self.assertEqual( child_names(self.b), ['C', 'E', 'F'])
    
    def add_leaf_to_orphan(self):
        '''Test add children to orphan'''
        # tree('A')
        #   tree('B')
        #
        # tree('E')
        #   tree('C')
        #   tree('D') 
        
        self.e.add_children([self.c, self.d])
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.e), ['C', 'D'])
        self.assertEqual( child_names(self.c), [])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.c.parent.name, 'E')
        self.assertEqual( self.d.parent.name, 'E')
        
    def test_switch_leaf_to_branch(self):
        '''Test set children equivalent to leaf.parent = branch'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #     tree('D')       
        #     tree('E')
        
        self.b.children = [self.c, self.d]
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C', 'D'])
        self.assertEqual( child_names(self.c), [])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'B')
        
    def test_switch_leaf_to_root(self):
        '''Test set children equivalent to leaf.parent = root'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #   tree('D')
        
        self.a.children = [self.b, self.d]
        
        self.assertEqual( child_names(self.a), ['B', 'D'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'A')
        
    def test_switching_branch_to_orphan(self):
        '''Test set children equivalent to branch.parent = orphan'''
        # tree('A')
        #   tree('B')
        #
        # tree('E')       
        #   tree('C')
        #     tree('D')

        self.e.children = self.c
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.e), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.c.parent.name, 'E')
        self.assertEqual( self.d.parent.name, 'C')

    def test_switching_branch_to_root(self):
        '''Test set children equivalent to branch.parent = root'''
        # tree('A')
        #   tree('B')
        #   tree('C')
        #     tree('D')
        
        self.a.children = [self.b, self.c]
        
        self.assertEqual( child_names(self.a), ['B', 'C'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'A')
        self.assertEqual( self.d.parent.name, 'C')

    def test_switching_orphan_to_leaf(self):
        '''Test set children equivalent to orphan.parent = leaf'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #          tree('E')
        
        self.d.children = self.e
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), ['E'])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'D')
        
    def test_switching_orphan_to_branch(self):
        '''Test set children equivalent to orphan.parent = branch'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #     tree('E')
        
        self.b.children = [self.c, self.e]
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C', 'E'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'B')
        
    def test_switching_orphan_to_root(self):
        '''Test set children equivalent to orphan.parent = root'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        #   tree('E')  
        
        self.a.children = [self.b, self.e]
        
        self.assertEqual( child_names(self.a), ['B', 'E'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        self.assertEqual( child_names(self.e), [])
        
        self.assertEqual( self.a.parent, None)
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
        self.assertEqual( self.e.parent.name, 'A')
        
    def test_switching_root_to_orphaned_tree(self):
        '''Test switching a root to a tree that is orphaned'''
        # tree('E')
        #   tree('A')
        #     tree('B')
        #       tree('C')
        #          tree('D')
        
        self.e.children = self.a
        
        self.assertEqual( child_names(self.e), ['A'])
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
        self.assertEqual( self.e.parent, None)
        self.assertEqual( self.a.parent.name, 'E')
        self.assertEqual( self.b.parent.name, 'A')
        self.assertEqual( self.c.parent.name, 'B')
        self.assertEqual( self.d.parent.name, 'C')
 

# complexe scenario's testen waarbij er meerdere tree's van een structuur worden geadd als children bij een andere




if __name__ == '__main__':
    unittest.main()


