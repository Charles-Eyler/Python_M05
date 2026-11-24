import importlib


def check_dependencies(name: str):
    try:
        module = importlib.import_module(name)
    except ImportError:
        return None
    return module.__version__


def loading_reagents():
    print("\nREAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    has_pandas = False
    has_numpy = False
    if check_dependencies("pandas") is None:
        print("[MISSING]: pandas is not installed do:")
        print("[pip]: run \'pip install -r requirements.txt\'"
              " or \'pip install pandas\'")
        print("[poetry] run \'poetry install\'\n")
    else:
        print(f"[OK] pandas ({check_dependencies("pandas")})"
              " - Data manipulation ready")
        has_pandas = True
    if check_dependencies("numpy") is None:
        print("[MISSING]: numpy is not installed do:")
        print("[pip]: run \'pip install -r requirements.txt\'"
              " or \'pip install numpy\'")
        print("[poetry] run \'poetry install\'\n")
    else:
        print(f"[OK] numpy ({check_dependencies("numpy")})"
              " - Numerical computation ready")
        has_numpy = True
    if has_pandas is True and has_numpy is True:
        print("\npip vs Poetry:")
        print(" requirements.txt declares what to install;"
              " pip resolves it at install time.")
        print(" pyproject.toml declares the same constraints,"
              " and Poetry pins the resolved")
        print(" versions in poetry.lock so every install is identical.\n")
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    loading_reagents()
