import random
people = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Laurel",
    "Michael",
    "Oliver",
    "Victor",
    "William",
    "Chris"
]
possessives = [
    "my",
    "your",
    "their",
    "his",
    "her",
    "the"
]
objects = [
    "moon",
    "sun",
    "country"
]
adjectives = [
    "quick",
    "brown",
    "lazy",
    "red",
    "white",
    "black",
    "slow",
    "busy"
]
nouns = people.copy()
nouns.extend(objects)
def generate():
    r = random.choice
    secret_questions = [
        f"Why did {r(people)} take over {r(possessives)} {r(objects)}?",
        f"The {r(adjectives)} {r(adjectives)} {r(nouns)} jumped over the {r(adjectives)} {r(nouns)}."
    ]
    return random.choice(secret_questions)
if __name__ == '__main__':
    print(generate())