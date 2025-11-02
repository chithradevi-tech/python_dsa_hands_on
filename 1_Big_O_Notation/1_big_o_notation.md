**Big O Notation**

Big O Notation is a mathematical concept used in Data Structures and Algorithms (DSA) to describe the efficiency of an algorithm, especially its time and space complexity. It tells you how the performance of an algorithm changes with the size of the input.

---

🔹 **Why is Big O Notation Important?**

    It helps compare algorithms.

    It gives a high-level understanding of the worst-case (or sometimes best/average-case) performance.

    It allows you to estimate how your code will scale.

---

🔹 **Common Big O Complexities**

| Big O      | Name             | Description                                                                   |
| ---------- | ---------------- | ----------------------------------------------------------------------------- |
| O(1)       | Constant Time    | Execution time doesn't depend on input size.                                  |
| O(log n)   | Logarithmic Time | Divide-and-conquer algorithms like Binary Search.                             |
| O(n)       | Linear Time      | Loops through all elements once.                                              |
| O(n log n) | Linearithmic     | Efficient sorting algorithms like Merge Sort, Heap Sort.                      |
| O(n²)      | Quadratic Time   | Nested loops over the input — e.g., Bubble Sort.                              |
| O(2ⁿ)      | Exponential Time | Algorithms that double with each input increase — e.g., recursive Fibonacci.  |
| O(n!)      | Factorial Time   | Algorithms that try every permutation — e.g., brute-force Traveling Salesman. |

---

🔹 **Time Complexity Examples**

| Algorithm               | Time Complexity          |
| ----------------------- | ------------------------ |
| Binary Search           | O(log n)                 |
| Linear Search           | O(n)                     |
| Bubble Sort             | O(n²)                    |
| Merge Sort              | O(n log n)               |
| Insertion in Hash Table | O(1) average, O(n) worst |
| DFS/BFS (Graph)         | O(V + E)                 |

---

🔹 **Visual Analogy (Growth Rate)**

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

---

🔸 **O(1) – Constant Time**

Example: Using a dictionary to find the meaning of a word (assuming you know the page number).

No matter how many words are in the dictionary, looking up a word by page number takes the same time.
```text
def add_items(n):

    return n + n + n

print add_items(10)
```
---

🔸 **O(log n) – Logarithmic Time**

Example: Finding a name in a phone book by dividing pages in half each time.

You open the book in the middle. If the name is before it, you search the left half. If after, the right half. Each step cuts the number of pages in half.

This is like Binary Search.

---

🔸 **O(n) – Linear Time**

Example: Checking everyone’s name in a queue to find a specific person.

You might have to go through each person one by one until you find the one you're looking for.

ex:
```text
def print_items(n):

    for i in range(n):

    print(i)

print_items(10)
```
ex:
```text
def print_items(n):

    for i in range(n):

    print(i)

    for j in range(n):

        print(j)

print_items(10)
```
---

🔸 **O(n log n) – Linearithmic Time**

Example: Sorting a list of names using an efficient strategy like divide and conquer.

You split the list into smaller parts (log n splits), sort each (n work), and merge them.

Similar to how companies sort employee records.

---

🔸 **O(n²) – Quadratic Time**

Example: Comparing every student with every other student in a class for a group activity.

If there are 10 students, you make around 100 comparisons.

Like Bubble Sort, where each item is compared with every other item.

ex:
```text
def print_items(n):

    for i in range(n):

        for j in range(n):

            print(i,j)

print_items(10)
```
ex:
```text
def print_items(n):

    for i in range(n):

        for j in range(n):

        print(i,j)

    for k in range(n):

        print(k)

print_items(10)
```
---

🔸 **O(2ⁿ) – Exponential Time**

Example: Trying every combination on a locked suitcase with n digits.

For each digit, you have 2 choices (e.g., locked/unlocked or 0/1). Total combinations = 2ⁿ.

Similar to solving a puzzle where you try all possible paths.

---

🔸 **O(n!) – Factorial Time**

Example: Planning every possible order to visit n cities.

If there are 5 cities, there are 120 possible routes (5! = 120).

This is like the Traveling Salesman Problem — very slow to solve as n increases.

---

![Image](https://github.com/user-attachments/assets/81f3750a-c0e3-4e15-864f-9534b7104209)
