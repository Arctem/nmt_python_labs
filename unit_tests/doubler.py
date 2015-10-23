def d(fname="lab99_ex1_easy.expected_input"):
    with open(fname) as f:
        n = int(f.read().split()[0])
        return str(n * 2 + n % 2)

if __name__ == "__main__":
    print(d())
