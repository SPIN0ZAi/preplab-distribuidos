# scripts/generators/generate_master.py
# -*- coding: utf-8 -*-
"""
Master Question Bank Assembler.
Compiles 260 questions for Lab 1 and 260 questions for Lab 2.
Total = 520 questions.
Writes to src/data/lab1.json and src/data/lab2.json.
"""

import os
import sys
import json
import subprocess

def main():
    generators_dir = os.path.dirname(__file__)
    sys.path.append(generators_dir)

    import lab1_part1
    import lab1_part2
    import lab1_part3
    import lab1_part4
    import lab2_part1
    import lab2_part2
    import lab2_part3
    import lab2_part4

    l1 = (
        lab1_part1.get_questions() +
        lab1_part2.get_questions() +
        lab1_part3.get_questions() +
        lab1_part4.get_questions()
    )

    l2 = (
        lab2_part1.get_questions() +
        lab2_part2.get_questions() +
        lab2_part3.get_questions() +
        lab2_part4.get_questions()
    )

    print(f"Loaded Lab 1: {len(l1)} questions.")
    print(f"Loaded Lab 2: {len(l2)} questions.")
    print(f"Total Questions: {len(l1) + len(l2)}")

    base_dir = os.path.abspath(os.path.join(generators_dir, "..", ".."))
    data_dir = os.path.join(base_dir, "src", "data")
    os.makedirs(data_dir, exist_ok=True)

    lab1_path = os.path.join(data_dir, "lab1.json")
    lab2_path = os.path.join(data_dir, "lab2.json")

    with open(lab1_path, "w", encoding="utf-8") as f:
        json.dump(l1, f, indent=2, ensure_ascii=False)
    print(f"Wrote {lab1_path}")

    with open(lab2_path, "w", encoding="utf-8") as f:
        json.dump(l2, f, indent=2, ensure_ascii=False)
    print(f"Wrote {lab2_path}")

    # Run validation
    val_script = os.path.join(base_dir, "scripts", "validate-questions.mjs")
    print(f"\nRunning validation script: node {val_script}")
    res = subprocess.run(["node", val_script], cwd=base_dir, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print(res.stderr, file=sys.stderr)

    if res.returncode != 0:
        print("Validation FAILED!")
        sys.exit(1)
    else:
        print("Validation PASSED PERFECTLY!")

if __name__ == "__main__":
    main()
