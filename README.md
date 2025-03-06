# Python-Scripts

## massReplace.py

**Description:**

The `massReplace.py` script is a Python tool that performs mass replacement of numbers with corresponding letters or words based on a provided key file. It reads a key file (`Input/Key.txt`) that defines the mapping between numbers and their replacements, and a data file (`Input/NumReel.txt`) containing the numbers to be replaced.  The script then generates an output file (`Output/Reels.txt`) with the numbers replaced according to the key.

**File Formats:**

*   **`Input/Key.txt`:**  This file contains the key for the replacement.  Each line should contain a number and its corresponding replacement, separated by a tab (`\t`).  It can also handle spaces as separators.
    ```
    1   a
    2   b
    3   word
    10  longword
    ```

*   **`Input/NumReel.txt`:** This file contains the data where numbers will be replaced.  The file should have values separated by tabs (`\t`).
    ```
    1   2   3
    4   5   6   7   10
    ```

*   **`Output/Reels.txt`:** This file will be created by the script and will contain the result of the replacement. The output format will mirror the input format of `NumReel.txt`, with numbers replaced by their corresponding values from `Key.txt`.  For the example input above, the output would be:
    ```
    a   b   word
    d   e   f   g   longword
    ```