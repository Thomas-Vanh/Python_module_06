from alchemy.grimoire.light_spellbook import light_spell_record


def main():
    print("--- Kaboom 0 ---")
    result = light_spell_record("Lumos", "fire, air")
    print(result)


if __name__ == "__main__":
    main()
