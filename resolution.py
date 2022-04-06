


def resolution(kb, test_clause):
    # 1. Negating test clause and adding to knowledge base
    kb.add_negated_clause(test_clause.negate())
    
    # 2. Find 2 clauses to apply resolution rule
    n = len(kb.list)
    i = 0
    # Search previous clauses for current clause i, j is prev clauses
    while i < n:
        j = 0
        while j < i:
            pass
    
    # Change form to standard form
    
    # Add to kb
    