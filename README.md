
# Blood Bank Recommendation System

This project is a Streamlit-based application that helps users find the most similar blood banks based on their location input.

## Features

- Allows users to select state, district, city, and enter pincode to find nearby blood banks
- Recommends the top 3 most similar blood banks based on Levenshtein distance
- Displays detailed information about the recommended blood banks, including name, state, city, pincode, contact info, and nodal officer details
- Provides a stream-like display of the recommended blood banks

## Demo

[Insert a link to a demo video showcasing the application]

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/blood-bank-recommendation.git
   ```
2. Navigate to the project directory:
   ```
   cd blood-bank-recommendation
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

## Usage

1. Select the state, district, and city from the sidebar options.
2. Enter the pincode in the input field.
3. Click the "Find Blood Bank" button to see the recommended blood banks.
4. The recommended blood banks will be displayed in a stream-like format, showing their details.

## Project Structure

```
blood-bank-recommendation/
├── app.py
├── model.ipynb
├── bank.pkl
├── similarity.pkl
├── Bloodbank.csv
└── README.md
```

- `app.py`: The main Streamlit application file that handles the user interface and calls the recommendation function.
- `blood_bank_recommender.py`: The module that contains the `nearest_bank_recommendation()` function, which performs the blood bank recommendation logic.
- `bank.pkl`: The pickled blood bank data used by the application.
- `similarity.pkl`: The pickled similarity data used by the recommendation function.
- `bloodbank.csv`: The file contain the dataset of blood bank across in India.
- `README.md`: The project's documentation, including the demo video link and installation/usage instructions.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
