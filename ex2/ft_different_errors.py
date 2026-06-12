def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        _ = 10 / 0
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        "hello" + 5  # type: ignore[operator]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation_num in range(5):
        print(f"Testing operation {operation_num}...")
        try:
            garden_operations(operation_num)
            print("Operation completed successfully")
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError,
        ) as e:
            print(f"Caught {type(e).__name__}: {e}")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
