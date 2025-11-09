# coauthorship_story_network.py
# Story-driven multi-layer co-authorship-like network:
# - Main meta nodes (cross-universe bridges): Mangalya, Ridima, Divyansh
# - Layer A: The Office characters (logical links from the show's storyline)
# - Layer B: Stranger Things characters (friendships/relations from show)
# - Layer C: Mahabharat characters (canonical relations)
#
# Produces layered visualization + per-algorithm community plots.
# Author: generated for Mangalya
# Date: 2025-11

import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np

try:
    import community as community_louvain  # python-louvain
    HAVE_LOUVAIN = True
except Exception:
    HAVE_LOUVAIN = False

OUT = "coauthorship_outputs"
os.makedirs(OUT, exist_ok=True)


def build_story_network():
    """
    Build a logical, story-driven network combining:
    - Main meta nodes (bridges)
    - Office (secondary)
    - Stranger Things (tertiary)
    - Mahabharat (layer4)
    Returns graph and the four node lists in hierarchical order.
    """
    G = nx.Graph()

    # Main meta nodes (cross-universe bridges)
    main_nodes = ["Mangalya", "Ridima", "Divyansh"]

    # The Office characters (story-driven links)
    office_nodes = [
        "Michael", "Jim", "Pam", "Dwight", "Andy", "Stanley",
        "Kevin", "Meredith", "Creed", "Ryan", "Holly", "Erin"
    ]

    # Stranger Things characters (story-driven links)
    stranger_nodes = [
        "Mike", "Eleven", "Will", "Joyce", "Jonathan", "Nancy", "Steve", "Billy"
    ]

    # Mahabharat characters (canonical relations)
    mahabharat_nodes = [
        "Yudhishthira", "Bhima", "Arjuna", "Nakula", "Sahadeva",
        "Krishna", "Karna", "Duryodhana", "Bhishma", "Drona", "Abhimanyu", "Draupadi"
    ]

    # Add nodes
    G.add_nodes_from(main_nodes + office_nodes + stranger_nodes + mahabharat_nodes)

    # ----------------------
    # Main core: strong ties among meta-nodes
    # ----------------------
    for i in range(len(main_nodes)):
        for j in range(i + 1, len(main_nodes)):
            G.add_edge(main_nodes[i], main_nodes[j], weight=4)  # strong bridging ties

    # ----------------------
    # The Office: logical edges following storyline
    # ----------------------
    # Michael is boss — edges to core office staff
    office_edges = [
        ("Michael", "Jim"), ("Michael", "Pam"), ("Michael", "Dwight"),
        ("Michael", "Andy"), ("Michael", "Stanley")
    ]
    # Jim & Pam (romantic + co-workers), Jim & Dwight (prank/rivalry), Dwight small clique
    office_edges += [
        ("Jim", "Pam"), ("Jim", "Dwight"), ("Pam", "Dwight"),
        ("Dwight", "Andy"), ("Andy", "Stanley"), ("Stanley", "Kevin"),
        ("Kevin", "Meredith"), ("Meredith", "Creed"), ("Creed", "Ryan"),
        ("Ryan", "Kelly")  # Kelly not in list; ignore if absent — kept conceptual (no effect)
    ]
    # Add Erin & Holly as HR-related / romantic subplot edges
    office_edges += [
        ("Holly", "Michael"), ("Erin", "Andy"), ("Holly", "Dwight")
    ]

    # Filter out any non-existent pair safely and add
    for (a, b) in office_edges:
        if a in G.nodes() and b in G.nodes():
            G.add_edge(a, b)

    # ----------------------
    # Stranger Things: logical edges
    # ----------------------
    st_edges = [
        ("Mike", "Eleven"), ("Mike", "Will"), ("Mike", "Jonathan"),
        ("Eleven", "Will"), ("Eleven", "Mike"),
        ("Joyce", "Will"), ("Joyce", "Jonathan"),
        ("Jonathan", "Nancy"), ("Nancy", "Steve"),
        ("Steve", "Billy"),  # Steve / Billy antagonism (connected, but weak)
        ("Billy", "Will")    # antagonistic tie — included to represent conflict
    ]
    for a, b in st_edges:
        if a in G.nodes() and b in G.nodes():
            # weight friend=2, antagonist=1 (approx)
            w = 2 if (a, b) in [("Mike", "Eleven"), ("Mike", "Will"), ("Jonathan", "Nancy")] else 1
            G.add_edge(a, b, weight=w)

    # Tertiary interconnects within ST (peer clique)
    st_clique = [("Mike", "Jonathan"), ("Eleven", "Nancy"), ("Steve", "Jonathan")]
    for a, b in st_clique:
        if a in G.nodes() and b in G.nodes():
            G.add_edge(a, b, weight=2)

    # ----------------------
    # Mahabharat: canonical relations and alliances
    # ----------------------
    # Pandavas clique
    pandavas = ["Yudhishthira", "Bhima", "Arjuna", "Nakula", "Sahadeva"]
    for i in range(len(pandavas)):
        for j in range(i + 1, len(pandavas)):
            G.add_edge(pandavas[i], pandavas[j], weight=3)

    # Allies & key relations
    mahab_edges = [
        ("Krishna", "Arjuna"), ("Karna", "Duryodhana"), ("Duryodhana", "Karna"),
        ("Bhishma", "Kaurava")  # Kaurava not present — conceptual
    ]
    # specific edges
    mahab_edges += [
        ("Bhishma", "Duryodhana"), ("Drona", "Karna"), ("Drona", "Duryodhana"),
        ("Abhimanyu", "Arjuna"), ("Draupadi", "Yudhishthira"), ("Draupadi", "Arjuna"),
        ("Karna", "Duryodhana")
    ]
    for a, b in mahab_edges:
        if a in G.nodes() and b in G.nodes():
            G.add_edge(a, b, weight=2)

    # ----------------------
    # Cross-universe semantic bridges (main meta nodes connect to representative characters)
    # - Mangalya, Ridima, Divyansh act as interpreters / meta-connectors across stories
    # ----------------------
    # Mangalya (empathetic / mediator) connects to Pam, Eleven, Draupadi, Arjuna (advice/empathy)
    bridges = [
        ("Mangalya", "Pam"), ("Mangalya", "Eleven"), ("Mangalya", "Draupadi"), ("Mangalya", "Arjuna")
    ]
    # Ridima (strategic / connector) connects to Jim, Mike, Krishna, Yudhishthira
    bridges += [
        ("Ridima", "Jim"), ("Ridima", "Mike"), ("Ridima", "Krishna"), ("Ridima", "Yudhishthira")
    ]
    # Divyansh (provocative / challenger) connects to Dwight, Joyce, Karna, Duryodhana
    bridges += [
        ("Divyansh", "Dwight"), ("Divyansh", "Joyce"), ("Divyansh", "Karna"), ("Divyansh", "Duryodhana")
    ]
    for a, b in bridges:
        if a in G.nodes() and b in G.nodes():
            G.add_edge(a, b, weight=2)

    # ----------------------
    # Add a few cross-layer thematic parallels for realism:
    # e.g., Dwight <-> Bhima (strength/loyalty), Jim <-> Mike (prankster/leader parallels),
    # Pam <-> Draupadi (emotional center), Eleven <-> Krishna (mystic guide analogue)
    thematic = [
        ("Dwight", "Bhima"), ("Jim", "Mike"), ("Pam", "Draupadi"),
        ("Eleven", "Krishna"), ("Steve", "Karna")  # Steve (protector) vs Karna (warrior) as a rough analog
    ]
    for a, b in thematic:
        if a in G.nodes() and b in G.nodes():
            G.add_edge(a, b, weight=1)

    return G, main_nodes, office_nodes, stranger_nodes, mahabharat_nodes


