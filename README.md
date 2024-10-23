KL Divergence Example
This project provides a simple demonstration of calculating Kullback-Leibler (KL) Divergence between two probability distributions. KL Divergence is a measure of how one probability distribution diverges from a second, expected probability distribution. This concept is useful in understanding information loss when approximating or substituting one distribution with another.

/kl_divergence_example
│
├── main.py
└── README.md

Usage
The main.py script defines two sample probability distributions (P and Q) and calculates the KL Divergence between them.

Prerequisites
Python 3.x
NumPy library
Installation
To install the necessary dependencies, run:
pip install numpy

To execute the script, navigate to the kl_divergence_example directory and run:
python main.py

KL Divergence could be between P and Q: 0.0589

P: Represents the "expected" distribution.
Q: Represents the "actual" observed distribution.
The script computes the divergence of Q from P. A lower value of KL Divergence indicates that the distributions are more similar.