import networkx as nx
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from tqdm import tqdm

import csv

import string


def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())
    
    # Removing punctuation
    tokens = [token for token in tokens if token not in string.punctuation]
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Stemming
    stemmer = SnowballStemmer("english")
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens

# Function to construct directed graph from text
def construct_graph(text):
    # Preprocess text
    tokens = preprocess_text(text)
    
    # Initialize directed graph
    G = nx.DiGraph()
    
    # Add nodes and edges based on term relationships
    for i in range(len(tokens)-1):
        if G.has_edge(tokens[i], tokens[i+1]):
            G[tokens[i]][tokens[i+1]]['weight'] += 1
        else:
            G.add_edge(tokens[i], tokens[i+1], weight=1)
    return G



def read_from_file(filename):
    data = []
    graphs = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row
        total_rows = sum(1 for row in reader)  # Count the total number of rows

    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row
        for row in tqdm(reader, desc=f"Reading {filename}", total=total_rows):
            link, cleaned_text, stemmed_text, category, _ = row

            graph = construct_graph(cleaned_text)
            graphs.append(graph)
            data.append({
                'Link': link,
                'Cleaned Text': cleaned_text,
                'Stemmed Text': stemmed_text,
                'Category': category,
                'Graph': graph
            })
    return data, graphs

def read_graphs_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    graphs = []  # List to store multiple graphs

    # Parse each line to extract vertices and edges
    for line in lines:
        if line.startswith("t"):
            # Create a new graph for each "t" line
            G = nx.DiGraph()
            graphs.append(G)
            vertex_labels = {}  
        elif line.startswith("v"):
            _, vertex_id, vertex_label = line.strip().split()
            vertex_labels[vertex_id] = vertex_label
        elif line.startswith("e"):
            _, source_id, target_id, _ = line.strip().split()
            G.add_edge(vertex_labels[source_id], vertex_labels[target_id])

    return graphs


def write_graphs_to_file(graphs, filename):
    with open(filename, 'w' ,  encoding='utf-8') as f:
        for graph_idx, graph in enumerate(graphs[:12]):
            node_mapping = {}  # To store the mapping between NetworkX node IDs and gSpan node IDs
            gspan_node_id = 0
            
            # Write a header for the graph
            f.write(f"t # {graph_idx}\n")
            
            # Write vertices
            for node in graph.nodes():
                node_mapping[node] = gspan_node_id
                line = f"v {gspan_node_id} {node}\n"
                f.write(line)
                gspan_node_id += 1
            
            # Write edges
            for edge in graph.edges():
                source, target = edge
                gspan_source = node_mapping[source]
                gspan_target = node_mapping[target]
                line = f"e {gspan_source} {gspan_target} 2\n"
                f.write(line)

        f.write(f"t # {-1}\n")

        return
