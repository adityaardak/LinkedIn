import numpy as np
from scipy.stats import entropy

def main():
    #consider example distributions
    P = np.array([0.4, 0.35, 0.2, 0.05])  # Expected distribution
    Q = np.array([0.5, 0.3, 0.15, 0.05])  # Observed distribution

    #We just need to  Ensure that both P and Q are valid probability distributions
    assert np.isclose(np.sum(P), 1.0), "P must sum to 1"
    assert np.isclose(np.sum(Q), 1.0), "Q must sum to 1"

    #Now Ccalculate the KL Divergence using scipy's entropy function (base e by default)
    kl_value = entropy(P, Q)
    print(f"KL Divergence between P and Q: {kl_value:.4f}")

if __name__ == "__main__":
    main()
