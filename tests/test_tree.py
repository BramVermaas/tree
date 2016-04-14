import unittest
import tree.tree as tree

def child_names(parent):
    '''Returns a list of child names for given parent'''
    return [c.name for c in parent.children]   

    
    
class Set_TreeChildren_Testcase(unittest.TestCase):
    def setUp(self):
        self.a = tree.Tree('A')
        self.b = tree.Tree('B')
        self.c = tree.Tree('C')
        self.d = tree.Tree('D')

    def test_empty_children(self):
        ''' Test if an empty iterator is returned when there are no children '''
        self.assertEqual( list(self.a.children), [])

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
        
        self.d = tree.Tree('D')
        self.c = tree.Tree('C', children = self.d)
        self.b = tree.Tree('B', children = self.c)
        self.a = tree.Tree('A', children = self.b)

    def test_switching_leaf_tree(self):
        '''Test switching a child that has no children of it's own'''
        # tree('A')
        #   tree('B')
        #     tree('C') 
        #   tree('D')
        
        self.a.children = [self.b, self.d]
        self.assertEqual( child_names(self.a), ['B', 'D'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.d), [])
        
    def test_switching_branch_tree(self):
        '''Test switching a child that does have children of it's own'''
        # tree('A')
        #   tree('B')
        #   tree('C')
        #     tree('D')
        
        self.a.children = [self.b, self.c]
        self.assertEqual( child_names(self.a), ['B', 'C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
        
    def test_switching_root_tree(self):
        '''Test switching a child to a tree that was first the root'''
        # tree('A')
        #   tree('B')
        #     tree('C')
        #        tree('D')
        
        # tree('D')
        #   tree('A')
        #      tree('B')
        #        tree('C')
        
        print 'test_switching_root_tree'
        
        self.d.children = self.a
        self.assertEqual( child_names(self.d), ['A'])
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), ['C'])
        self.assertEqual( child_names(self.c), [])

    def test_switching_to_orphaned_tree(self):
        '''Test switching a child to a tree has no parent'''
        # tree('A')
        #   tree('B')
        #
        # tree('E')
        #   tree('C')
        #     tree('D')
        
        e = tree.Tree('E', children = self.c)
        
        self.assertEqual( child_names(self.a), ['B'])
        self.assertEqual( child_names(self.b), [])
        self.assertEqual( child_names(e), ['C'])
        self.assertEqual( child_names(self.c), ['D'])
        self.assertEqual( child_names(self.d), [])
     
        
"""
def test_add_children_to_tree_without_children(self):
    ''' Test add children when a Tree has no children yet'''
    expected_result = ['B', 'C']

    self.a.add_children([self.b, self.c])
    names_list = [c.name for c in self.a.children]

    self.assertEqual( names_list, expected_result)
    
def test_add_children_to_tree_with_children(self):
    ''' Test add children when a Tree has no children yet'''
    #expected_result = ['B', 'C']

    #self.a.add_children([self.b, self.c])
    #names_list = [c.name for c in self.a.children]
    #
    #self.assertEqual( names_list, expected_result)
"""

# werkt de test ook als ik een parent met een child heb. en ik probeer dat child als child zijn parent te geven (circular)
# testen of het ook lukt om parent te zetten
# parent op none
# child setten of je de parent ook set en vice verse
#
# wat gebeurt er als ik een tree met 1 child heb. En ik gebruik niet add children
# maar ik doe tree.Tree(mychild2, parent = mytree)
# dus ik voeg hem toe doormiddel van het zetten van de parent
# (dan moet eigenlijk de add_children gebruikt worden)
#
# kan een tree duplicaten van children hebben?
# dus 2 children, en die zijn allebij childA
# (ik denk dat validtree daar voor moet checken)



if __name__ == '__main__':
    unittest.main()


