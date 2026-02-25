from pathology.preprocessor import preprocess
from pathology.extractor import (
    extract_tnm,
    extract_tumor_size,
    extract_cancer_type,
    extract_margins,
    extract_primary_site,
)


def run_pipeline(raw_text: str) -> dict:
    """
    Full pipeline: takes raw pathology report text,
    cleans it, extracts all fields, returns structured dict.
    """
    # Step 1: Clean the text
    clean_text = preprocess(raw_text)

    # Step 2: Extract everything
    tnm = extract_tnm(clean_text)

    result = {
        "cancer_type": extract_cancer_type(clean_text),
        "primary_site": extract_primary_site(clean_text),
        "tumor_size": extract_tumor_size(clean_text),
        "T_stage": tnm["T"],
        "N_stage": tnm["N"],
        "M_stage": tnm["M"],
        "margins": extract_margins(clean_text),
    }

    return result