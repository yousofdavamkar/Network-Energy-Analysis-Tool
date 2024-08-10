# Network Energy Analysis Tool 🌐⚡

## Overview

This project provides a comprehensive tool for analyzing the energy of various network types based on different belief configurations. It supports both synthetic network models and real-world network data.

---

## 🚀 Features

- **Synthetic Network Generation**
  - Erdős-Rényi (ER) model
  - Watts-Strogatz (SW) model
  - Barabási-Albert (BA) model

- **Real Network Analysis**
  - Support for CSV input files

- **Belief Configuration**
  - All positive beliefs
  - All negative beliefs
  - Random belief distribution

- **Energy Calculation**
  - Based on network structure and belief configuration

---

## 🛠️ Dependencies

- [NetworkX](https://networkx.org/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)

---

## 📊 Supported Network Types

### Synthetic Networks
- Erdős-Rényi (ER)
- Watts-Strogatz (SW)
- Barabási-Albert (BA)

### Real Networks
- C. elegans Metabolic Network (453 nodes)
- Dolphin Social Network (63 nodes)
- Zachary's Karate Club (33 nodes)
- Typical Cortex Network (63 nodes)

---

## 🖥️ Usage

1. **Create a network:**
   ```python
   G = create_network('ER', n=100, p=0.1)

Generate beliefs:
pythonCopybeliefs = generate_beliefs(n=100, belief_type=3)

Calculate network energy:
pythonCopyenergy = calculate_energy(G, signed_matrix, belief_type=3)

Analyze real networks:
pythonCopyG = create_graph_from_csv('Dolphins_63node.csv')



📈 Example Output
CopyEnergy of ER network with belief type 1: -245.0
Energy of SW network with belief type 2: -196.0
Energy of BA network with belief type 3: -97.0
Energy of Celegans_Metabolic_453node.csv with belief type 1: -1012.0

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

📝 License
This project is MIT licensed.

<p align="center">
  Made with ❤️ by [Your Name]
</p>
