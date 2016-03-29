# hier komt een class die settings stored voor trees
# moet vanuit de tree nog wel gezorgd worden dat alleen de root de settings heeft


        # als we dit in een settings object doen, is de hele init niet nodig van Tree
        self.default_traversal_order = 'width'
        self.default_filter_order = 'post_traversal'


    # tree settings
    # misschien moet dit in een appart settings object.
    # Dus Tree.settings.traversal_order('width')
    @property
    def default_traversal_order(self):
        '''returns default traversal method used when getting children'''
        return self._default_traversal_order

    @default_traversal_order.setter
    def default_traversal_order(self, traversal_order=''):
        '''sets default traversal order used when getting descendants'''
        # VALIDATOR voor gebruiken
        # settings moeten alleen opgeslagen en verandert kunnen worden op de root node.
        # anders kunnen er rare dingen gebeuren
        # en het moet ook aangepast worden als er van parent verandert wordt
        self._default_traversal_order = traversal_order
