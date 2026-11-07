def is_variable(x):
    return isinstance(x, str) and x[0].islower()

def substitute(term, subs):
    while isinstance(term, str) and term in subs:
        term = subs[term]
    return term

def unify(x, y, subs):
    x = substitute(x, subs)
    y = substitute(y, subs)

    if x == y:
        return subs

    if is_variable(x):
        subs[x] = y
        return subs

    if is_variable(y):
        subs[y] = x
        return subs

    if isinstance(x, tuple) and isinstance(y, tuple):

        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            subs = unify(a, b, subs)

            if subs is None:
                return None

        return subs

    return None


def unify_predicate(p1, p2):

    if p1[0] != p2[0]:
        return None

    if len(p1[1]) != len(p2[1]):
        return None

    subs = {}

    for a, b in zip(p1[1], p2[1]):
        subs = unify(a, b, subs)

        if subs is None:
            return None

    return subs


print("FIRST ORDER LOGIC - UNIFICATION")

p1 = ("Eats", ("x", "Apple"))
p2 = ("Eats", ("Riya", "y"))

print("\nExpression 1:", p1)
print("Expression 2:", p2)

result = unify_predicate(p1, p2)

if result is not None:
    print("\nUnification Successful!")
    print("Substitutions:")

    for key, value in result.items():
        print(key, "=", value)

    print("\nUnified Expression: Eats(Riya, Apple)")

else:
    print("\nUnification Failed!")
