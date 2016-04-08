
        self.tree = tree
        self.default_traversal_order = 'width'
        self.default_filter_order = 'post_traversal'



    @property
    def default_traversal_order(self):
        '''returns default traversal method used when getting children'''
        return self._default_traversal_order

    @default_traversal_order.setter
    def default_traversal_order(self, traversal_order=''):
        '''sets default traversal order used when getting descendants'''
        self._default_traversal_order = traversal_order

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