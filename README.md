**🧩 what is Algorithms?**

Algorithms - well-defined sequence of steps that take one or more values as inputs and produce one or more values as outputs.

Algorithms are step‑by‑step procedures for solving problems: sorting, searching, traversals, graph paths, dynamic programming, greedy methods, backtracking.

![Image](https://github.com/user-attachments/assets/2ebca19e-118a-4a6e-b816-824f375e6f06)

---

**Algorithms are everywhere :**

- search engines
- GPS systems
- sorting and filtering
- computational geometry

---

**🔍 what makes a good algorithm?**

- it's finite
- correct result every time
- it's efficient

---

**⚙️ Problem solving approach :**

- understand the problem
- gather all the information you have
- write some code, test, refactor

---

**🔁Types of Algorithms**

1. **Brute‑Force (Exhaustive Search)**

   - What it does: Tries every possible option until it finds a solution.
   - Pros: Always finds the answer if one exists.
   - Cons: Very slow for large inputs (often exponential complexity).
   - Example: Trying every possible password or checking all subsets of items

   ![Image](https://github.com/user-attachments/assets/18ca0246-ab6d-43b9-96c4-dca154b554b6)

   ---

2. **Greedy Algorithms** - **Greedy = Smart decision-making at each step**

   - What it does: Makes the best choice at each step based on what seems best right now.
   - Pros: Fast and simple.
   - Cons: Doesn't guarantee the best overall result in all problems.
   - Example: Picking the shortest available interval in interval scheduling, Huffman coding, MST (Kruskal/Prim), Dijkstra’s shortest

   <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/bf69fa4a-b030-4951-b465-4605b2718c36" />


   <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/bafd9da9-dcc3-463a-8089-fd828406c2de" />


   <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/0dd1db4b-b8ef-42f9-9350-27a27b3f7ef4" />


   <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/efabf498-126d-42f8-8f97-01022a977eba" />

   ---

3. **Divide & Conquer**

   - What it does: Splits a problem into smaller pieces, solves each one, then merges the results.
   - Pros: Efficient and works well for big data sets.
   - Cons: Can require recursion and careful implementation.
   - Example: Merge Sort, Quick Sort, binary search

   <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/ddcc6f28-ebd4-481f-b155-da7479586441" />

4. **Dynamic Programming (DP)**

   - What it does: Breaks a problem into subproblems and stores their results to avoid repeating work.
   - Pros: Very efficient for overlapping subproblems and optimization tasks.
   - Cons: Requires extra memory and careful planning.
   - Example: Fibonacci with memoization, Knapsack, Longest Common Subsequence

   <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/ec67ba76-73e9-4b5a-9e19-68034c42b19b" />

5. **Backtracking**

   - What it does: Tries building a solution step by step, and backs up when a choice leads nowhere.
   - Pros: Finds all possible valid solutions for constraint-based problems.
   - Cons: Can be slow unless you prune bad branches early.
   - Example: Solving Sudoku, N‑Queens, valid parentheses generation

   <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/dd52676c-5fcf-43ed-b105-550900330294" />

6. Randomized Algorithms

   - What it does: Uses random choices during execution to potentially make tasks faster.
   - Pros: Good average-case performance and simplicity.
   - Cons: Results can vary, and it may fail in the worst case.
   - Example: Randomized QuickSort, Monte Carlo simulations, Rabin‑Karp string search

7. Recursive Algorithms

   - What it does: A function calls itself with smaller inputs until a base case is reached.
   - Pros: Clean and expressive for tree-like or mathematical problems.
   - Cons: Can lead to deep recursion and stack overflow if not careful.
   - Example: Factorial, Fibonacci (naive version)

8. Search & Sorting Algorithms

   - Purpose: Basic tools to retrieve or order data quickly.
   - Examples:

     Searching: Linear search, Binary search (for sorted lists)

     Sorting: Bubble sort (simple), Merge sort, Quick sort, Heap sort, Timsort (used in Python)

---

**🧠 What are Data Structures and Algorithms?**

Data Structures are ways to organize and store data: e.g. arrays (lists), linked lists, stacks, queues, hash tables (dict/set), trees, heaps, graphs.

---
