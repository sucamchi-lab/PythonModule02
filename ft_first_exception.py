def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    try:
        return input_temperature(temp_str)
    except TypeError:
        raise TypeError("Caught input_temperature error: invalid literal for int() with base 10: " + temp_str)

def main() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")

