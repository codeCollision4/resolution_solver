


def resolution(kb, test_clause):
    # 1. Negating test clause and adding to knowledge base
    kb.add_negated_clause(test_clause.negate())
    
    # 2. Find 2 clauses to apply resolution rule
    
    # Change form to standard form
    
    # Add to kb
    