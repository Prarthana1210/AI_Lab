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

                if len(conditions) == 1:

                    condition = conditions[0]

                    if condition[0] == fact[0]:

                        variable = condition[1]
                        value = fact[1]

                        new_conclusion = (
                            conclusion[0],
                            value
                        )

                        if new_conclusion not in facts:

                            facts.add(new_conclusion)
                            new_fact_added = True

                            if new_conclusion == goal:
                                return True, facts

                else:

                    variable = conditions[0][1]

                    matching_value = None
                    all_match = True

                    for condition in conditions:

                        expected_predicate = condition[0]

                        found = False

                        for f in facts:

                            if f[0] == expected_predicate:

                                if matching_value is None:
                                    matching_value = f[1]
                                    found = True

                                elif f[1] == matching_value:
                                    found = True

                        if not found:
                            all_match = False
                            break

                    if all_match:

                        new_conclusion = (
                            conclusion[0],
                            matching_value
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