# used for displaying trees
# TreeViewer class

TreeViewer(self)

class TreeViewer(object):
    def __init__(self, tree):
        self.tree = tree
        
    def to_string(self, tree, name_only):
        '''returns tree as a string '''
        if name_only:
            return self.tree.name
        else:
            return unicode(self.tree)
    
    def indented_text(self, name_only = False):
        '''returns tree view as indented string'''
        view_string = self.to_string(self.tree, name_only)
        for t in tree.descendants.descendants_depthfirst():
            view_string += '\r\n{indent}{t}'.format(indent = '    '*tree.traits.depth, 
                                                    t = self.to_string(t, name_only) )
        return view_string
    
    def line_text(self, name_only = False):
        '''returns tree view as line drawing string, using unicode box-drawing characters'''
        view_string = self.to_string(self.tree, name_only)
        
        # row_elements are added in reverse order (starting from child)
        for d in self.tree.descendants_depthfirst():
            row_elements = [self.to_string(d, name_only)]
            
            # the last child has └ in front of it, instead of ├
            if d.parent.children(index = -1) == t:
                row_elements.append(u'\u2514\u2500\u2500\u2500') # '└───'
            else:
                row_elements.append(u'\u251C\u2500\u2500\u2500') # '├───'
            
            # check ancestors to see if we need any  │           
            for a in d.find.ancestors():
                if a.parent.children(index=-1) in [a, None]:
                    row_elements.append(u'    ')
                else:
                    row_elements.append(u'\u2502   ') # '│   '
            
            view_string += u'\r\n' + ''.join( reversed(row_elements) )
        return view_string
            
            