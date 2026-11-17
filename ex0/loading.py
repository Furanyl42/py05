def check_reagents() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:\n")

    missing_dependencies = False

    try:
        import pandas as pd  # type: ignore[import-untyped]

        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    except ImportError:
        print("[MISSING] pandas - Not found")
        missing_dependencies = True

    try:
        import numpy as np

        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    except ImportError:
        print("[MISSING] numpy - Not found")
        missing_dependencies = True

    print()
    print("pip vs Poetry:")
    print(
        "  requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "  pyproject.toml declares the same constraints, and Poetry pins "
        "the resolved"
    )
    print("  versions in poetry.lock so every install is identical.")
    print()

    if missing_dependencies:
        print("WARNING: Some reagents are missing!")
        print("To install using pip, run:")
        print("  pip install -r ex0/requirements.txt")
        print("To install using Poetry, run:")
        print("  cd ex0 && poetry install")
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    check_reagents()
