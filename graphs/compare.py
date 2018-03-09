
# =============================================================================
class TreeNode():

    # -------------------------------------------------------------------------
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.left = None
        self.right = None

    # -------------------------------------------------------------------------
    def contains_subtree(self, sub):
        if sub is None:
            return True  # empty tree is always subtree
        def match_subtree(T1, T2):
            if T1 is None and T2 is None:
                return True
            if T1 is None or T2 is None:
                return False
            if T1.value != T2.value:
                return False
            return match_subtree(T1.right, T2.right) and match_subtree(T1.left, T2.left)
        def is_subtree(T1, T2):
            if T1 is None or T2 is None:
                return False  # exhausted tree
            if T1.value == T2.value and match_subtree(T1, T2):  # evaluate from root
                return True
            return match_subtree(T1.left, T2) or match_subtree(T1.right, T2)
        return is_subtree(self, sub)

    # -------------------------------------------------------------------------
    def find_subtree(self, value):
        finder = self
        while finder.value != value:
            if value > finder.value:
                finder = finder.right
            else:
                finder = finder.left
        return finder

    # -------------------------------------------------------------------------
    def append(self, value):
        finder = self
        while finder is not None:
            parent = finder
            if value > finder.value:
                finder = finder.right
            elif value < finder.value:
                finder = finder.left
            else:
                raise Exception('%s == %s' % (str(value), str(finder.value)))
        finder = TreeNode(value)
        if value > parent.value:
            parent.right = finder
        else:
            parent.left = finder

    # -------------------------------------------------------------------------
    def __str__(self):
        return '%s%s%s' % (
            str(self.value),
            (' >%s' % str(self.right) if self.right is not None else ''),
            (' <%s' % str(self.left) if self.left is not None else '')
        )


# =============================================================================
if __name__ == '__main__':

    t1 = TreeNode(5)
    map(t1.append, [4, 1, 6, 3, 0, 9, 2, 7, 8])
    print str(t1)

    t2 = t1.find_subtree(6)
    print str(t2)
    print t1.contains_subtree(t2)

    t2.append(4)
    print str(t2)
    print t1.contains_subtree(t2)
