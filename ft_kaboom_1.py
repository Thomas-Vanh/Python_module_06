
def main() -> None:
    print("--- Kaboom 1 ---")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record

        res: str = dark_spell_record("Curse", "bats, arsenic")
        print(res)
    except (ImportError, AttributeError) as e:
        print("\nKABOOM! Your alchemist laboratory has just exploded!")
        print(f"Error Details: {e}")


if __name__ == "__main__":
    main()
