
# AVIF Image Converter

A lightweight and user-friendly **PyQt5-based GUI application** to batch convert images into the **AVIF** format using **FFmpeg**. 
The app allows users to control image quality with a slider and decide whether to overwrite existing files.
The code was generated mostly using [**ChatGPT 4o**](https://chat.openai.com)

---

## Features

- **Batch Conversion**:
  - Convert multiple image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`) to AVIF.
  - Saves converted files in a `converted` folder within the input directory.

- **Customizable Output Settings**:
  - **Quality Slider**: Adjust output quality using a slider (`0` = worst quality, `100` = best quality).
  - **Overwrite Option**: Decide whether to overwrite existing files.

- **User-Friendly Interface**:
  - Simple GUI for folder selection and conversion settings.

---

## Installation

### Prerequisites

1. **FFmpeg**:
   Ensure `ffmpeg` is installed.
   - On macOS (via Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - On Ubuntu/Debian:
     ```bash
     sudo apt install ffmpeg
     ```
   - On Windows: [Download FFmpeg](https://ffmpeg.org/download.html)

2. **Python 3.7+**:
   Download and install Python from [python.org](https://www.python.org/).

### Install Required Python Libraries

Install the dependencies using `pip`:
```bash
pip install PyQt5
```

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/avif-image-converter.git
   cd avif-image-converter
   ```

2. Run the application:
   ```bash
   python avif_converter.py
   ```

3. Use the GUI to:
   - **Select Input Folder**: Choose a folder containing images to convert.
   - **Adjust Settings**:
     - Move the quality slider to adjust output quality (`0` = worst, `100` = best).
     - Check/uncheck the "Overwrite existing files" box to control overwrite behavior.
   - **Start Conversion**: Converted `.avif` files will be saved in the `converted` folder inside the input folder.

---

## Screenshots

### Main Interface
<img width="448" alt="Image2AVIF Converter" src="https://github.com/user-attachments/assets/e335ecd2-4abd-46a4-afd5-2a86b360fc11">


---

## Code Overview

### Main Components

- **GUI (PyQt5)**:
  - A folder selection dialog for selecting the input directory.
  - Quality slider and overwrite checkbox for user settings.
  - A button to start batch conversion.

- **Backend (FFmpeg)**:
  - Uses FFmpeg for image conversion to AVIF.
  - Adjustable quality using the CRF parameter (`-crf`).

---

## Customization

Feel free to modify the app to suit your needs:
- Add support for additional input formats.
- Extend the UI with more customization options (e.g., resolution settings).

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Acknowledgments

- [PyQt5](https://pypi.org/project/PyQt5/)
- [FFmpeg](https://ffmpeg.org/)

---

### TODO

- ✅ Add a quality slider for better control over output image quality.
- ✅ Include an option to overwrite existing files.
- ➡️ Add support for more image formats as input.
- ➡️ Implement drag-and-drop functionality for file selection.
- ➡️ Include a progress bar for visual feedback during conversion.

---
