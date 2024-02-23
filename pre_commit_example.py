import subprocess

def main():
    print("Running pre-commit checks...")
    subprocess.call(["pre-commit", "run", "--all-files"])
    print("Pre-commit checks completed.")

if __name__ == "__main__":
    main()
