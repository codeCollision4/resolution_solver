


# Holds atoms and whether the are negated, to be used in a clause
class Literal():
    def __init__(self, lit):
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
        self.hash = hash
        
    def negate(self):
        for idx, lit in enumerate(self.literals):
            # Swapping negation sign
            if lit.negated:
                self.literals[idx] = lit.atom
            else:
                self.literals[idx] = '~' + lit.atom
        return self
    
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
            self.list.append(Clause(lit, len(self.list)+1))
        
    def __str__(self):
        return str(self.list)
    
    def __repr__(self):
        return str(self.list)

    






    

        

        

