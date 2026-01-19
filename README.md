Real-Time Potato Quality Inspection Using Raspberry Pi

Project Description
This project implements a real-time system to inspect the quality of potatoes using a Raspberry Pi and a camera.
It automatically detects whether a potato is in good condition or defective (e.g:has sprouts,rough skin).
The system provides a simple and efficient solution for basic quality control in small-scale agricultural or food processing setups.

Problem Statement
Manual inspection of potatoes is time-consuming, inconsistent, and prone to errors.
There is a need for an automated solution that can quickly and accurately classify potatoes as good or defective in real-time.

System Pipeline:
The system follows a straightforward pipeline:
Image Capture – The Raspberry Pi camera captures live images of potatoes.
Preprocessing – The images are converted to grayscale, and noise is removed for clearer analysis.
Feature Extraction – Key features like smoothness, presence of sprouts, and texture irregularities are identified.
Classification – Potatoes are classified as “Good” or “Defective” based on the extracted features.
Real-Time Output – The results are displayed on the screen in real-time for easy monitoring.

Technologies Used
Python – Programming language for implementing the system
OpenCV – Library for image processing
NumPy – Library for numerical operations

Hardware Used
Raspberry Pi – For running the program and processing images
Raspberry Pi Camera Module – To capture real-time images
Power Supply – To power the Raspberry Pi

Setup Instructions

Clone the repository:
git clone https://github.com/NavyaBommisetty/RaspberryPi-Real-Time-Potato-Inspection.git

Navigate to the project folder:
cd RaspberryPi-Real-Time-Potato-Inspection

Install the required Python libraries:
pip install opencv-python numpy

Connect the Raspberry Pi camera module to your Raspberry Pi.

Run the main program:
python potato_inspection.py

Demo:
A demo video of the system running in real-time is available 

Project Outcomes
-Real-time detection of good and defective potatoes
-Simple and lightweight system that can be deployed easily
-Provides a foundation for automated sorting systems
-Can be extended to other vegetables or fruits in the future

Future Work

-Integrate with a small conveyor belt for automatic sorting
-Improve detection accuracy using machine learning models
-Extend to multi-class classification for different types of defects
