import argparse
from pathlib import Path
from logic_classes import Literal, Clause, KnowledgeBase
from resolution import resolution

def main():
    #Command Line Parser
    parser = argparse.ArgumentParser()
    # Positional Arguments
    parser.add_argument("input",
                        help="Path to a .kb file that holds list of clauses",
                        type=Path
                        )

    # Parse input
    args = parser.parse_args()

    if args.input.exists() and args.input.is_file():
        # Looping thru file
        with args.input.open() as f:
            kb = KnowledgeBase()
            # Creating knowledge base with clauses
            for idx, line in enumerate(f, start=1):
                lits = line.split()
                literals = []
                contain = set()
                hash = {}
                for idx, lit in enumerate(lits):
                    contain.add(lit) # Set to quickly see if shared literals btw clauses
                    hash["lit"] = idx # Hash map to find said literals in array
                    literals.append(Literal(lit)) # Array of literals
                clause = Clause(literals, contain, hash, idx)
                kb.add_clause(clause)

        # Getting test clause from end of list
        test_clause = kb.remove_clause()
        
        # Calling resolution algorithm
        resolution(kb, test_clause)
       

        for c in kb.list:
            print(c.index)
        print(test_clause)
        print(kb)
                        
    else:
        print("Please provide a .kb file that exists. Make sure you are not just providing a directory.")
        exit()

if __name__ == '__main__':
    main()