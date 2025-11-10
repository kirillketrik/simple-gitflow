from animals import Animal


def main():
    animals: list[Animal] = [

    ]

    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.speak()}")


if __name__ == '__main__':
    main()
