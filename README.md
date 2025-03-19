# Python Practice Exercises – Shalev Gabay  

## Overview  
This repository contains a collection of Python exercises demonstrating fundamental programming principles and in-depth understanding of Python. The exercises cover a wide range of topics, including functional programming, data structures, recursion, algorithmic problem-solving, and object-oriented programming.  

## Table of Contents  
- [Features](#features)  
- [Exercises](#exercises)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Examples](#examples)  
- [Contributing](#contributing)  
- [License](#license)  

## Features  
✅ Implementations of core Python concepts  
✅ Functional programming and immutability principles  
✅ Recursive data structures and binary trees  
✅ Algorithmic operations on numbers, sets, and collections  
✅ Real-world inspired exercises such as parking management  

## Exercises  

### **1. Power Operations (`Targil 1`)**  
- Implements power calculations using tuples as immutable structures.  
- Supports operations like multiplication, division, and simplification of powers.  
- Demonstrates higher-order functions and functional programming concepts.  

### **2. Binary Tree (`Targil 2`)**  
- Implements a binary tree with functional access methods.  
- Supports searching, counting occurrences, and checking if the tree is balanced.  
- Demonstrates recursion and hierarchical data processing.  

### **3. Pricing System (`Targil 3`)**  
- Implements a pricing system with discounts based on store and product type.  
- Uses dictionary-based data handling and functional programming techniques.  

### **4. Accumulate Prices (`Targil 4`)**  
- Uses the `reduce()` function to calculate total prices across different stores.  
- Demonstrates lambda functions and higher-order functions in Python.  

### **5. Parking Management (`Targil 5`)**  
- Implements a parking lot system with priority levels (Regular, Priority, VIP).  
- Supports real-time updates and vehicle tracking.  
- Demonstrates dictionary-based state management and procedural logic.  

## Installation  
1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/python-exercises.git
   cd python-exercises
   ```
2. Ensure you have **Python 3.x** installed.  

## Usage  
Run any of the exercises using:  
```sh
python targil1.py  # Replace with the appropriate script name
```

## Examples  

### **Power Operations Example**  
```python
x = make_power(4, 5)
print_power(x)  # Output: 4 ^ 5
print_power(improve_power(x))  # Output: 2 ^ 10
```

### **Binary Tree Example**  
```python
tree = make_tree(12, make_tree(6, make_tree(8, None, None), None), make_tree(7, make_tree(8, None, None), make_tree(15, None, None)))
print_tree(tree)  # Outputs tree values in order
```

## Contributing  
If you have suggestions or improvements, feel free to open a pull request or submit an issue.  

## License  
This project is open-source and available under the **MIT License**.  

---

🔗 **GitHub Repository:** https://github.com/shalevg12/Python_API 
