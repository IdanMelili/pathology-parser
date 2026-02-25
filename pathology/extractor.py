import re


def extract_tnm(text: str) -> dict:
    """
    Extract TNM staging from pathology report text.
    Handles formats like: pT2aN1M0, T2a N1 M0, pathologic stage T2
    """
    # Optional prefix (p=pathologic, c=clinical, y=post-treatment, r=recurrent), then T + stage number + optional sub-letter
    t_match = re.search(r'(?:p|c|y|r)T([0-4X][a-z]?)\b', text, re.IGNORECASE)
    # Same prefix options, then N + lymph node stage (0-3 or X)
    n_match = re.search(r'(?:p|c|y|r)N([0-3X][a-z]?)\b', text, re.IGNORECASE)
    # Optional prefix, then M + metastasis flag (0, 1, or X)
    m_match = re.search(r'(?:p|c|y|r)?M([0-1X])\b', text, re.IGNORECASE)

    return {
        "T": t_match.group(0) if t_match else None,
        "N": n_match.group(0) if n_match else None,
        "M": m_match.group(0) if m_match else None,
    }


def extract_tumor_size(text: str) -> str | None:
    """
    Extract tumor size. Handles: '2.3 cm', '23 mm', '2.3 x 1.5 cm'
    """
    # Decimal number, optional second dimension (x ...), then unit cm or mm
    match = re.search(r'(\d+\.?\d*)\s*(?:x\s*\d+\.?\d*\s*)?(?:cm|mm)\b', text, re.IGNORECASE)
    return match.group(0) if match else None


def extract_cancer_type(text: str) -> str | None:
    """
    Match known cancer histology types using a keyword list.
    """
    cancer_types = [
        "adenocarcinoma",
        "squamous cell carcinoma",
        "small cell carcinoma",
        "large cell carcinoma",
        "ductal carcinoma",
        "lobular carcinoma",
        "melanoma",
        "glioblastoma",
        "mesothelioma",
    ]
    text_lower = text.lower()
    for cancer in cancer_types:
        if cancer in text_lower:
            return cancer
    return None


def extract_margins(text: str) -> str | None:
    """
    Extract surgical margin status.
    Looks for: 'margins negative', 'positive margins', 'clear margins', etc.
    """
    # Matches "margins negative" OR "negative margins" (and plural variants)
    match = re.search(
        r'(margins?\s*(negative|positive|clear|involved|close)|'
        r'(negative|positive|clear|involved)\s*margins?)',
        text, re.IGNORECASE
    )
    return match.group(0) if match else None


def extract_primary_site(text: str) -> str | None:
    """
    Match known anatomical primary sites.
    """
    sites = [
        "lung", "breast", "colon", "rectum", "prostate",
        "pancreas", "liver", "kidney", "bladder", "ovary",
        "uterus", "cervix", "stomach", "esophagus", "thyroid",
    ]
    text_lower = text.lower()
    for site in sites:
        if site in text_lower:
            return site
    return None