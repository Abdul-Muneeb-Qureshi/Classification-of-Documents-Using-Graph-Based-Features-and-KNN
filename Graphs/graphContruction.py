import networkx as nx
import matplotlib.pyplot as plt
from functions import read_from_file , write_graphs_to_file 


# Function to visualize the graph
def visualize_graph(graph):
    pos = nx.spring_layout(graph)  # Position nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, edge_color='black', linewidths=1, arrows=True)
    plt.title("Directed Graph Visualization")
    plt.show()



def process_file(file_path, text_filename):
   
    print("File Reading start.....")
    data, graphs = read_from_file(file_path)
    write_graphs_to_file(graphs, text_filename)
    print(f"Successfully {text_filename} Graph Created............")

def main():
    # process_file('../Scrapping/scrapping_Diseases_Symptoms.csv', '../GraphDataBase/diseases_symptoms_graph.txt')
    # process_file('../Scrapping/scrapping_Beauty_Fashion.csv', '../GraphDataBase/beauty_fashion_graph.txt')
    process_file('../Scrapping/scrapping_Food.csv', '../GraphDataBase/food_graph.txt')
    # process_file('../Scrapping/data.csv', '../GraphDataBase/data.txt')


if __name__ == "__main__":
    main()






