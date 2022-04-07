from logic_classes import Clause

# Main algorithm logic
class Resolution():
    def __init__(self, kb, test_clause):
        self.kb = kb
        self.test_clause = test_clause


    def resolution(self):
        # 1. Negating test clause and adding to knowledge base
        self.kb.add_negated_clause(self.test_clause)

        # Print Kb
        for c in self.kb.list:
            output_clause(self.kb, c)
        
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
                            self.checker(new_clause, i_clause, j_clause)
                            n = len(self.kb.list) - 1
                            # print(new_clause)
                            break
                    else:
                        if '~' + lit.atom in j_clause.contains:
                            new_clause = self.create_clause(str(lit), str('~' + lit.atom), i_clause, j_clause) # Right is negated left is not, based on i and j
                            self.checker(new_clause, i_clause, j_clause)
                            n = len(self.kb.list) - 1
                            # print(new_clause)
                            break
                j += 1
            i += 1
     



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
            hash[str(lit)] = idx
        
        return Clause(literals, contains, hash, len(self.kb.list)+1) # TODO +1?


    def is_repeated(self, clause):
        return len(clause.contains) != len(clause.literals)
    
    def is_true(self, clause):
        hold = False
        for lit in clause.contains:
            # Negated lit
            if lit[0] == '~':
                hold = lit[1] in clause.contains
            else:
                # Normal lit
                hold = ('~' + lit) in clause.contains
        
        return hold

    def is_redundant(self, clause):
        return str(clause) in self.kb.hash
    
    def checker(self, clause, i_clause, j_clause):
        c = False
        r = True
        i = i_clause.index
        j = j_clause.index
        # Repeated literals Check
        if not self.is_repeated(clause):
            # True Check aka no ~p and p in same clause
            if not self.is_true(clause):
                # Redundant logic/clause check
                if not self.is_redundant(clause):
                    # Contradiction check, if null/None then Valid else print and move on
                    if not clause.contains:
                        c = True
                    else:
                        c = False
                    
                    # Add clause to KB
                    self.kb.add_clause(clause)
                    
                    # Print clause
                    output_clause(self.kb, clause, i_idx=i, j_idx=j, resolved=r, contra=c)
        
def output_clause(kb, clause, i_idx=0, j_idx=0, resolved=False, contra=False):
    out = "{}. ".format(clause.index)
    
    if contra and resolved:
        out += "Contradiction {{{}, {}}}".format(i_idx,j_idx)
        print(out)
        print("Valid")
        exit()
        
    if not contra:
        # Building rest of string
        for lit in clause.literals:
            out += "{} ".format(lit)
    
    # No resolution
    if not resolved and not contra:
        out += "{}"
        print(out)
    # Resolved but not contradiction
    elif resolved and not contra:
        out += "{{{}, {}}}".format(i_idx, j_idx)
        print(out)
    
    
    
    
    
# 1. ∼p q {}
# 2. ∼z y {}
# 3. p {}
# 4. z {}
# 5. ∼y {}
# 6. q {3, 1}
# 7. y {4, 2}
# 8. ∼z {5, 2}
# 6. Contradiction {7, 5}
# Valid


