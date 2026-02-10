def extract_skills(text, skill_list):
    return [skill for skill in skill_list if skill in text]


def calculate_skill_score(matched_skills, total_skills):
    if total_skills == 0:
        return 0
    return len(matched_skills) / total_skills
