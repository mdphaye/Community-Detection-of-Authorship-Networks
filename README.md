# Community Detection of Authorship Networks

_A comparative study and visualization framework for analyzing collaborative patterns in multi-layer co-authorship-like networks._

## Overview

Community Detection of Authorship Networks is a comprehensive Python framework designed for studying collaboration patterns within multi-layer co-authorship-like networks. This repository provides tools for comparative analysis, algorithmic evaluation, and intuitive visualization, enabling in-depth exploration of network communities and structures.

## Features

- **Comparative Study**: Analyze and compare the performance of various community detection algorithms on co-authorship networks.
- **Visualization Tools**: Generate insightful visualizations to illustrate collaborative patterns and detected communities.
- **Multi-layer Network Support**: Handle networks with multiple layers to model complex interactions and relationships.
- **Customizable Evaluation Metrics**: Assess and validate detected communities using various metrics.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Recommended packages (please see `requirements.txt` for the full list):
  - NetworkX
  - Matplotlib
  - NumPy
  - Pandas
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

- `analysis/` — Scripts and modules for comparative studies of community detection algorithms
- `visualization/` — Modules for network and community visualization
- `data/` — Sample data and templates for loading networks
- `examples/` — Example use cases and tutorials
- `requirements.txt` — List of required Python packages

## Algorithms Supported

- Louvain
- Infomap
- Label Propagation
- Other popular community detection algorithms

## Contributing

Contributions are welcome! Please submit issues or pull requests for improvements, bug fixes, and new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Citation

If you use this framework in your research, please consider citing the repository:

```
Phaye, M. (2025). Community Detection of Authorship Networks: A Comparative Study and Visualization Framework. GitHub Repository. https://github.com/mdphaye/Community-Detection-of-Authorship-Networks
```

## Contact

For questions or inquiries, please open an issue or contact the repository maintainer.

---
