import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox, QSlider, QCheckBox
)
from PyQt5.QtCore import Qt

class AVIFConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AVIF Converter")
        self.setGeometry(100, 100, 400, 250)

        # Main Layout
        self.layout = QVBoxLayout()

        # Label
        self.label = QLabel("Select a folder to convert images to AVIF format:")
        self.layout.addWidget(self.label)

        # Select folder button
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_folder_button)

        # Quality Slider
        self.quality_label = QLabel("Quality: 50 (Higher = Better Quality, Larger File Size)")
        self.layout.addWidget(self.quality_label)
        self.quality_slider = QSlider(Qt.Horizontal)
        self.quality_slider.setMinimum(0)  # Worst quality
        self.quality_slider.setMaximum(100)  # Best quality
        self.quality_slider.setValue(50)  # Default medium quality
        self.quality_slider.valueChanged.connect(self.update_quality_label)
        self.layout.addWidget(self.quality_slider)

        # Overwrite checkbox
        self.overwrite_checkbox = QCheckBox("Overwrite existing files")
        self.overwrite_checkbox.setChecked(True)  # Default checked
        self.layout.addWidget(self.overwrite_checkbox)

        # Convert button
        self.convert_button = QPushButton("Convert to AVIF")
        self.convert_button.clicked.connect(self.convert_to_avif)
        self.convert_button.setEnabled(False)
        self.layout.addWidget(self.convert_button)

        # Set layout
        self.setLayout(self.layout)

        # Variables
        self.input_folder = None
        self.output_folder = None

    def update_quality_label(self):
        """Update the quality label based on the slider value."""
        quality = self.quality_slider.value()
        self.quality_label.setText(f"Quality: {quality} (Higher = Better Quality, Larger File Size)")

    def map_quality_to_crf(self, quality):
        """
        Map slider quality (0-100) to FFmpeg CRF values (63-10).
        Lower CRF = Higher Quality.
        """
        # Reverse mapping: Higher slider value -> Lower CRF value
        return int(63 - (quality / 100) * 53)

    def select_folder(self):
        """Open file dialog to select an input folder."""
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.input_folder = folder
            self.output_folder = os.path.join(folder, "converted")
            self.label.setText(f"Selected Folder: {folder}")
            self.convert_button.setEnabled(True)

    def convert_to_avif(self):
        """Convert images to AVIF format."""
        if not self.input_folder:
            QMessageBox.warning(self, "Warning", "Please select a folder first!")
            return

        # Ensure output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

        supported_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif"}
        converted_count = 0

        for filename in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, filename)
            file_extension = os.path.splitext(filename)[1].lower()

            if file_extension in supported_extensions:
                output_file = os.path.join(self.output_folder, os.path.splitext(filename)[0] + ".avif")

                # Check if the file already exists and overwrite option
                if os.path.exists(output_file) and not self.overwrite_checkbox.isChecked():
                    print(f"Skipping {filename} (already exists).")
                    continue

                try:
                    # Map slider value to FFmpeg CRF value
                    crf_value = self.map_quality_to_crf(self.quality_slider.value())
                    print(f"Converting {filename} with CRF {crf_value}...")

                    # FFmpeg command with overwrite flag
                    subprocess.run([
                        "ffmpeg", "-y", "-i", file_path,  # Add `-y` to force overwrite
                        "-c:v", "libaom-av1",  # AVIF encoder
                        "-crf", str(crf_value),  # Mapped CRF value
                        "-b:v", "0",          # Constant quality mode
                        output_file
                    ], check=True)
                    print(f"Converted: {filename} -> {output_file}")
                    converted_count += 1

                except subprocess.CalledProcessError as e:
                    QMessageBox.critical(self, "Error", f"Failed to convert {filename}: {e}")

        QMessageBox.information(self, "Conversion Complete", f"Successfully converted {converted_count} images to AVIF.\nSaved to: {self.output_folder}")

# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = AVIFConverterApp()
    window.show()
    app.exec()
