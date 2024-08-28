# F1 Cars Detection

## Overview
The **F1 Cars Detection** project is an AI-powered system designed to detect and classify Formula 1 cars in real-time video footage. This project utilizes the YOLOv8 model to distinguish between cars from top F1 teams, offering precise and timely identification during race events. The application of this technology can extend to live race monitoring, automated video editing, and providing enhanced real-time analytics for racing enthusiasts.

## Features
- **Real-time Detection:** Continuously processes video footage to identify F1 cars.
- **High Accuracy Classification:** The system is trained to recognize and classify cars from leading F1 teams: Ferrari, McLaren, Mercedes, and Red Bull.
- **Scalable Application:** Can be adapted to different video inputs, making it versatile for various media sources.

## Technology Stack
- **YOLOv8:** Used for object detection, known for its speed and accuracy.
- **OpenCV:** Provides the tools for video capture, processing, and display.
- **Pandas:** Manages detection data for easy processing and analysis.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Osama-Abo-Bakr/f1-cars-detection.git
   cd f1-cars-detection
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Pre-trained YOLO Model:**
   - Download the `detection_f1_cars.pt` model and place it in the project directory.

## Usage
1. **Run the Detection Script:**
   ```bash
   python f1_cars_detection.py
   ```

2. **Select Video Input:**
   - The script is set to process a predefined video file, but you can easily switch to a live webcam feed or another video source by modifying the `video = cv2.VideoCapture()` line in the code.

3. **Monitor Output:**
   - The video will display bounding boxes around detected cars, with labels indicating the team and the confidence level of the detection.

## Customization
- **Model Tuning:** You can adjust the YOLO model parameters to improve detection accuracy based on different racing environments or camera angles.
- **Team Addition:** Extend the system to recognize cars from other F1 teams by retraining the model with additional data.

## Contributing
Contributions are encouraged! Feel free to open issues or submit pull requests for enhancements, bug fixes, or additional features.

## License
This project is licensed under the MIT License. Feel free to use and modify it for your needs.
