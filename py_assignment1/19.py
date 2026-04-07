import cProfile

def pythagorean_triples(N):
    triples = []
    for a in range(1, N+1):
        for b in range(a, N+1):
            for c in range(b, N+1):
                if a*a + b*b == c*c:
                    triples.append((a, b, c))
    return triples

def main():
    pythagorean_triples(200)

if __name__ == "__main__":
    cProfile.run("main()")