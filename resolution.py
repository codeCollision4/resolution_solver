from logic_classes import Clause

class Resolution():
    def __init__(self, kb, test_clause):
        self.kb = kb
        self.test_clause = test_clause


    def resolution(self):
        # 1. Negating test clause and adding to knowledge base
        self.kb.add_negated_clause(self.test_clause)
        

        # 2. Find 2 clauses to apply resolution rule
        n = len(self.kb.list) - 1
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
                # TODO make Clause comparison use self.contains
                # min_set = min(i_clause.contains, j_clause.contains, key=len)
                # max_set = max(j_clause.contains, i_clause.cotains, key=len)
                for lit in i_clause.literals:
                    # If it has the ~ symbol and its opposite is in the other clasue can resolve
                    # print(lit)
                    # print(type(lit))
                    # print(self.kb.list)
                    if lit.negated:
                        if lit.atom in j_clause.contains:
                            new_clause = self.create_clause(str(lit), str(lit.atom), i_clause, j_clause) # remove literals from i and j, left is negated right is not
                            # print(new_clause)
                            break
                    else:
                        if '~' + lit.atom in j_clause.contains:
                            new_clause = self.create_clause(str(lit), str('~' + lit.atom), i_clause, j_clause) # Right is negated left is not, based on i and j
                            # print(new_clause)
                            break
                # repeated literal check
                j += 1
            i += 1

    # Change form to standard form

    # Add to kb


    '''
    Helper Functions
    '''
    # Resolves two clauses and creates a new one
    def create_clause(self, i_lit, j_lit, i_clause, j_clause):
        # Combining clauses to then remove resolved lierals for new clause
        literals = i_clause.literals + j_clause.literals
        contains = i_clause.contains.union(j_clause.contains)
        hash = {**i_clause.hash, **j_clause.hash}

        # Deleting resolved literals
        i_idx = i_clause.hash[i_lit]
        del hash[i_lit] # From dict
        contains.remove(i_lit) # From set
        del literals[i_idx] # From list

        j_idx = j_clause.hash[j_lit] + (len(i_clause.literals) - 1) # Subtracting the len of left array minus the removed lit for index of max on "right"
        del hash[j_lit]
        contains.remove(j_lit)
        del literals[j_idx]

        # Updating hash for new clause, might need to optimize TODO
        for idx, lit in enumerate(literals):
            hash[lit] = idx
        
        return Clause(literals, contains, hash, len(self.kb.list)) # TODO +1?


    def is_repeated(self):
        pass

        