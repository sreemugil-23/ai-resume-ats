def calculate_ats_score(similarity, skill_score):
    similarity_weight = 0.5
    skill_weight = 0.3
    hygiene_weight = 0.2

    hygiene_score = 0.8  # placeholder (formatting etc.)

    final = (
        similarity * similarity_weight +
        skill_score * skill_weight +
        hygiene_score * hygiene_weight
    )

    return round(final * 100, 2)
