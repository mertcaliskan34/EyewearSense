# Glasses Detection Web Application

This project is a web application that utilizes a trained convolutional neural network (CNN) model to detect whether a person is wearing glasses in an uploaded image. The application is built using Flask and provides a user-friendly interface for image uploads and results display.

## Project Structure

```
glasses-detection-webapp
├── app
│   ├── static
│   │   └── styles.css          # CSS styles for the web application
│   ├── templates
│   │   └── index.html          # HTML structure for the web application
│   ├── app.py                  # Main application file
│   └── model
│       └── glasses_cnn_model.h5 # Trained model file
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Requirements

To run this application, you need to have the following dependencies installed:

- Flask
- TensorFlow
- Other necessary libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd glasses-detection-webapp
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the `app` directory:
   ```
   cd app
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- Upload an image using the provided form on the homepage.
- The application will process the image and display whether glasses are detected or not.

## License

This project is licensed under the MIT License.