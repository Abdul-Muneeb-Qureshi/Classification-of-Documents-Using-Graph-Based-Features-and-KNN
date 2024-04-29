import random
import networkx as nx
from functions import read_from_file , read_graphs_from_file
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns




def read_data(file_path):
    """Read data from the specified file and return graphs."""
    print("Reading data from file...")
    data, graphs = read_from_file(file_path)
    return graphs

def compute_mcs(graph1, graph2):
    """Compute the maximum common subgraph between two graphs."""
    matching_graph = nx.Graph()
    for n1, n2 in graph2.edges():
        if graph1.has_edge(n1, n2):
            matching_graph.add_edge(n1, n2)
    if matching_graph.number_of_edges() == 0:
        return nx.Graph()  # Return an empty graph if no common edges are found
    components = nx.connected_components(matching_graph)
    largest_component = max(components, key=len)
    return nx.induced_subgraph(matching_graph, largest_component)
def custom_distance(query_features, graph_features):
    """Compute Euclidean distance between two feature vectors."""
    # Convert feature vectors to numpy arrays for efficient computation
    query_features = np.array(query_features)
    graph_features = np.array(graph_features)
    
    
    # Compute Euclidean distance
    distance = 1- (np.sum((query_features - graph_features) ** 2))/max(len(query_features) ,len(graph_features))
    # distance = np.sum(query_features - graph_features)
    
    return distance

def compute_distance(query_graph_features, feature_matrix):
    """Compute distance between the query graph and each graph in the feature matrix."""
    distances = []
    for features, _ in feature_matrix:
        distance = custom_distance(query_graph_features, features)
        distances.append(distance)
    return distances


def shuffle_dataset(dataset):
    random.shuffle(dataset)
    return dataset

def knn(query_features ,feature_matrix, k):
    """Perform k-nearest neighbors classification."""
    
    distances = compute_distance(query_features, feature_matrix)
    neighbors = [(label, distance) for (_, label), distance in zip(feature_matrix, distances)]
    neighbors.sort(key=lambda x: x[1] , reverse=True)
    nearest_neighbors = neighbors[:k]
    return nearest_neighbors

def create_feature_vector(graph, frequent_subgraphs):
    """Create a feature vector indicating presence of frequent subgraphs."""
    features = []
    for subgraph in frequent_subgraphs:
        if set(subgraph.nodes()).issubset(graph.nodes()):
            features.append(1)
        else:
            features.append(0)
    return features

def create_feature_matrix(train_set, frequent_subgraphs):
    feature_matrix = []
    for graph, label in train_set:
        # Create feature vector for the current graph
        graph_features = create_feature_vector(graph, frequent_subgraphs)
        # Append the feature vector and label to the feature matrix
        feature_matrix.append((graph_features, label))
    return feature_matrix

# Main function
def main():
    # Read data from files
    diseases_graphs = read_data('../Scrapping/scrapping_Diseases_Symptoms.csv')
    fashion_graphs = read_data('../Scrapping/scrapping_Beauty_Fashion.csv')
    food_graphs = read_data('../Scrapping/scrapping_Food.csv')




    test_set = diseases_graphs[12:15] + fashion_graphs[12:15] + food_graphs[12:15]

    print(len(diseases_graphs[12:15]) , len(fashion_graphs[12:15]) , len(food_graphs[12:15]))


    # Create labeled dataset
    dataset = diseases_graphs[:12] + fashion_graphs[:12] + food_graphs[:12]
    labels = ["Diseases"] * 12 + ["Fashion"] * 12 + ["Food"] * 12
    labeled_dataset = list(zip(dataset, labels))
    train_set = shuffle_dataset(labeled_dataset)

    test_set = diseases_graphs[12:15] + fashion_graphs[12:15] + food_graphs[12:15]
    labels = ["Diseases"] * 3 + ["Fashion"] * 3 + ["Food"] * 3
    test_set = list(zip(test_set, labels))
    # test_set = shuffle_dataset(test_set)



    frequent_subgraph = read_graphs_from_file('../GraphDataBase/frequentSubgrphs.txt')

    feature_train_matrix = create_feature_matrix(train_set, frequent_subgraph)

    feature_test_matrix = create_feature_matrix(test_set , frequent_subgraph)


    results = []

    for features , label in feature_test_matrix:
        nearest_neighbors =knn(features,feature_train_matrix, 5)
        neighbor_labels = [neighbor[0] for neighbor in nearest_neighbors]
        label_counts = Counter(neighbor_labels)
        most_common_label = max(label_counts, key=label_counts.get)
        print(nearest_neighbors)
        results.append((label, most_common_label))




    # # Calculate accuracy
    correct_predictions = sum(1 for true_label, pred_label in results if true_label == pred_label or pred_label == "equal")
    accuracy = correct_predictions / len(test_set)
    print("Accuracy:", accuracy)


    true_labels = [true_label for _, true_label in test_set]
    predicted_labels = [pred_label for _, pred_label in results]

    accuracy = accuracy_score(true_labels, predicted_labels)
    precision = precision_score(true_labels, predicted_labels, average='weighted')
    recall = recall_score(true_labels, predicted_labels, average='weighted')
    f1 = f1_score(true_labels, predicted_labels, average='weighted')

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)

    # Plot confusion matrix
    cm = confusion_matrix(true_labels, predicted_labels)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', xticklabels=['Diseases', 'Fashion', 'Food'], yticklabels=['Diseases', 'Fashion', 'Food'])
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

if __name__ == "__main__":
    main()
