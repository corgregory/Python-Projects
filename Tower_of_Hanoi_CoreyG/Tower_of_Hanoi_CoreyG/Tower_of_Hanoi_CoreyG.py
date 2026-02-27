def hanoi_solver(total_disks: int) -> str:

    # Rod A starts with all disks (largest → smallest)
    rod_A: list[int] = list(range(total_disks, 0, -1))
    rod_B: list[int] = []
    rod_C: list[int] = []

    # This list will store every state of the rods
    states: list[str] = []
    states.append(f"{rod_A} {rod_B} {rod_C}")  # Starting arrangement

    def move(n: int, src: list[int], dest: list[int], helper: list[int]) -> None:
        """
        Recursively move n disks from src to dest using helper.
        Each move updates the rods and records the new state.
        """
        if n == 1:
            # Move the top disk from src to dest
            disk = src.pop()
            dest.append(disk)
            states.append(f"{rod_A} {rod_B} {rod_C}")
            return
        else:
            # Move n-1 disks to helper
            move(n - 1, src, helper, dest)
            # Move the largest disk to destination
            move(1, src, dest, helper)
            # Move the n-1 disks from helper to destination
            move(n - 1, helper, dest, src)

    # Perform the full Tower of Hanoi solution
    move(total_disks, rod_A, rod_C, rod_B)

    # Return all recorded states as a single string
    return "\n".join(states)


def main() -> None:
    """Test calls for the hanoi_solver function."""
    print("Testing Tower of Hanoi Solver:\n")

    print("=== 1 Disk ===")
    print(hanoi_solver(1))
    print()

    print("=== 2 Disks ===")
    print(hanoi_solver(2))
    print()

    print("=== 3 Disks ===")
    print(hanoi_solver(3))
    print()

    print("=== 4 Disks ===")
    print(hanoi_solver(4))
    print()


if __name__ == "__main__":
    main()

