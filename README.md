Bacterial Foraging Optimization Algorithm (BFOA) for Multiple Sequence Alignment
This project implements an improved version of the Bacterial Foraging Optimization Algorithm (BFOA) for solving the problem of Multiple Sequence Alignment (MSA) in bioinformatics. The BFOA is inspired by the foraging behavior of E. coli bacteria and is optimized to find better alignments of genetic sequences by using strategies like chemotaxis, reproduction, and elimination-dispersal.

Overview
The algorithm is designed to handle the computational complexity of aligning multiple genetic sequences by optimizing their alignment scores using a BLOSUM matrix for scoring. The improved version introduces adaptive parameters, elitism, and other enhancements to increase the algorithm's performance and convergence rate.

Features
Multiple Sequence Alignment (MSA) using BFOA
BLOSUM scoring for evaluating the quality of alignments
Adaptive chemotaxis parameters to balance exploration and exploitation
Elitism to preserve high-quality solutions across generations
Mechanisms for mutation and diversity to escape local optima
Performance comparison between the original and improved versions

Directory Structure
.
├── bacteria.py            # Implementation of the Bacteria class
├── chemiotaxis.py         # Implementation of the Chemotaxis class
├── evaluadorBlosum.py     # BLOSUM matrix evaluator
├── fastaReader.py         # FASTA file reader
├── main.py                # Main script to run the algorithm
├── README.md              # This README file

Installation
To run this project, you need to have Python installed along with the following dependencies:

numpy
matplotlib
You can install the dependencies using pip:
pip install numpy matplotlib

Original BFOA
The original BFOA code is based on the implementation from riosew/BFOA on GitHub. The original algorithm uses a combination of chemotaxis, reproduction, and elimination-dispersal to optimize the alignment of genetic sequences. However, it may suffer from premature convergence and inefficiency in exploring the solution space.

Improved BFOA
The improved version includes:

Adaptive Parameters: Dynamically adjusting attraction and repulsion parameters based on population performance.
Elitism: Preserving a subset of the best solutions across generations.
Diversity Mechanisms: Introducing random mutations to maintain genetic diversity and avoid local optima.
Output
The algorithm outputs the best alignment found along with performance metrics like the alignment score (fitness) and the number of function evaluations (NFE).


Example Results
Below is a sample output from the improved BFOA:

Iteration: 1, Best Fitness: 3922.0, NFE: 20
Iteration: 2, Best Fitness: 3978.0, NFE: 31
...
Iteration: 30, Best Fitness: 4195.5, NFE: 339

Best Alignment Found:
[Aligned sequences printed here]

Performance Comparison
The project includes a script to generate comparative graphs between the original and improved algorithms, illustrating the improvements in fitness scores and efficiency.

Acknowledgments
Original BFOA implementation: riosew/BFOA on GitHub
Inspired by the natural foraging behavior of E. coli bacteria.
Special thanks to the bioinformatics community for providing foundational research in MSA and evolutionary algorithms.
