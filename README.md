# 🥗 Hyper-local Market Intelligence: Cloud Kitchen Expansion Strategy

![Status](https://img.shields.io/badge/Status-Completed-success)
![Tech](https://img.shields.io/badge/Tech-Python%20%7C%20Pandas%20%7C%20Seaborn-blue)
![Domain](https://img.shields.io/badge/Domain-Strategy%20%26%20Retail-purple)

## 📌 Project Overview
Opening a restaurant in Bangalore is high-risk. This project uses data to solve the classic "Location vs. Product" problem for a new Cloud Kitchen venture.
By analyzing supply (restaurant density) vs. demand (vote volume) and mining sentiment trends, I identified the optimal **Location** and **Cuisine Niche** for maximum ROI.

---

## 📸 The Investment Pitch

### 1. Location Strategy: Finding the "White Space"
I plotted a Strategic Matrix to identify underserved markets.

<img width="1920" height="1020" alt="Screenshot 2026-02-05 174018" src="https://github.com/user-attachments/assets/7047a687-81b1-4358-9bb6-3cf35fafdd75" />
*(Figure 1: The Matrix identifies **HSR Layout** (Green Bubble) as the primary Opportunity Zone—characterized by high consumer demand but moderate competition compared to saturated hubs like Koramangala.)*

### 2. Product Strategy: The "Cuisine Gap"
Once the location was selected, I analyzed the specific supply-demand mismatch in that area.

<img width="1920" height="1020" alt="Screenshot 2026-02-05 174031" src="https://github.com/user-attachments/assets/35e00d5b-fd50-4e9e-a480-b3478bf43496" />
*(Figure 2: Analysis of HSR Layout reveals a massive gap in the **"Healthy/Salad"** category (High Search Interest vs. Low Supply), while North Indian and Chinese segments are oversaturated.)*

---

## 🧠 Final Recommendation
**TO:** Investors / Operations Head
**RECOMMENDATION:** Launch a **"Healthy Bowl/Salad"** Cloud Kitchen in **HSR Layout**.

* **Why HSR Layout?** It has the highest *Demand-to-Supply Ratio* (Saturation Index: 1.8) compared to Koramangala (Saturation Index: 0.6).
* **Why Healthy Food?** Search volume for "Healthy" keywords is 4x higher than the current supply of rated healthy outlets in this specific zone.

---

## 🛠️ Tech Stack & Methodology
* **Python (Pandas):** Data aggregation and saturation indexing.
* **Seaborn:** Advanced strategic visualization (Bubble Charts).
* **Gap Analysis:** Comparing `Supply %` vs. `Search Interest Index` to quantify market voids.

## 🚀 How to Run
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Market-Intelligence-Strategy.git](https://github.com/YOUR_USERNAME/Market-Intelligence-Strategy.git)
    ```
2.  **Install Requirements:**
    ```bash
    pip install pandas matplotlib seaborn
    ```
3.  **Generate Data:**
    ```bash
    python generate_market_data.py
    ```
4.  **Run Strategy Analysis:**
    ```bash
    python market_strategy.py
    ```
