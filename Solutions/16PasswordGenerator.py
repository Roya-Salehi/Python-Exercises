import random
import string


def main():
    def pass_gen_simple_solution(lenght):
        return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=lenght))

    def pass_gen_short_solution(lenght):
        return "".join(random.choices(string.printable[:94], k=lenght))

    listOfRandomWords = ["Bumfuzzle", "Cattywampus", "Gardyloo", "Taradiddle", "Snickersnee",
                         "Widdershins", "Collywobbles", "Gubbins", "Abibliophobia", "Bumbershoot"]

    strenght = input(
        "Enter 's' for a strong password, or 'w' for a weak password: ").lower()

    if strenght == 's':
        lenght = int(input("Enter the lenght of the password: "))
        passw1 = pass_gen_simple_solution(lenght)
        passw2 = pass_gen_short_solution(lenght)
        print(passw1, passw2, sep="\n")

    else:
        def weakpass(): return "".join(random.choices(
            listOfRandomWords, k=random.randint(1, 2)))
        print(weakpass())
