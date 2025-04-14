# PRODIGY_DS_01
# Population Pyramid Visualization

This project loads population data from a CSV file, processes it to group age and gender-wise population, and visualizes the data as a **population pyramid** using a horizontal bar chart.

---

# Project Structure
```
├── data_loader.py # Loads the CSV data                                                                                                        
├── data_processor.py # Filters and groups the data                                                                                                                                                         
├── data_visualizer.py # Plots population pyramid                                                                                                                                                    
├── main.py # Main entry point                                                                                                                          
├── population.csv # Input data file (must be placed in same directory or updated path)                                                                            
├── requirements.txt
└── README.md                                                  
```
# How to Run

**Install dependencies**  
   Create a virtual environment (optional) and install the required libraries:

```
pip install matplotlib pandas seaborn
```
Another way to install libraries (Make sure you have requirements.txt in that dict)
```
pip install -r "requirements.txt"
```


Run the project
Execute the main script:
python main.py
# Features
Cleans and processes raw population data

Groups by age group and gender

Visualizes population split for comparison

# Customization
You can update the CSV path in main.py or data_loader.py.

Age ranges and filtering logic are customizable in data_processor.py.

# Dependencies
pandas: For data manipulation

matplotlib: For plotting the pyramid

# Dataset
Make sure the dataset is in the same directory
```
https://drive.google.com/file/d/1HWriLEmT-iSWcWRcEW1RYFGOFk21KKcp/view?usp=drive_link
```
