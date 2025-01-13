# FileFinderCLI

FileFinderCLI is a command-line tool for searching files on your computer with unmatched accuracy and speed. This script outperforms the Windows File Explorer in locating files, even discovering files that the File Explorer might miss. With multiple search modes and a user-friendly interface, it’s your go-to solution for quick and efficient file searches.

---

## Features

- **Faster and More Accurate Searches**: Locate files with precision and speed beyond what Windows File Explorer offers.
- **Versatile Search Modes**:
  - **Exact Match** (`=`): Search for files that match your input exactly.
  - **Starts With** (`sw`): Find files that start with the specified string.
  - **Ends With** (`ew`): Search for files that end with the specified string.
  - **Contains**: Default mode to search for files containing your input.
- **File Opening**: Open located files directly from the command line.
- **Interactive Help and Guidance**: Provides help and guidance for all operations.

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/AZaUk/FileFinderCLI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FileFinderCLI
   ```
3. Run the script:
   ```bash
   python Search.py
   ```

4. Follow the on-screen instructions:
   - Type 'exit' to exit the program.
   - Type 'help' to display the help menu.
   - Select your desired search mode:
       - '=' for exact match
       - 'sw' for files starting with your input
       - 'ew' for files ending with your input
       - Or simply input a substring to search for files containing it.


5. Once a file is found:
   - You will be prompted whether you want to open the file.
   - Respond with 'y' (yes) or 'n' (no).

---

## Why Use FileFinderCLI?

### 1. Unmatched Performance

FileFinderCLI is engineered for speed and accuracy, often outperforming the Windows File Explorer. It can find files that Windows File Explorer may fail to detect, making it the ideal choice for power users and developers.

### 2. Custom Search Modes

Choose from multiple search modes to narrow down results and locate files with specific criteria.

### 3. Interactive and Intuitive

The interactive prompts guide you every step of the way, ensuring ease of use even for those new to the command line.

---

## Requirements

- Python 3.x
- OS with Python installed (Windows, Linux, or macOS)

---

## Limitations

- This script performs a recursive search starting from the root directory (/). For systems with a large file structure, it may take a while depending on the input and scope of the search.

---

## Contributing
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Disclaimer

FileFinderCLI is designed to complement existing file search utilities. While it surpasses the Windows File Explorer in many aspects, the script may require elevated permissions to search certain directories. Always ensure that you have proper permissions before running this tool.