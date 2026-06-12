def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    try:
        print("Input data is '25'")
        result = input_temperature('25')
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    try:
        print("Input data is 'abc'")
        result = input_temperature('abc')
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    try:
        print("Input data is '100'")
        result = input_temperature('100')
        print(f"Temperature is now {result}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    try:
        print("Input data is '-50'")
        result = input_temperature('-50')
        print(f"Temperature is now {result}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
