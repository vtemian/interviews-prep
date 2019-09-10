def reverse(x: str) -> str:
    return " ".join(x.split()[::-1])


assert reverse("ana are mere") == "mere are ana"
