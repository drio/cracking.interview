from recursion import hanoi

def run_hanoi():
    pegs = ["A", "B", "C"]
    p_from = "A"
    p_to = "C"
    hanoi(pegs, p_from, p_to, 3)

run_hanoi()



