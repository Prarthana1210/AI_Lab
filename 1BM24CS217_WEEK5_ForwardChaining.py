facts = {
    ("Student", "John"),
    ("Intelligent", "John")
}

rules = [
    (
        [("Student", "X")],
        ("Hardworking", "X")
    ),
    (
        [("Hardworking", "X"), ("Intelligent", "X")],
        ("Succeeds", "X")
    )
]

goal = ("Succeeds", "John")


def forward_chaining(facts, rules, goal):

    facts = set(facts)

    while True:

        new_fact_added = False

        for conditions, conclusion in rules:

            for fact in facts.copy():

                substitution = {}

                if len(conditions) == 1:

                    condition = conditions[0]

                    if condition[0] == fact[0]:

                        variable = condition[1]
                        value = fact[1]

                        substitution[variable] = value

                        new_conclusion = (
                            conclusion[0],
                            substitution[conclusion[1]]
                        )

                        if new_conclusion not in facts:
                            facts.add(new_conclusion)
                            new_fact_added = True

                            if new_conclusion == goal:
                                return True, facts

        if not new_fact_added:
            return False, facts


result, final_facts = forward_chaining(
    facts,
    rules,
    goal
)

print("Goal:", goal)
print("Result:", result)
print("Facts:", final_facts)