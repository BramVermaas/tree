class TreeSettings(object):
    '''Stores settings for tree objects'''
    def __init__(self, tree):
        self.tree = tree
        self.traversal_order = 'width'
        self.filter_order = 'post_traversal'



    @property
    def traversal_order(self):
        '''returns default traversal method used when getting children'''
        return self._traversal_order

    @traversal_order.setter
    def traversal_order(self, traversal_order=''):
        '''sets default traversal order used when getting descendants'''
        self._traversal_order = traversal_order

    def check_traversal_order(self):
        traversal_order_type = type(self.traversal_order)
        if not traversal_order_type == str:
            raise TypeError('Unexpected traversal order type: ' \
                            '{traversal_type}. Can only be of type str.'.format(
                            traversal_type = traversal_order_type))
        if not self.traversal_order in ['depth', 'width']:
            raise ValueError("Unexpected traversal order value: {traversal_order}." \
                             "Allowed values are only 'depth' or 'width.'".format(
                             traversal_order = self.traversal_order))