# kan ik tree's wel los testen van traversers en validators?
class Advanced_SetTreeChildren_Testcase(unittest.Tescase):
    def setUp(self):
        self.a = tree.Tree('A')

        self.b = tree.Tree('B')
        self.c = tree.Tree('C')
        self.d = tree.Tree('D')
        
        class NewTree(tree.Tree):
            pass
            
        self.nT = NewTree('nT')
        
        
    def test_set_tree_subclass_instance_as_child(self):
        '''Test setting children to instance of a Tree subclass'''
        expected_result = [type( tree.Tree() ), type( NewTree() )]

        self.a.children = [self.b, self.nT]
        type_list = [type(c) for c in self.a.children]

        self.assertEqual( type_list, expected_result)
        
    def test_set_non_tree_as_child(self):
        '''Test setting children to non tree items (should raise an error)'''
        with self.assertRaises(TypeError):
            self.a.children = [self.b, 'wrong_type', self.d]
            
    def test_set_self_as_child(self):
        '''Test setting a Tree as it's own child (should raise an error)'''
        with self.assertRaises(ValueError):
            self.a.children = [self.b, self.a]
            
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
            
