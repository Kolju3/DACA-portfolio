from pathlib import Path
from Structure_Utils import CreateFolderWithReadme  # <-- Updated import

# --- Configuration ---
Folders = ["Data", "RAG"] + [f"Week{WeekCounter}" for WeekCounter in range(11)]  # Week0 to Week10
RootReadme = "README.md"

# --- Main execution ---
def Main():
    # Safety check: are we inside a Git repo?
    if not (Path.cwd() / ".git").exists():
        print("❌ Error: No .git folder found. Please run this script from the root of your Git repository.")
        return

    # 1. Create all folders and their READMEs
    for FolderName in Folders:
        CreateFolderWithReadme(FolderName)

    # 2. Update or create the root README (with duplicate check)
    RootReadmePath = Path(RootReadme)
    
    if RootReadmePath.exists():
        # Read the current content
        with open(RootReadmePath, "r") as FileHandle:
            CurrentContent = FileHandle.read()
        
        # Check if the structure section already exists
        if "## Project Structure" not in CurrentContent:
            # Append the structure section
            with open(RootReadmePath, "a") as FileHandle:
                FileHandle.write("\n## Project Structure\n\n")
                for FolderName in Folders:
                    FileHandle.write(f"- `{FolderName}/` - see `{FolderName}/README.md`\n")
            print(f"✅ Updated root {RootReadme} with structure listing.")
        else:
            print(f"⏩ Root {RootReadme} already contains '## Project Structure' – skipping append.")
    else:
        # Create a new root README from scratch
        with open(RootReadmePath, "w") as FileHandle:
            FileHandle.write("# DACA Portfolio\n\nData Analysis Course portfolio.\n\n## Project Structure\n\n")
            for FolderName in Folders:
                FileHandle.write(f"- `{FolderName}/` - see `{FolderName}/README.md`\n")
        print(f"✅ Created root {RootReadme}.")

    print("\n🎉 Folder structure created successfully!")
    print("Now stage, commit, and push with:")
    print("  git add .")
    print('  git commit -m "Add folder structure for course weeks"')
    print("  git push origin main")

if __name__ == "__main__":
    Main()