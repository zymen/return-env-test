import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python print_env.py VAR1,VAR2,...")
        sys.exit(1)

    env_vars = sys.argv[1].split(",")
    for var in env_vars:
        var = var.strip()
        value = os.environ.get(var, "")
        print(f"{var}={value}")