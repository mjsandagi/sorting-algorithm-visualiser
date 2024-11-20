# Sorting Algorithm Visualiser

This is a sorting algorithm visualiser built using python, using the PyGame library in particular.

## Features

-   Visualise multiple sorting algorithms
    -   Bubble Sort
    -   Insertion Sort
    -   Merge Sort
    -   Quick Sort
    -   Bogo Sort (yes... really)
-   Adjustable speed for visualisation (line `191`)
-   User-friendly interface

## Requirements

-   PyGame (install via `pip install pygame`)

## Installation

1. Clone the repository:
    ```powershell
    git clone https://github.com/mjsandagi/sorting-algorithm-visualiser.git
    ```
2. Navigate to the project directory:
    ```powershell
    cd sorting-algorithm-visualiser
    ```
3. Run the file `main.py`:
    ```powershell
    python main.py
    ```

## Algorithms

### Bubble Sort

Bubble Sort simply repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

### Insertion Sort

Insertion Sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as the quicksort or merge sort.

### Merge Sort

Merge Sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. Most implementations produce a stable sort, meaning that the implementation preserves the input order of equal elements in the sorted output.

### Quick Sort

Quick Sort is an efficient, in-place, comparison-based, divide and conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

### Bogo Sort

Bogo Sort is a highly ineffective sorting algorithm based on the generate and test paradigm. The algorithm successively generates permutations of its input until it finds one that is sorted. (Basically, it creates random permutations until it gets the correct one).
