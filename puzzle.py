from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    And(Implication(AKnight, 
    And(AKnight,AKnave)), 
    Or(AKnave,AKnight))
)
print(knowledge0.formula())


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(AKnight,And(BKnave,AKnave)),
    Or(AKnave,AKnight),
    Or(BKnave,BKnight),
    Or(BKnight,Not(BKnave))

    # TODO
)
print(knowledge1.formula())


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(
        Biconditional(AKnight,
        Or(
            And(AKnight,BKnight),
            And(Not(AKnight), Not(BKnight))
        ))
    ),
    Biconditional(BKnight,
        Or(
            And(AKnight, Not(BKnight)),
            And(Not(AKnight),BKnight)
        )
    ),
    Or(AKnave,AKnight),
    Or(BKnave, BKnight)


    
    # TODO
)
print(knowledge2.formula())


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave,AKnight),
    Or(BKnight,BKnave),
    Or(CKnave,CKnight),
    And(
        Biconditional(BKnight,Not(CKnight)),
        Biconditional(CKnight,AKnight),
        Biconditional(BKnight,Not(CKnight)),
        Biconditional(CKnight,AKnight),
        Biconditional(BKnight,Biconditional(
            AKnight,AKnave
        )),
        Or(Biconditional(AKnight,AKnight), Biconditional(AKnight, AKnave))
    )


    # TODO
)
print(knowledge3.formula)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
