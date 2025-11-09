# Community Detection of Authorship Networks

_A comparative study and visualization framework for analyzing collaborative patterns in multi-layer co-authorship-like networks._

## Overview

Community Detection of Authorship Networks is a comprehensive Python framework designed for studying collaboration patterns within multi-layer co-authorship-like networks. This repository provides tools for comparative analysis, algorithmic evaluation, and intuitive visualization, enabling in-depth exploration of network communities and structures.
This project explores community detection techniques applied to a multi-layer, story-driven co-authorship-like network, conceptualized as a model for real-world scientific collaboration.
It integrates characters from three narrative domains — The Office, Stranger Things, and Mahabharat — interconnected through meta-authors (Mangalya, Ridima, and Divyansh) that serve as bridges across layers.

## Objectives

- **Comparative Study**: Analyze and compare the performance of various community detection algorithms on co-authorship networks.
- **Visualization Tools**: Generate insightful visualizations to illustrate collaborative patterns and detected communities.
- **Multi-layer Network Support**: Handle networks with multiple layers to model complex interactions and relationships.
- **Customizable Evaluation Metrics**: Assess and validate detected communities using various metrics.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Recommended packages (please see `requirements.txt` for the full list):
  - networkx
  - matplotlib
  - numpy
  - python-louvain
  - scikit-learn

### Installation

Clone the repository:

```bash
git clone https://github.com/mdphaye/Community-Detection-of-Authorship-Networks.git
cd Community-Detection-of-Authorship-Networks
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

The main scripts and modules can be run directly or adapted for your research needs. Detailed usage instructions and examples can be found in the `examples/` directory.

#### Example: Running Comparative Analysis

```bash
python analysis/comparative_study.py --input data/network_data.csv --algorithm louvain
```

#### Example: Generating Visualizations

```bash
python visualization/visualize_network.py --network data/network_data.csv --output results/figure.png
```

_Complete documentation for modules and scripts is available in the repository._

## Project Structure
- `requirements.txt` — List of required Python packages
- `Community Detection/` — Coauthorship.py
- `Coauthorship_outputs/` — network_girvan-newman_edge_betweenness.png
		                        network_greedy_modularity_maximization.png
		                        network_label_propagation_diffusion.png
		                        network_louvain_modularity_optimization.png
		                        network_spectral_clustering_laplacian.png
		                        network_story_layered.png

## Algorithms Supported

1. Louvain Modularity Optimization
2. Greedy Modularity Maximization
3. Label Propagation
4. Girvan–Newman (Edge Betweenness)
5. Spectral Clustering (Laplacian-based)

## Contributing

Contributions are welcome! Please submit issues or pull requests for improvements, bug fixes, and new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
