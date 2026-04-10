import cProfile as CP

def pythagorean_triples(n):
    triples = []
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if a*a + b*b == c*c:
                    triples.append((a, b, c))
    return triples

CP.run("pythagorean_triples(100)");