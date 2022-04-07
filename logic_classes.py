
# Logic Classes used in resolution algorithm

# Holds atoms and whether the are negated, to be used in a clause
class Literal():
    def __init__(self, lit):
        self.lit = lit
        # Checking if atom is negated
        if lit[0] == '~':
            self.negated = True
        else:
            self.negated = False
        # Char used for literal
        if self.negated:
            self.atom = lit[1]    
        else:
            self.atom = lit

    def __str__(self):
        return '~' + self.atom if self.negated else self.atom
        
    def __repr__(self):
        return '~' + self.atom if self.negated else self.atom

# Holds literals that are connected by OR 
class Clause():
    def __init__(self, lits, contain, hash, idx):
        self.index = idx # Number in KB
        self.literals = lits # List for literals in clause
        self.contains = contain # Set of literals in clause
        self.hash = hash # Hash map to quickly access literals
        
    def __str__(self):
        return str(self.literals)
    
    def __repr__(self):
        return str(self.literals)

class KnowledgeBase():
    def __init__(self):
        self.list = []
        
    def add_clause(self, clause):
        self.list.append(clause)
    
    def remove_clause(self):
        return self.list.pop()
    
    def add_negated_clause(self, clause):
        for lit in clause.literals:
            # Swapping negation sign
            contain = set()
            if lit.negated:
                big_lit = Literal(lit.atom)
                hash = {lit.atom:0}
                contain.add(lit.atom)
            else:
                big_lit = Literal('~' + lit.atom)
                hash = {'~' + lit.atom:0}
                contain.add('~' + lit.atom)
            literals = [big_lit]
            self.list.append(Clause(literals, contain, hash, len(self.list)+1))
        
    def __str__(self):
        return str(self.list)
    
    def __repr__(self):
        return str(self.list)

    






    

        

        

