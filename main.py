import argparse
from pathlib import Path
from logic_classes import Literal, Clause, KnowledgeBase
from resolution import Resolution

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
                for id, lit in enumerate(lits):
                    big_lit = Literal(lit)
                    contain.add(big_lit) # Set to quickly see if shared literals btw clauses
                    hash[lit] = id # Hash map to find said literals in array
                    literals.append(big_lit) # Array of literals
                clause = Clause(literals, contain, hash, idx)
                kb.add_clause(clause)

        # Getting test clause from end of list
        test_clause = kb.remove_clause()
        
        # Calling resolution algorithm
        solver = Resolution(kb, test_clause)
        solver.resolution()
       

        # for c in kb.list:
        #     for l in c.literals:
        #         print(l)
        #         print(type(l))
        #     print(c.index)
        #     print(c.contains)
        #     print(c.hash)
        # print(test_clause)
        # print(kb)


        
                        
    else:
        print("Please provide a .kb file that exists. Make sure you are not just providing a directory.")
        exit()

if __name__ == '__main__':
    main()