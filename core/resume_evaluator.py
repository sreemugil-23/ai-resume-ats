import re


def evaluate_resume_only(raw_text, cleaned_text):
    score = 0
    feedback = {}

    words = cleaned_text.split()
    word_count = len(words)

    # -------------------------
    # 1. SECTION STRUCTURE (25)
    # -------------------------
    sections = [
        "experience", "skills", "education",
        "projects", "certifications", "summary"
    ]

    found_sections = [s for s in sections if s in cleaned_text]
    score += (len(found_sections) / len(sections)) * 25
    feedback["sections_found"] = found_sections

    # -------------------------
    # 2. KEYWORD PRESENCE (25)
    # -------------------------
    keywords = [
        "python", "java", "sql", "api", "cloud",
        "data", "machine learning", "docker",
        "git", "javascript"
    ]

    matched_keywords = [k for k in keywords if k in cleaned_text]
    score += min(len(matched_keywords) / 6, 1.0) * 25
    feedback["keywords_matched"] = matched_keywords

    # -------------------------
    # 3. RESUME LENGTH (15)
    # -------------------------
    if 400 <= word_count <= 900:
        score += 15
    elif 250 <= word_count < 400 or 900 < word_count <= 1200:
        score += 9
    else:
        score += 4

    feedback["word_count"] = word_count

    # -------------------------
    # 4. SKILL DENSITY (15)
    # -------------------------
    if word_count > 0:
        density = len(matched_keywords) / word_count
        score += min(density * 400, 1.0) * 15

    # -------------------------
    # 5. CONTACT INFO (10)  ✅ FIXED
    # -------------------------
    email_present = bool(
        re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", raw_text)
    )

    phone_present = bool(
        re.search(r"(\+?\d{1,3}[\s-]?)?\d{10}", raw_text)
    )

    contact_score = 10 if (email_present or phone_present) else 4
    score += contact_score

    feedback["contact_detected"] = email_present or phone_present

    return round(score, 2), feedback
