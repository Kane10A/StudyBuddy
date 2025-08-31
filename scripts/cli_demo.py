import argparse
from src.utils.random_problem import get_random_problems


def pretty_print_problem(problem: dict):
    print(f"Title {problem['title']}")
    print(f"Difficulty: {problem['difficulty']}")
    print(f"Source: {problem['source']}")
    print(f"Question: \n {problem['statement']}")
    print(f"URL: {problem['url']}")

def main():
    print("======== Welcome to the Study Helper CLI! ========")
    number_problems = input("How many problems would you like? (default 5) ")
    problems = get_random_problems(number_problems) if number_problems else get_random_problems()
    for i, problem in enumerate(problems):
        print(f"\n------Problem {i + 1} --------")
        pretty_print_problem(problem)
        print("\n")
        cont = input("Print Next Problem?")
if __name__ == "__main__":
    main()