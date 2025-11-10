from animals import Animal, Cat, Dog


def main():
    animals: list[Animal] = [
        Cat(),
        Dog()
    ]

    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.speak()}")


if __name__ == '__main__':
    main()
