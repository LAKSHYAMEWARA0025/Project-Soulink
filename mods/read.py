def read_persona(file = "static/data/persona_v1.01.txt"):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    print(read_persona())