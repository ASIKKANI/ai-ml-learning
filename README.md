# Machine Learning Learning Projects

## Overview

This repository contains a collection of **learning-focused machine learning projects** created while studying ML fundamentals.
Each project is implemented with the goal of understanding both **practical workflows** and **core mathematical concepts**, ranging from library-based models to from-scratch implementations.

These projects are for **educational purposes only**, not production or domain-specific diagnostic use.

---

## Project 1: Logistic Regression – Binary Classification
 
### Description

This project focuses on learning **Logistic Regression** using a standard machine learning workflow with Scikit-learn.
It demonstrates how a binary classification problem is handled end-to-end, including preprocessing, model training, and evaluation.

### Dataset

**Breast Cancer Wisconsin (Diagnostic) Dataset**

- Publicly available dataset for binary classification
- Target variable: `diagnosis`
  - `1` → Malignant
  - `0` → Benign

### Objectives

- Understand Logistic Regression in practice
- Apply standard preprocessing techniques
- Train and evaluate a binary classification model
- Interpret model outputs

### Workflow

1. Load and inspect the dataset  
2. Remove irrelevant columns  
3. Encode categorical labels  
4. Scale numerical features  
5. Split data into training and testing sets  
6. Train a Logistic Regression model  
7. Evaluate performance using accuracy  

### Model Used

- Logistic Regression (Scikit-learn)

### Notes

- Built as part of learning ML fundamentals
- No advanced hyperparameter tuning or cross-validation
- No medical or diagnostic claims are made

---

## Project 2: Multiple Linear Regression – From Scratch (NumPy)

### Description

This project implements **Multiple Linear Regression from scratch** using NumPy, without relying on machine learning libraries.
The goal is to understand the **mathematics behind regression**, including cost computation and gradient descent optimization.

### Objectives

- Implement linear regression manually
- Understand cost functions and gradients
- Apply gradient descent for parameter optimization
- Gain intuition about model convergence

### Key Concepts Implemented

- Linear hypothesis: `h(x) = X·w + b`
- Mean Squared Error (MSE) cost function
- Gradient computation for weights and bias
- Gradient descent optimization loop

### Implementation Details

- Weights and bias initialized manually
- Gradients computed using explicit loops for clarity
- Parameter updates performed using gradient descent

### Tools Used

- Python
- NumPy
- Matplotlib (for visualization, if used)

### Notes

- Focused on conceptual clarity over performance
- No vectorized or library-optimized shortcuts used
- Designed strictly as a learning exercise

---

## Future Projects

- Logistic Regression from scratch
- Regularized Linear Regression
- Gradient Descent visualization
- Model comparison (from-scratch vs Scikit-learn)

---

## Author

**P Asik Kani**
