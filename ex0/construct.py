import sys
import os
import site

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and
                                   sys.base_prefix != sys.prefix):
    print("LABORATORY STATUS: The laboratory is sealed\n")
    print("Current Python:", sys.executable)
    print("Virtual Evironment:", os.path.basename(sys.prefix))
    print(f"Evironment path: {sys.prefix}\n")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.\n")
    print("Reagent installation path:")
    package_loc: list[str] = site.getsitepackages()
    print(package_loc[0])

else:
    print("LABORATORY STATUS: You are working in the open\n")
    print("Current Python:", sys.executable)
    print("Virtual Evironment:", sys.prefix)
    print("Virtual environment: None detected\n")
    print("WARNING: you are in the global environment!")
    print("Every reagent you install here leaks into the whole sytem\n")
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")
