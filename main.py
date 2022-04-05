import argparse
from pathlib import Path
from logic_classes import Clause

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
            kb = []
            # Getting all clauses, creating classes for them and then storing in list
            for idx, line in enumerate(f, start=1):
                clause = Clause(line, idx)
                kb.append(clause)

        # Getting test clause from end of list
        test_clause = kb.pop()

        for c in kb:
            print(c)
        print(test_clause)
                        
    else:
        print("Please provide a .kb file that exists. Make sure you are not just providing a directory.")
        exit()

if __name__ == '__main__':
    main()