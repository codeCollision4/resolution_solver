


# Holds atoms and whether the are negated, to be used in a clause
class Literal():
    def __init__(self, lit):
        # Checking if atom is negated
        if lit[0] == '~':
            self.negated = True
        else:
            self.negated = False
        # Char used for literal    
        self.atom = lit

    def __str__(self):
        return '~' + self.atom if self.negated else self.atom
        

# Holds literals that are connected by OR 
class Clause():
    def __init__(self, line, idx):
        self.index = idx # Number in KB
        self.literals = line.split() # Getting each literal from line












    def __str__(self):
        return str(self.literals)

        

        

