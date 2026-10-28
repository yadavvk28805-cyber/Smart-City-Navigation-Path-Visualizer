
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from graph_data import city_graph
from algorithms import dijkstra

st.set_page_config(
    page_title="DAA Path Visualizer",
    page_icon="🗺️",
    layout="centered"
)

st.title("🗺️ Smart City Navigation & Path Visualizer")
st.markdown("### Design and Analysis of Algorithms (DAA) Project")
st.write("Project using **Dijkstra's Algorithm** with Python and Streamlit.")

# Validate graph data
if not city_graph:
    st.error("City graph is empty. Please check graph_data.py.")
    st.stop()

nodes = list(city_graph.keys())

# Source and destination selection
col1, col2 = st.columns(2)

with col1:
    start_node = st.selectbox(
        "Select Source Node:",
        nodes,
        index=0
    )

with col2:
    default_goal_index = min(4, len(nodes) - 1)
    goal_node = st.selectbox(
        "Select Destination Node:",
        nodes,
        index=default_goal_index
    )

if st.button("Find Shortest Path", type="primary"):
    if start_node == goal_node:
        st.warning("Source and Destination cannot be the same!")
    else:
        try:
            path, total_cost = dijkstra(
                city_graph, start_node, goal_node
            )

            if path:
                st.success(
                    f"Shortest Path Found: {' ➔ '.join(map(str, path))}"
                )
                st.info(f"Total Minimum Cost / Distance: {total_cost}")

                # Create graph for visualization
                G = nx.Graph()

                for node, edges in city_graph.items():
                    G.add_node(node)

                    for neighbor, weight in edges.items():
                        G.add_edge(node, neighbor, weight=weight)

                # Draw graph
                fig, ax = plt.subplots(figsize=(8, 5))
                pos = nx.spring_layout(G, seed=42)

                nx.draw_networkx_nodes(
                    G, pos,
                    node_color="lightblue",
                    node_size=800,
                    ax=ax
                )

                nx.draw_networkx_labels(
                    G, pos,
                    font_weight="bold",
                    ax=ax
                )

                nx.draw_networkx_edges(
                    G, pos,
                    edge_color="gray",
                    ax=ax
                )

                edge_labels = nx.get_edge_attributes(G, "weight")
                nx.draw_networkx_edge_labels(
                    G, pos,
                    edge_labels=edge_labels,
                    ax=ax
                )

                # Highlight shortest path
                path_edges = list(zip(path[:-1], path[1:]))

                nx.draw_networkx_nodes(
                    G, pos,
                    nodelist=path,
                    node_color="orange",
                    node_size=850,
                    ax=ax
                )

                nx.draw_networkx_edges(
                    G, pos,
                    edgelist=path_edges,
                    edge_color="red",
                    width=3,
                    ax=ax
                )

                ax.set_title("Shortest Path Visualization")
                ax.axis("off")

                st.pyplot(fig)
                plt.close(fig)

            else:
                st.error("No path found between selected nodes!")

        except Exception as e:
            st.error(f"An error occurred: {e}")
