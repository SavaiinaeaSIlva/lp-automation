import subprocess
import sys

def run_command(command):
    """Runs a shell command, prints its output, and checks for errors."""
    print(f"\n▶️  Executing: {command}")
    # The 'shell=True' part allows us to run commands as a string
    # 'capture_output=True' and 'text=True' make the output readable
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Print the standard output from the command
    if result.stdout:
        print(result.stdout)

    # If there was an error, print it and return False
    if result.stderr:
        print("   [ERROR]", result.stderr)
        return False
        
    print("✅ Command successful.")
    return True

def main():
    """Main function to run the git commands."""
    
    # Get a commit message from the user
    commit_message = input("💬 Enter your commit message: ")
    if not commit_message:
        print("   [ERROR] Commit message cannot be empty. Aborting.")
        return

    # List of commands to run in order
    commands = [
        "git add .",
        f'git commit -m "{commit_message}"',
        "git push"
    ]

    # Run each command, and stop if one fails
    for cmd in commands:
        if not run_command(cmd):
            print("\n❌ A command failed. Halting script.")
            sys.exit(1) # Exit the script with an error code

    print("\n🎉 Successfully pushed all changes to the remote repository!")

if __name__ == "__main__":
    main()
