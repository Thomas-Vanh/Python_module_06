
def main():
    print("--- Kaboom 1 ---")
    try:
        # Accessing dark_spellbook triggers top-level circular import failure
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        
        res = dark_spell_record("Curse", "bats, arsenic")
        print(res)
    except (ImportError, AttributeError) as e:
        print("\n💥 KABOOM! Your alchemist laboratory has just exploded! 💥")
        print(f"Error Details: {e}")


if __name__ == "__main__":
    main()