class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown watering error"):
        self.message = message
        super().__init__(self.message)


def water_plant(amount: int) -> None:
    if amount < 10:
        raise WaterError("Not enough water in the tank!")
    print("Plant watered successfully.")


def plant_tomato(soil_quality: str) -> None:
    if soil_quality != "good":
        raise PlantError("The tomato plant is wilting!")
    print("Tomato planted successfully.")


def test_specific_error() -> None:
    print("\nTesting PlantError...")
    try:
        plant_tomato("bad")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        water_plant(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_all_garden_errors() -> None:
    print("\nTesting catching all garden errors...")
    try:
        plant_tomato("bad")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        water_plant(5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_specific_error()
    test_all_garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
