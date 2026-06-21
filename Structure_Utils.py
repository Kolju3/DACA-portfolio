from pathlib import Path

def CreateFolderWithReadme(FolderName):
    """
    Creates a folder and a README.md inside it (if the README doesn't exist).
    """
    FolderPath = Path(FolderName)
    FolderPath.mkdir(exist_ok=True)

    ReadmePath = FolderPath / "README.md"
    if not ReadmePath.exists():
        with open(ReadmePath, "w") as FileHandle:
            FileHandle.write(f"# {FolderName}\n\n")
            FileHandle.write(f"Placeholder for {FolderName} materials.\n")
            
            if FolderName.startswith("Week"):
                WeekNumber = FolderName.replace("Week", "")
                FileHandle.write(f"Content for Week {WeekNumber} of the Data Analysis course.\n")
            elif FolderName == "Data":
                FileHandle.write("Raw and processed datasets used in the course.\n")
            elif FolderName == "RAG":
                FileHandle.write("Materials related to Retrieval-Augmented Generation (RAG).\n")
        
        print(f"✅ Created {ReadmePath}")
    else:
        print(f"⏩ {ReadmePath} already exists, skipped.")