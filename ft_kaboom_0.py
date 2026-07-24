from alchemy.grimoire import light_spell_record


def main() -> None:
    print("--- Kaboom 0 ---")
    result: str = light_spell_record("Lumos", "fire, air")
    print(result)


if __name__ == "__main__":
    main()
