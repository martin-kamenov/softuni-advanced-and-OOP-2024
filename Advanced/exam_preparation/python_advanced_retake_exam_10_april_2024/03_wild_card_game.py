def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []

    for row in args:
        card_name, card_type = row[0], row[1]

        if card_type == 'spell':
            spell_cards.append(card_name)
        else:
            monster_cards.append(card_name)

    for name, curr_card_type in kwargs.items():
        if curr_card_type == 'spell':
            spell_cards.append(name)
        else:
            monster_cards.append(name)

    result = []

    if monster_cards:
        result.append('Monster cards:')

        for monster in sorted(monster_cards, reverse=True):
            result.append(f'  ***{monster}')

    if spell_cards:
        result.append('Spell cards:')

        for spell in sorted(spell_cards):
            result.append(f'  $$${spell}')

    return '\n'.join(result)


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"),
                 ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
