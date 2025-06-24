import plistlib
import json
import os

def convert_plists_to_vscode_snippets(directory_path=".", output_file_name="all_mac_text_replacements.code-snippets"):
    """
    Scans a directory for .plist files, converts their text replacements
    into VS Code snippets, and consolidates them into a single .code-snippets file.

    Args:
        directory_path (str): The path to the directory to scan for .plist files.
                              Defaults to the current directory (".").
        output_file_name (str): The name of the output VS Code snippets file.
    """
    all_vscode_snippets = {}
    processed_files_count = 0
    snippet_count = 0

    print(f"Scanning directory: '{os.path.abspath(directory_path)}' for .plist files...")

    # Get a list of all files in the specified directory
    try:
        files_in_directory = os.listdir(directory_path)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return

    plist_files = [f for f in files_in_directory if f.lower().endswith('.plist')]

    if not plist_files:
        print("No .plist files found in the specified directory. Exiting.")
        return

    for plist_file_name in plist_files:
        plist_file_path = os.path.join(directory_path, plist_file_name)
        print(f"\nProcessing '{plist_file_name}'...")

        try:
            with open(plist_file_path, 'rb') as fp:
                plist_data = plistlib.load(fp)

            # Verify that the plist root is an array as per your example
            if isinstance(plist_data, list):
                processed_files_count += 1
                for item in plist_data:
                    if isinstance(item, dict):
                        shortcut = item.get('shortcut')
                        phrase = item.get('phrase')

                        if shortcut and phrase:
                            # Create a unique and descriptive snippet name
                            # We append the filename without extension to help distinguish if needed
                            # And use a simplified name for the actual snippet if the file is large
                            snippet_id = f"{os.path.splitext(plist_file_name)[0]}_{shortcut}"
                            snippet_name = f"Mac Repl [{os.path.splitext(plist_file_name)[0]}] {shortcut}"

                            # Escape dollar signs as they have special meaning in VS Code snippets
                            body_lines = [line.replace('$', '\\$') for line in phrase.splitlines()]

                            # Add to our master dictionary of all snippets
                            all_vscode_snippets[snippet_name] = {
                                "prefix": shortcut,
                                "body": body_lines,
                                "description": f"macOS Text Replacement from '{plist_file_name}' for '{shortcut}'"
                            }
                            snippet_count += 1
                        else:
                            print(f"  Warning: Skipping an item in '{plist_file_name}' due to missing 'shortcut' or 'phrase': {item}")
                    else:
                        print(f"  Warning: Skipping an non-dictionary item in '{plist_file_name}': {item}")
            else:
                print(f"  Error: Expected plist root in '{plist_file_name}' to be an array, but found {type(plist_data).__name__}. Skipping this file.")

        except plistlib.InvalidFileException as e:
            print(f"  Error: Invalid plist file format for '{plist_file_name}': {e}. Skipping this file.")
        except Exception as e:
            print(f"  An unexpected error occurred while processing '{plist_file_name}': {e}. Skipping this file.")

    if not all_vscode_snippets:
        print("\nNo valid text replacements were found in any .plist files. No output file generated.")
        return

    # Write all consolidated snippets to a single output file
    output_file_path = os.path.join(directory_path, output_file_name)
    try:
        with open(output_file_path, 'w') as f:
            json.dump(all_vscode_snippets, f, indent=2)
        print(f"\nSuccessfully processed {processed_files_count} .plist file(s) and generated {snippet_count} VS Code snippets.")
        print(f"All snippets consolidated into: '{output_file_path}'")
        print(f"You can now open '{output_file_path}' and copy its content into your VS Code snippets file.")
    except Exception as e:
        print(f"Error writing the consolidated VS Code snippets file: {e}")

# --- How to run the script ---
if __name__ == "__main__":
    # Ensure all your .plist files are in the same directory as this script.
    # The script will look in the current directory ('.').
    # The output file will also be created in the current directory.
    convert_plists_to_vscode_snippets()