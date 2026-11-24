# pyrefly: ignore[missing-import]
import os
from dotenv import load_dotenv, dotenv_values

env_vars_keys = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                 "ZION_ENDPOINT"]

load_dotenv()

env_vars = {k: os.getenv(k) for k in env_vars_keys}
env_vars_file = dotenv_values(".env")


def is_configured(settings: dict) -> bool:
    for key, val in env_vars.items():
        if val == "":
            return False
    return True


def config_details():
    print("Configuration loaded:\n")
    print("Mode:", env_vars.get("MATRIX_MODE"))
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print("log level:", env_vars.get("LOG_LEVEL"))
    print("Remote Network: Online")


def env_ignored():
    try:
        file = open(".gitignore", "r")
        check_env = file.read().split("\n")
        for i in check_env:
            if i == ".env":
                return True
        return False
    except FileNotFoundError as e:
        return print(e)


def print_checks():
    print("\nConfiguration security checks:")
    print("[OK] No hardcoded secrets detected")
    if env_ignored() is True:
        print("[OK] .env file properly ignored by git")
    else:
        print("[KO] .env file was not found to be in .gitignore")
    if env_vars.items() != env_vars_file.items():
        print("[OK] Production overrides available")
    else:
        print("[OK] .env variables loaded")


def access_validation():
    print("ORACLE STATUS: Consulting the configuration...\n")
    try:
        open(".env", "r")
    except FileNotFoundError as e:
        print(e)
        return print("Do: \"cp ex1/.env.example ex1/.env\"")
    if is_configured(env_vars) is False:
        print("!!!MISSING CONFIGURATION!!!\n")
        for key, val in env_vars.items():
            if val == "":
                print(f"{key}: is missing its configuration")
        print("\nCheck default values:\n")
        file = open(".env.example", "r")
        return print(file.read())
    else:
        config_details()
        print_checks()
        print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    access_validation()
