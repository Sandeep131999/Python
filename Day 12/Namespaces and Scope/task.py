enemies = 1


def increase_enemies():
    """
        Local Scope
    """
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {locals(enemies)}")
