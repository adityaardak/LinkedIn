import numpy as np

def kl_divergence(P, Q):
    """
    Calculate KL Divergence between two probability distributions P and Q.
    Ensure that both P and Q are NumPy arrays and are normalized.
    """
    #Just to Ensure the distributions are normalized (sum to 1) to represent valid probability distributions
    P = np.array(P, dtype=np.float64)
    Q = np.array(Q, dtype=np.float64)

    #Here we just replace zeros in Q to avoid division by zero errors (KL Divergence is undefined if Q[i] == 0)
    Q = np.where(Q == 0, 1e-10, Q)

    #Now Calculate KL Divergence using the formula: sum(P[i] * log(P[i] / Q[i]))
    kl_div = np.sum(P * np.log(P / Q))
    return kl_div

def main():
    #We just consider example distributions
    P = np.array([0.4, 0.35, 0.2, 0.05])  #Expected distribution
    Q = np.array([0.5, 0.3, 0.15, 0.05])  #Observed distribution

    #ensure that both P and Q are valid probability distributions
    assert np.isclose(np.sum(P), 1.0), "P must sum to 1"
    assert np.isclose(np.sum(Q), 1.0), "Q must sum to 1"

    # Now we will calculate the KL Divergence
    kl_value = kl_divergence(P, Q)
    print(f"KL Divergence between P and Q: {kl_value:.4f}")

if __name__ == "__main__":
    main()
