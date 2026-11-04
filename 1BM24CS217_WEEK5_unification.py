def is_variable(x):
    return isinstance(x, str) and x.isupper()


def occurs_check(variable, expression, substitutions):
    if variable == expression:
        return True

    if expression in substitutions:
        return occurs_check(
            variable,
            substitutions[expression],
            substitutions
        )

    return False


def unify(x, y, substitutions=None):

    if substitutions is None:
        substitutions = {}

    if x == y:
        return substitutions

    if is_variable(x):
        return unify_variable(x, y, substitutions)

    if is_variable(y):
        return unify_variable(y, x, substitutions)

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0]:
            return None

        if len(x) != len(y):
            return None

        for i in range(1, len(x)):
            substitutions = unify(
                x[i],
                y[i],
                substitutions
            )

            if substitutions is None:
                return None

        return substitutions

    return None


def unify_variable(variable, expression, substitutions):

    if variable in substitutions:
        return unify(
            substitutions[variable],
            expression,
            substitutions
        )

    if is_variable(expression) and expression in substitutions:
        return unify(
            variable,
            substitutions[expression],
            substitutions
        )

    if occurs_check(variable, expression, substitutions):
        return None

    substitutions[variable] = expression

    return substitutions


# TEST
expr1 = ("Parent", "X", "Y")
expr2 = ("Parent", "John", "Mary")

result1 = unify(expr1, expr2)

print(result1)

expr11 = ("Knows", "X", "X")
expr22 = ("Knows", "Ravi", "John")

result2 = unify(expr11, expr22)

print(result2)