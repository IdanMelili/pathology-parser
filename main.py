import os
from pathology.pipeline import run_pipeline

report_files = [
    "data/sample_report.txt",
    "data/report_narrative.txt",
    "data/report_synoptic.txt",
    "data/report_messy.txt",
]

for filepath in report_files:
    print("=" * 40)
    print(f"  Report: {os.path.basename(filepath)}")
    print("=" * 40)

    with open(filepath, "r") as f:
        raw_report = f.read()

    results = run_pipeline(raw_report)

    fields = {
        "Cancer Type":  results["cancer_type"],
        "Primary Site": results["primary_site"],
        "Tumor Size":   results["tumor_size"],
        "T Stage":      results["T_stage"],
        "N Stage":      results["N_stage"],
        "M Stage":      results["M_stage"],
        "Margins":      results["margins"],
    }

    for field, value in fields.items():
        display = value if value is not None else "Not found"
        print(f"  {field:<14} {display}")

    print()