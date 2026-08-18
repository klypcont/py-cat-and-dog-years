def get_human_age(cat_years: int, dog_years: int) -> list:
    def calc_age(months: int, is_cat: bool) -> int:
        if months < 15:
            return 0
        elif 15 <= months <= 23:
            return 1
        elif 24 <= months <= 27:
            return 2
        
        # 28 months and above
        # At 28 months: cat = 3 human years, dog = 3 human years
        base_years = 3
        extra_months = months - 28
        
        if is_cat:
            increment = extra_months // 4
        else:
            increment = extra_months // 5
            
        return base_years + increment

    return [calc_age(cat_years, True), calc_age(dog_years, False)]


if __name__ == "__main__":
    pass

