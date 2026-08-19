def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """Calculate human age for cats and dogs based on their pet age in months."""
    def calc_age(months: int, increment: int) -> int:
        if months < 15:
            return 0
        if 15 <= months < 24:
            return 1
        if 24 <= months < 28:
            return 2
        
        base_years = 3
        extra_months = months - 28
        return base_years + (extra_months // increment)

    return [calc_age(cat_age, 4), calc_age(dog_age, 5)]
