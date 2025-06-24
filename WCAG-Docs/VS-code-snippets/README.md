# VS Code — Snippets for text replacements

VS Code snippets are keyboard shortcuts that expand into larger, predefined blocks of text, saving you typing time.

Mac's in-build text replacements may not work in VS Code, especially if you have existing snippets in there already. You can use Python to convert and combine the Mac OS `.plist` files into a single VS code snippet file that will replicate the functionality.

## [How to add the VS code snippet](#how-to-add-the-vs-code-snippet)

First, [download the snippet file](all-wcag-text-replacements.code-snippets).

Then open VS Code and **save it to your snippets directory**. The path should look something like: `~/Library/Application Support/Code/User/snippets/all-wcag-text-replacements.code-snippets`.

Alternatively, go to `Code > Settings > Configure Snippets > New Global Snippets File...` and paste the contents into this new file.

## Future updates

Whenever guidelines are updated and new `.plist` files available, you can **generate a new snippet file** via a Python script.

This script will:
1. Scan the directory where the script is run for all files ending in `.plist.`
2. Process each valid `.plist` file it finds.
3. Combine all text replacements from all `.plist` files into a single, comprehensive VS Code snippets file.

Instructions: 

1. Download the latest [macOS Text replacements](macOS-Text-Replacements) and unzip the directory.
2. Install Python, if you haven't already: `brew install python`.
3. Download the [Python script](convert_all_snippets.py) and save it to the **same directory** where you've saved the `.plist` files.
4. Open a terminal and navigate to where where the `.plist` and `.py` files are saved. E.g. `cd downloads/macOS Text Replacements`
5. Run the script: `python3 convert_all_snippets.py`. This should generate a new `.code-snippets` file in the same directory.
6. [Save the new VS code snippet](#how-to-add-the-vs-code-snippet)
