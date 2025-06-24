# VS Code — Snippets for text replacements

VS Code snippets are keyboard shortcuts that expand into larger, predefined blocks of text, saving you typing time.

Mac's in-build text replacements may not work in VS Code, especially if you have existing snippets in there already. You can use Python to convert and combine the Mac OS `.plist` files into a single VS code snippet file that will replicate the functionality.

## [How to add as a VS code snippet](#how-to-add-as-a-vs-code-snippet)

[Download the snippet file](all-wcag-text-replacements.code-snippets). Then open VS Code and save it to your snippets directory. The path should look something like: `~/Library/Application Support/Code/User/snippets/all-wcag-text-replacements.code-snippets`.

Alternatively, go to `Code > Settings > Configure Snippets > New Global Snippets File...` and paste the contents into this new file.

## How to generate a new snippet file

When guidelines are updated and new `.plist` files available, follow the below instructions to generate a new snippet file.

### Step 1: Download all plist files

If you haven't done so already, download the [macOS Text replacements](macOS-Text-Replacements) and unzip the directory.

### Step 2: Download the Python script

Note, Python is required. If you are on a Mac you can install this with `brew install python`. 

Save the [Python script file](convert_all_snippets.py) to the **same directory** where you've saved the `.plist` files. 

This script will:
1. Scan the directory where the script is run for all files ending in `.plist.`
2. Process each valid `.plist` file it finds.
3. Combine all text replacements from all `.plist` files into a single, comprehensive VS Code snippets file.

### Step 3: Run the script

Open a terminal and go to the directory where the `.plist` and `.py` files are saved. E.g. `cd downloads/macOS Text Replacements`.

Run `python3 convert_all_snippets.py`. 

This should generate a new `.code-snippets` file in the same directory.

### Step 4: Save to VS Code

See [How to add as a VS code snippet](#how-to-add-as-a-vs-code-snippet) above.
