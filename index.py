import networkx as nx
import numpy as np
import pandas as pd


def create_network(network_type, n, p=0.1, m=2):
    if network_type == 'ER':
        return nx.erdos_renyi_graph(n, p)
    elif network_type == 'SW':
        return nx.watts_strogatz_graph(n, 4, p)
    elif network_type == 'BA':
        return nx.barabasi_albert_graph(n, m)
    else:
        raise ValueError("نوع شبکه نامعتبر است.")


def generate_beliefs(n, belief_type):
    if belief_type == 1:
        return [1] * n
    elif belief_type == 2:
        return [-1] * n
    elif belief_type == 3:
        return [np.random.choice([-1, 1]) for _ in range(n)]
    else:
        raise ValueError("نوع عقیده نامعتبر است.")


def create_signed_matrix(adjacency_matrix):
    # ایجاد ماتریس علامت‌دار بر اساس ماتریس مجاورت
    signed_matrix = np.zeros_like(adjacency_matrix)
    for i in range(adjacency_matrix.shape[0]):
        for j in range(i + 1, adjacency_matrix.shape[1]):
            if adjacency_matrix[i][j] == 1:
                sign = np.random.choice([-1, 1])
                signed_matrix[i][j] = sign
                signed_matrix[j][i] = sign
    return signed_matrix


def calculate_energy(G, signed_matrix, belief_type):
    n = G.number_of_nodes()
    beliefs = generate_beliefs(n, belief_type)

    energy = 0
    for i in range(n):
        for j in range(i + 1, n):  # فقط یک‌بار هر جفت را حساب می‌کنیم
            energy -= signed_matrix[i][j] * beliefs[i] * beliefs[j]

    return energy


def create_graph_from_csv(file_path):
    df = pd.read_csv(file_path, delim_whitespace=True)  # Use delim_whitespace to handle
    G = nx.Graph()
    for index, row in df.iterrows():
        source = row[0]
        target = row[1]
        G.add_edge(source, target)
    return G


# تست برای شبکه‌های مصنوعی
network_types = ['ER', 'SW', 'BA']
n = 100  # تعداد گره‌ها

for network_type in network_types:
    G = create_network(network_type, n)
    adjacency_matrix = nx.to_numpy_array(G)
    signed_matrix = create_signed_matrix(adjacency_matrix)
    for belief_type in [1, 2, 3]:
        energy = calculate_energy(G, signed_matrix, belief_type)
        print(f"انرژی شبکه {network_type} با نوع عقیده {belief_type}: {energy}")

# تست برای شبکه‌های واقعی
real_network_paths = ['Celegans_Metabolic_453node.csv', 'Dolphins_63node.csv', 'Karate_Club_33node.csv',
                      'Typical_Cortex_63node.csv']

for network_path in real_network_paths:
    G = create_graph_from_csv(network_path)
    adjacency_matrix = nx.to_numpy_array(G)
    signed_matrix = create_signed_matrix(adjacency_matrix)
    for belief_type in [1, 2, 3]:
        energy = calculate_energy(G, signed_matrix, belief_type)
        print(f" انرژی شبکه {network_path} با نوع عقیده {belief_type}: {energy}")
