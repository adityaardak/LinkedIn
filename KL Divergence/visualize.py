import numpy as np
import matplotlib.pyplot as plt

def visualize_distributions(P, Q, labels=None):
    """
    Visualizes two probability distributions P and Q as bar plots.
    
    Parameters:
        - P: The "expected" probability distribution.
        - Q: The "actual" probability distribution.
        - labels: List of labels for each category, optional.
    """
    indices = np.arange(len(P))

    if labels is None:
        labels = [f"Category {i+1}" for i in range(len(P))]

    plt.figure(figsize=(10, 6))

    # Plot the "expected" distribution
    plt.bar(indices - 0.2, P, width=0.4, label='Expected Distribution (P)', color='blue', alpha=0.7)

    # Plot the "actual" distribution
    plt.bar(indices + 0.2, Q, width=0.4, label='Actual Distribution (Q)', color='orange', alpha=0.7)

    # Add labels, title, and legend
    plt.xlabel('Categories')
    plt.ylabel('Probability')
    plt.title('Comparison of Expected and Actual Distributions')
    plt.xticks(indices, labels)
    plt.legend(loc='best')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    # Example distributions
    P = np.array([0.4, 0.35, 0.2, 0.05])  # Expected distribution
    Q = np.array([0.5, 0.3, 0.15, 0.05])  # Observed distribution
    labels = ["A", "B", "C", "D"]  # Example labels for categories

    # Visualize the distributions
    visualize_distributions(P, Q, labels)

if __name__ == "__main__":
    main()