def draw_layered_graph(G, main_nodes, office_nodes, stranger_nodes, mahab_nodes, title, filename):
    """Layered shell layout + descriptive legends. Keeps labels readable and well separated."""
    plt.figure(figsize=(13, 9))
    plt.title(title, fontsize=14, fontweight='bold')

    # Shell layout with the four concentric groups (main at center)
    pos = nx.shell_layout(G, nlist=[main_nodes, office_nodes, stranger_nodes, mahab_nodes])

    # Styling per layer: sizes and legend labels
    layers = [
        (main_nodes, 1100, "Main (Meta bridges)"),
        (office_nodes, 700, "The Office (Story characters)"),
        (stranger_nodes, 600, "Stranger Things (Story characters)"),
        (mahab_nodes, 650, "Mahabharat (Epic characters)")
    ]

    cmap = plt.cm.get_cmap("Set2")
    for i, (nodes, size, label) in enumerate(layers):
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_size=size,
                               node_color=[cmap(i)], label=label)
    nx.draw_networkx_edges(G, pos, alpha=0.35)
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight='medium')
    plt.legend(scatterpoints=1, loc='upper left', fontsize=10, frameon=True)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, filename), dpi=250)
    plt.close()


def detect_communities(G):
    """
    Run multiple community detection algorithms.
    Returns results as dict:
      key: descriptive algorithm name,
      value: (partition_dict node->community_id, modularity or None)
    """
    results = {}

    # 1. Louvain Modularity Optimization (if available)
    if HAVE_LOUVAIN:
        part = community_louvain.best_partition(G, weight='weight')
        mod = community_louvain.modularity(part, G, weight='weight')
        results["Louvain Modularity Optimization"] = (part, mod)
    else:
        # If python-louvain not installed, skip but still include a placeholder entry
        # (user can install python-louvain to get this result)
        pass

    # 2. Greedy Modularity Maximization (NetworkX)
    gm_comms = list(nx.algorithms.community.greedy_modularity_communities(G, weight='weight'))
    gm_part = {n: cid for cid, c in enumerate(gm_comms) for n in c}
    gm_mod = nx.algorithms.community.quality.modularity(G, gm_comms, weight='weight')
    results["Greedy Modularity Maximization"] = (gm_part, gm_mod)

    # 3. Label Propagation (fast, non-deterministic)
    lp_comms = list(nx.algorithms.community.label_propagation_communities(G))
    lp_part = {n: cid for cid, c in enumerate(lp_comms) for n in c}
    results["Label Propagation (Diffusion)"] = (lp_part, None)

    # 4. Girvan-Newman (Edge Betweenness, hierarchical) - take first split
    comp = nx.algorithms.community.girvan_newman(G)
    try:
        first_level = tuple(sorted(c) for c in next(comp))
        gn_part = {n: cid for cid, c in enumerate(first_level) for n in c}
        gn_mod = nx.algorithms.community.quality.modularity(G, first_level, weight='weight')
        results["Girvan-Newman (Edge Betweenness)"] = (gn_part, gn_mod)
    except StopIteration:
        # graph too small / GN failed; skip
        pass

    # 5. Spectral Clustering (Laplacian) using sklearn
    try:
        from sklearn.cluster import SpectralClustering
        A = nx.to_numpy_array(G)
        n_clusters = min(6, max(2, len(G) // 6))
        sc = SpectralClustering(n_clusters=n_clusters, affinity='precomputed', random_state=42)
        labels = sc.fit_predict(A)
        sp_part = {node: int(labels[i]) for i, node in enumerate(G.nodes())}
        results["Spectral Clustering (Laplacian)"] = (sp_part, None)
    except Exception:
        # sklearn not installed or failed -> skip spectral
        pass

    return results


def save_community_plots(G, results):
    """Draw per-algorithm community plots with descriptive algorithm names and readable modularity text."""
    # base layout for communities (use deterministic spring layout)
    pos = nx.spring_layout(G, seed=42)

    for algo_name, (partition, modularity) in results.items():
        # partition is dict node->community id
        # Build communities
        communities = {}
        for n, cid in partition.items():
            communities.setdefault(cid, []).append(n)

        plt.figure(figsize=(11, 9))
        mod_txt = f"Modularity={modularity:.3f}" if (modularity is not None) else "Modularity=Not Applicable"
        plt.title(f"{algo_name} — {mod_txt}", fontsize=13)

        cmap = plt.cm.get_cmap("tab10")
        for i, (cid, members) in enumerate(communities.items()):
            nx.draw_networkx_nodes(G, pos, nodelist=members, node_size=420,
                                   node_color=[cmap(i % 10)], label=f"Cluster {i + 1}")
        nx.draw_networkx_edges(G, pos, alpha=0.35)
        nx.draw_networkx_labels(G, pos, font_size=8)
        plt.legend(loc='upper left', fontsize=9)
        plt.axis("off")
        safe_name = algo_name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace(",", "")
        plt.tight_layout()
        plt.savefig(os.path.join(OUT, f"network_{safe_name}.png"), dpi=250)
        plt.close()


if __name__ == "__main__":
    G, main_nodes, office_nodes, stranger_nodes, mahab_nodes = build_story_network()

    # 1) Overview layered visualization (structure without algorithmic coloring)
    draw_layered_graph(G, main_nodes, office_nodes, stranger_nodes, mahab_nodes,
                       "Story-driven Four-layer Network (Office, Stranger Things, Mahabharat)",
                       "network_story_layered.png")

    # 2) Run community detection
    results = detect_communities(G)

    # 3) Save community-specific visuals
    save_community_plots(G, results)

    # 4) Console summary
    print("Community detection summary (descriptive names; modularity if available):\n")
    for algo_name, (partition, modularity) in results.items():
        n_communities = len(set(partition.values()))
        mod_str = f"{modularity:.3f}" if (modularity is not None) else "Not Applicable"
        print(f"{algo_name:40} -> Communities: {n_communities:2d}  |  Modularity: {mod_str}")

    print(f"\nAll visualizations saved in the folder: {OUT}")
