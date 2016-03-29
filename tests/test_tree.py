import unittest

import tree
import itertree


class SetTreeChildren_TestCase(unittest.TestCase):
    def setUp(self):
        self.tA = tree.Tree('tA')

        self.tB = tree.Tree('tB')
        self.tC = tree.Tree('tC')
        self.tD = tree.Tree('tD')

    def test_empty_children(self):
        ''' Test if an empty iterator is returned when there are no children '''
        self.assertEqual( list(self.tA.children), [])


    def test_set_childeren_from_single(self):
        '''Test setting tree children with a single tree'''
        expected_result = ['tB']

        self.tA.children = self.tB
        names_list = [c.name for c in self.tA.children]

        self.assertEqual( names_list, expected_result)

    def test_set_childeren_from_list(self):
        '''Test setting Tree children from a list by name'''
        expected_result = ['tB', 'tC', 'tD']

        self.tA.children = [self.tB, self.tC, self.tD]
        names_list = [c.name for c in self.tA.children]
        self.assertEqual( names_list, expected_result)


    def test_set_childeren_from_list(self):
        '''Test setting tree children from a list'''
        expected_result = ['tB', 'tC', 'tD']

        self.tA.children = [self.tB, self.tC, self.tD]
        names_list = [c.name for c in self.tA.children]

        self.assertEqual( names_list, expected_result)


    def test_clear_children(self):
        ''' Test if an empty iterator clear the children of a tree '''
        self.tA.children = [self.tB, self.tC, self.tD]
        self.tA.children = None

        self.assertEqual( list(self.tA.children), [])


    def test_set_childeren_from_itterator(self):
        '''Test setting tree children from an itterator'''
        expected_result = ['tB', 'tC', 'tD']

        self.tA.children = [self.tB, self.tC, self.tD]
        t_2 = tree.Tree('t_2')
        t_2.children = self.tA.children
        names_list = [c.name for c in t_2.children]

        self.assertEqual( names_list, expected_result)


    def test_set_tree_subclass_instance_as_child(self):
        '''Test setting children to instance of a Tree subclass'''
        class NewTree(tree.Tree):
            pass

        expected_result = [type( tree.Tree() ), type( NewTree() )]

        nT = NewTree('nT')
        self.tA.children = [self.tB, nT]
        type_list = [type(c) for c in self.tA.children]

        self.assertEqual( type_list, expected_result)


    def test_set_non_tree_as_child(self):
        '''Test setting children to non tree items (should raise an error)'''
        with self.assertRaises(TypeError):
            self.tA.children = [self.tB, 'wrong_type', self.tD]

    def test_set_self_as_child(self):
        '''Test setting a Tree as it's own child (should cause error)'''
        with self.assertRaises(ValueError):
            self.tA.children = [self.tB, self.tA]

    def test_switching_children_same_depth(self):
        '''Test setting Tree children from a list by name'''
        # voor de test moet ik weten of set default traversal goed werkt
        # doen we dat ook voor children (ja, anders krijgen we een hele rare mix)?
        # eigenlijk moet de default traversal alleen op de root gestored worden
        # of is het een class attribuut (kan dat?) NEE(want moet wel per tree anders moeten zijn)
        expected_result = ['tB', 'tC', 'tD']
        tA.children = [tB, tC]
        tC.children = tD

        tB.children = tD

        pass
        # tree('tA')
        #     tree('tB')
        #     tree('tC')
        #        tree('tD')
        #
        # tA.default_traversal_order = 'depth'
        # tA.children => [tB, tC, tD]
        #
        # -----------------
        # tB.children = tD
        #
        # tree('tA')
        #     tree('tB')
        #        tree('tD')
        #     tree('tC')
        #
        # tA.children => [tB, tD, tC]

        # tB.children = tD
        #self.tC.children = self.tA
        #self.tA.children = [self.tB, self.tC]

    def test_empty_children(self):
        ''' Test if an empty iterator is returned when there are no children '''
        self.assertEqual( list(self.tA.children), [])


    def test_add_children_to_tree_without_children(self):
        ''' Test add children when a Tree has no children yet'''
        expected_result = ['tB', 'tC']

        self.tA.add_children([self.tB, self.tC])
        names_list = [c.name for c in self.tA.children]

        self.assertEqual( names_list, expected_result)

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

    def test_add_children_to_tree_with_children(self):
        ''' Test add children when a Tree has no children yet'''
        #expected_result = ['tB', 'tC']

        #self.tA.add_children([self.tB, self.tC])
        #names_list = [c.name for c in self.tA.children]
        #
        #self.assertEqual( names_list, expected_result)

if __name__ == '__main__':
    unittest.main()

#bram, liselotte, joran, rianne, daniel, michelle = tree.Tree('Bram'), tree.Tree('Liselotte'), tree.Tree('Joran'), tree.Tree('Rianne'), tree.Tree('Daniel'), tree.Tree('Michelle')
#henk, marian, ans, john = tree.Tree('Henk'), tree.Tree('Marian'), tree.Tree('Ans'), tree.Tree('John')
#riet = tree.Tree('Riet')
#
#henk.children = [bram, liselotte]
#ans.children = [joran, rianne]
#john.children = [daniel, michelle]
#riet.children = [henk, marian, ans, john]
#
#print '\r\nriet children:'
#for d in riet.children:
#    print d
#
#
#print '\r\nriet descendants width first'
#for d in riet.descendants:
#     print d
#
#
#print '\r\nriet descendants depth first'
#riet.default_traversal_order = 'depth'
#for d in riet.descendants:
#    print d
#
#
#print '\r\njoran ancestors'
#for d in joran.ancestors:
#    print d
#
#print '\r\nbram ancestors'
#for d in bram.ancestors:
#    print d

#self.tA = tree.Tree('tA')
#
#self.tB = tree.Tree('tB')
#self.tC = tree.Tree('tC')
#self.tD = tree.Tree('tD')
#
#self.tE = tree.Tree('tE')
#self.tF = tree.Tree('tF')
#self.tG = tree.Tree('tG')
#
#self.tH = tree.Tree('tH')
#self.tI = tree.Tree('tI')
