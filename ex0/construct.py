import os
import site
import sys


def construct() -> None:
    inside_venv = sys.prefix != sys.base_prefix

    if inside_venv:
        status = "The laboratory is sealed"
    else:
        status = "You are working in the open"

    print(f"LABORATORY STATUS: {status}\n")
    print(f"Current Python: {sys.executable}")

    if inside_venv:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.\n")
        print("Reagent installation path:")
        print(site.getsitepackages()[0])
    else:
        print("Virtual Environment: None detected")
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    construct()
