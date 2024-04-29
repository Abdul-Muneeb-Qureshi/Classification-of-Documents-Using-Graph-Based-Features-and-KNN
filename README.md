# Classification-of-Documents-Using-Graph-Based-Features-and-KNN

## Overview

This project aims to classify documents using graph-based features and the K Nearest Neighbors (KNN) algorithm. It utilizes data scraped from various sources and organizes them into a graph database for analysis and classification.

## Folder Structure

### Scrapping

This folder contains scripts for web scraping and the corresponding scraped data files.

- **scrapping_Beauty_Fashion.py**: Scrapes data related to beauty and fashion.
- **scrapping_Beauty_Fashion.csv**: Stores the scraped data related to beauty and fashion.
- **scrapping_Diseases_Symptoms.py**: Scrapes data related to diseases and symptoms.
- **scrapping_Diseases_Symptoms.csv**: Stores the scraped data related to diseases and symptoms.
- **scrapping_Food.py**: Scrapes data related to food.
- **scrapping_Food.csv**: Stores the scraped data related to food.

### Graphs

This folder contains scripts related to graph processing and analysis.

- **featuresExtraction_classification.py**: Implements the K Nearest Neighbors (KNN) algorithm for classification based on the presence of common subgraphs. This script builds a feature matrix and classifies documents accordingly.

- **frequentSubgraphConstruction.py**: Utilizes the gSpan algorithm for frequent subgraph mining. This script takes a file containing graphs in a specific format as input and extracts frequent subgraphs. The script uses the `gSpan` module for mining frequent subgraphs. Ensure that the input file follows the required format for successful execution. Below is an example of the required graph format:
          - ```txt
  t # 0
  v 0 fever
  v 1 symptom
  v 2 follow
  v 3 treatment
  v 4 plan
  e 0 1 2
  e 0 3 2
  e 1 2 2
  e 3 4 2
  t # 1
  v 0 fever
  v 1 symptom
  v 2 follow
  v 3 test
  v 4 us
  e 0 1 2
  e 0 3 2
  e 1 2 2
  e 3 4 2

  from gspan_mining.config import parser
  from gspan_mining.main import main

 def mine_frequent_subgraphs(filename):
     # Define command line arguments for gSpan
     args_str = '-s 5 -d True -l 3 -u 10 -p True -w True ' + filename
     FLAGS, _ = parser.parse_known_args(args=args_str.split())
 
     # Run gSpan to mine frequent subgraphs
     gs = main(FLAGS)

  


- **graphConstruction.py**: Provides functionality to create graphs using the NetworkX library.

- **functions.py**: Contains utility functions for reading CSV files, creating NetworkX graphs, and converting NetworkX graphs to the format required by gSpan for subgraph mining.
- **mcs.py**: Works on finding the direct maximal common graph by finding connected components.


## Graph Database

This folder stores files of graphs in the format required by gSpan.

- **beauty_fashion_graph.txt**: Contains all fashion graphs.
- **diseases_symptoms_graph.txt**: Contains all diseases graphs.
- **food_graph.txt**: Contains all food graphs.
- **frequentSubgrphs.txt**: Contains all frequent subgraphs mined from the input graphs.

## Classification Results

The results of the classification are as follows:

### Diseases
- **Accuracy**: 1.0
- **Precision**: 1.0
- **Recall**: 1.0
- **F1-score**: 1.0

### Fashion
- **Accuracy**: 1.0
- **Precision**: 1.0
- **Recall**: 1.0
- **F1-score**: 1.0

### Food
- **Accuracy**: 1.0
- **Precision**: 1.0
- **Recall**: 1.0
- **F1-score**: 1.0

### Confusion Matrix

![image](https://github.com/Abdul-Muneeb-Qureshi/Classification-of-Documents-Using-Graph-Based-Features-and-KNN/assets/115551959/127144c8-8bf3-43bf-8d0b-25c2a688f63a)

## Usage

To use this project, follow these steps:

1. Run the scripts in the `Scrapping` folder to scrape data from various sources and store it in CSV files.
2. Run the `frequentSubgraphConstruction.py` script in the `Graphs` folder to mine frequent subgraphs from the input graphs stored in the `GraphDataBase` folder.
3. Execute the `featuresExtraction_classification.py` script in the `Graphs` folder to implement the K Nearest Neighbors (KNN) algorithm for classification based on the presence of common subgraphs.
4. Optionally, you can run the `mcs.py` script in the `Graphs` folder, which works on finding the direct maximal common graph by finding connected components.

Ensure that you have the necessary dependencies installed and that your input data is formatted correctly as per the instructions provided in the respective script files.

## Future Work

- **Enhance Efficiency and Scalability:**
  Explore parallelization and optimization techniques to improve the efficiency and scalability of graph mining algorithms.

- **Advanced Graph Embedding:**
  Investigate advanced graph embedding methods to capture richer semantic information and improve feature representation.

- **Ensemble Learning Techniques:**
  Incorporate ensemble learning methods to combine the strengths of graph-based and traditional vector-based methods for enhanced classification performance.

## Contributors

- Abdul Munneb Qureshi ([GitHub](https://github.com/Abdul-Muneeb-Qureshi))
- Ammar Farooq
