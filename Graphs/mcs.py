import random
import networkx as nx
from functions import read_from_file
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def process_file(file_path):
    print("File Reading start.....")
    data, graphs = read_from_file(file_path)
    return graphs

def getMCS(g1, g2):
    matching_graph = nx.Graph()
    for n1, n2 in g2.edges():
        if g1.has_edge(n1, n2):
            matching_graph.add_edge(n1, n2)
    if matching_graph.number_of_edges() == 0:
        return nx.Graph()  # Return an empty graph if no common edges are found
    components = nx.connected_components(matching_graph)
    largest_component = max(components, key=len)
    return nx.induced_subgraph(matching_graph, largest_component)

def compute_distance(graph1, graph2):
    mcs = getMCS(graph1, graph2)
    max_size = max(len(graph1), len(graph2))
    distance = 1 - (len(mcs) / max_size)
    return distance

def shuffle_dataset(dataset):
    random.shuffle(dataset)
    return dataset

def knn(query_graph, dataset, k):
    distances = []
    for graph, label in dataset:
        distance = compute_distance(query_graph, graph)
        distances.append((graph, label,distance))
    distances.sort(key=lambda x: x[2])

    nearest_neighbors = distances[:k]
    print(nearest_neighbors)
    return nearest_neighbors


diseases_graphs = process_file('../Scrapping/scrapping_Diseases_Symptoms.csv')
fashion_graphs = process_file('../Scrapping/scrapping_Beauty_Fashion.csv')
food_graphs = process_file('../Scrapping/scrapping_Food.csv')




test_set = diseases_graphs[12:15] + fashion_graphs[12:15] + food_graphs[12:15]

dataset = diseases_graphs[:12] + fashion_graphs[:12] + food_graphs[:12]
labels = ["Diseases"] * 12 + ["Fashion"] * 12 + ["Food"] * 12
labeled_dataset = list(zip(dataset, labels))
train_set = shuffle_dataset(labeled_dataset)




test_set = diseases_graphs[12:15] + fashion_graphs[12:15] + food_graphs[12:15]
labels = ["Diseases"] * 3 + ["Fashion"] * 3 + ["Food"] * 3
test_set = list(zip(test_set, labels))
test_set = shuffle_dataset(test_set)



# Example usage
k = 5 # Number of neighbors to find
results = []

for test_graph, test_label in test_set:
    print(test_label)
    nearest_neighbors = knn(test_graph, train_set, k)

    predicted_label = max(set([label for _, label,_ in nearest_neighbors]), key=[label for _, label ,_ in nearest_neighbors].count)
    results.append((test_label, predicted_label))
    print(results)
    



# Calculate accuracy
correct_predictions = sum(1 for true_label, pred_label in results if true_label == pred_label)
accuracy = correct_predictions / len(test_set)
print("Accuracy:", accuracy)

predicted_labels = [pred_label for _, pred_label in results]
true_labels =  [true_label for true_label, _ in results]


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

