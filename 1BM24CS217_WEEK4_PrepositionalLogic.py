from itertools import product

def implies(a, b):
    return (not a) or b

def check_entailment():
    symbols = ['P', 'Q', 'R']
    query = True

    print("P Q R | P->Q Q->R | KB | Query")

    entails = True

    for P, Q, R in product([True, False], repeat=3):

        s1 = implies(P, Q)
        s2 = implies(Q, R)
        s3 = P

        KB = s1 and s2 and s3
        query_value = R

        print(
            int(P), int(Q), int(R), "|",
            int(s1), int(s2), "|",
            int(KB), "|",
            int(query_value)
        )

        if KB and not query_value:
            entails = False

    if entails:
        print("\nKB entails the query R.")
    else:
        print("\nKB does not entail the query R.")

check_entailment()