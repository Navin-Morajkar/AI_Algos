import numpy as np


def simple_matching_coefficient(a, b):
    return np.sum(a == b) / len(a)


def jaccard_coefficient(a, b):
    return np.sum(a & b) / np.sum(a | b)


def extended_jaccard_coefficient(a, b):
    numerator = np.sum(np.minimum(a, b))
    denominator = np.sum(np.maximum(a, b))
    return numerator / denominator


def minkowski_distance(a, b, p):
    return np.sum(np.abs(a - b) ** p) ** (1/p)


def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))


def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


while True:
    print("\n---------Menu-----------")
    print("1. Simple Matching Coefficient")
    print("2. Jaccard Coefficient")
    print("3. Cosine Similarity")
    print("4. Extended Jaccard Coefficient")
    print("5. Minkowski Distance")
    print("6. Manhattan Distance")
    print("7. Euclidean Distance")
    print("8. Exit")

    choice = int(input("\nEnter Choice: "))

    if choice == 8:
        print("Exited successfully", exit())

    if choice in [1, 2]:
        print("Enter two binary vectors (separated by spaces):")
        a = np.array(input().split(), dtype=int)
        b = np.array(input().split(), dtype=int)
    else:
        print("Enter two vectors (separated by spaces):")
        a = np.array(input().split(), dtype=float)
        b = np.array(input().split(), dtype=float)

    if choice == 1:
        print("Simple Matching Coefficient:", simple_matching_coefficient(a, b))
    elif choice == 2:
        print("Jaccard Coefficient:", jaccard_coefficient(a, b))
    elif choice == 3:
        print("Cosine Similarity:", cosine_similarity(a, b))
    elif choice == 4:
        print("Extended Jaccard Coefficient:", extended_jaccard_coefficient(a, b))
    elif choice == 5:
        print("Enter the order (p) of Minkowski distance:")
        p = float(input())
        print("Minkowski Distance:", minkowski_distance(a, b, p))
    elif choice == 6:
        print("Manhattan Distance:", manhattan_distance(a, b))
    elif choice == 7:
        print("Euclidean Distance:", euclidean_distance(a, b))
    else:
        print("Invalid choice.")