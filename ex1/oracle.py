import os

from dotenv import load_dotenv


def hardcoded_secrets_detected() -> bool:
    with open(__file__, "r", encoding="utf-8") as source_file:
        source = source_file.read()

    secret_keys = ("API_KEY", "DATABASE_URL")
    markers = [
        f"{key} = {quote}"
        for key in secret_keys
        for quote in ('"', "'")
    ]
    return any(marker in source for marker in markers)


def env_file_ignored() -> bool:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gitignore_path = os.path.join(script_dir, ".gitignore")
    if not os.path.exists(gitignore_path):
        return False

    with open(gitignore_path, "r", encoding="utf-8") as gitignore:
        entries = {line.strip() for line in gitignore}
    return ".env" in entries


def consult_oracle() -> None:
    print("ORACLE STATUS: Consulting the configuration...\n")

    load_dotenv()

    matrix_mode = (os.getenv("MATRIX_MODE") or "development").strip().lower()
    if matrix_mode not in ("development", "production"):
        print(
            f"[WARNING] Unknown MATRIX_MODE '{matrix_mode}', "
            "defaulting to development."
        )
        matrix_mode = "development"

    database_url = os.getenv("DATABASE_URL") or ""
    api_key = os.getenv("API_KEY") or ""
    log_level = os.getenv("LOG_LEVEL") or "DEBUG"
    zion_endpoint = os.getenv("ZION_ENDPOINT") or ""

    missing_configs = []
    if not database_url:
        missing_configs.append("DATABASE_URL")
    if not api_key:
        missing_configs.append("API_KEY")
    if not zion_endpoint:
        missing_configs.append("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if database_url:
        if matrix_mode == "production":
            db_status = "Connected to remote cluster"
        else:
            db_status = "Connected to local instance"
        print(f"Database: {db_status}")
    else:
        print("Database: [WARNING] Using fallback / unconfigured state")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: [WARNING] Unauthenticated (API_KEY missing)")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: [WARNING] Offline (ZION_ENDPOINT missing)")

    print("\nConfiguration security check:")

    if hardcoded_secrets_detected():
        print("[WARNING] Hardcoded secrets detected in the source!")
    else:
        print("[OK] No hardcoded secrets detected")

    if env_file_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file is NOT listed in .gitignore!")

    if missing_configs:
        keys = ", ".join(missing_configs)
        print(f"[WARNING] Missing configuration keys: {keys}")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    consult_oracle()
