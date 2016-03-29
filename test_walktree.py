import unittest
import tree
import walktree

class DomainAndArguments_TestCase(unittest.TestCase):
    def setUp(self):
        self.tA = tree.Tree('tA')

        self.tB = tree.Tree('tB')
        self.tC = tree.Tree('tC')
        self.tD = tree.Tree('tD')

        self.tA.children = [self.tB, self.tC, self.tD]

    def test_childtraverser_right_kwarg_is_applicable(self):
        ''' Test if the childtraverser is applicable when children is in kwarg'''
        traverser = walktree.ChildTraverser(self.tA, traverse_node_type = 'children')
        self.assertTrue(traverser.is_applicable)

    def test_childtraverser_right_arg_is_applicable(self):
        ''' Test if the childtraverser is applicable when children is in arg'''
        traverser = walktree.ChildTraverser(self.tA, 'children')
        self.assertTrue(traverser.is_applicable)

    def test_childtraverser_wrong_kwarg_key_is_applicable(self):
        ''' Test if the childtraverser is applicable when children wrong key in kwargs'''
        traverser = walktree.ChildTraverser(self.tA, traverse_order = 'children')
        self.assertFalse(traverser.is_applicable)

    def test_childtraverser_wrong_kwarg_value_is_applicable(self):
        ''' Test if the childtraverser is applicable when wrong value in kwargs'''
        traverser = walktree.ChildTraverser(self.tA, traverse_node_type = 'descendants')
        self.assertFalse(traverser.is_applicable)

    def test_childtraverser_wrong_arg_is_applicable(self):
        ''' Test if the childtraverser is applicable when wrong item in args'''
        traverser = walktree.ChildTraverser(self.tA, 'descendants')
        self.assertFalse(traverser.is_applicable)
        
        
        
    def test_DescendantWidthTraverser_right_kwarg_is_applicable(self):
        ''' Test if the DescendantWidthTraverser is applicable when descendants is in kwarg'''
        traverser = walktree.DescendantWidthTraverser(self.tA, traverse_node_type = 'descendants',
                                                      traverse_order = 'width')
        self.assertTrue(traverser.is_applicable)

    def test_DescendantWidthTraverser_right_arg_is_applicable(self):
        ''' Test if the DescendantWidthTraverser is applicable when descendants is in kwarg'''
        traverser = walktree.DescendantWidthTraverser(self.tA,'descendants', 'width')
        self.assertTrue(traverser.is_applicable)


if __name__ == '__main__':
    unittest.main()

#what if no tree is defined? (does that ever hapen?)
