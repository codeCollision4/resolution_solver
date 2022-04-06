from logic_classes import Clause

class Resolution():
    def __init__(self, kb, test_clause):
        self.kb = kb
        self.test_clause = test_clause

    def resolution(self):
        # 1. Negating test clause and adding to knowledge base
        self.kb.add_negated_clause(self.test_clause.negate())

        # 2. Find 2 clauses to apply resolution rule
        n = len(self.kb.list)
        i = 0
        # Search previous clauses for current clause i, j is prev clauses
        while i <= n:
            j = 0
            while j < i:
                # i is index of first clause in kb, j is index of second clause
                # Start resolving each prev clause to i
                i_clause = self.kb.list[i]
                j_clause = self.kb.list[j]
                # Find intersecting literals, getting smallest set first
                min_set = min(i_clause.contains, j_clause.contains, key=len)
                max_set = max(j_clause.contains, i_clause.cotains, key=len)
                for lit in min_set:
                    # If it has the ~ symbol and its opposite is in the other clasue can resolve
                    if lit.negated:
                        if lit.atom in max_set:
                            self.create_clause(lit, lit.atom, min_set, max_set) # remove literals from i and j, left is negated right is not
                    else:
                        if '~' + lit in max_set:
                            self.create_clause(lit, '~' + lit, min_set, max_set) # Right is negated left is not, based on i and j


    # Change form to standard form

    # Add to kb


    '''
    Helper Functions
    '''
    def create_clause(self, min_lit, max_lit, min_clause, max_clause):
        # Combining clauses to then remove resolved lierals for new clause
        literals = min_clause.literals + max_clause.literals
        contains = min_clause.union(max_clause)
        hash = {**min_clause.hash, **max_clause.hash}

        # Deleting resolved literals
        min_idx = min_clause.hash[min_lit]
        del hash[min_lit] # From dict
        contains.remove(min_lit) # From set
        del literals[min_idx] # From list

        max_idx = max_clause.hash[max_lit] + (len(min_clause.literals) - 1) # Subtracting the len of left array minus the removed lit for index of max on "right"
        del hash[max_lit]
        contains.remove(max_lit)
        del literals[max_idx]

        # Updating hash for new clause, might need to optimize TODO
        for idx, lit in enumerate(literals):
            hash[lit] = idx





        