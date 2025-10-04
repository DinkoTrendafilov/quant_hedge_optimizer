# 🎯 Dynamic Hedge Engine for Sports Betting

## Overview
This project demonstrates a **dynamic risk management system** designed for **sports betting companies** and **trading teams**.  
It automatically identifies the most exposed betting outcome and calculates the **optimal hedge amount** to balance overall exposure and minimize potential loss.

Built with Python, it simulates real betting scenarios using basic 1X2 markets (Home / Draw / Away), providing a clear view of:
- total exposure,
- payout structure,
- dynamic hedge suggestions,
- and final balance across outcomes.

---

## ⚙️ Features
- Calculates **total exposure** and **potential payout** for each outcome  
- Detects the **most risky** outcome dynamically  
- Suggests **optimal hedge amount** based on risk-to-odds ratio  
- Supports **manual or automatic hedging** decision  
- Provides a **scenario simulation** after hedging  
- Clean CLI interface for testing and demonstration  

---

## 🧮 Example Input
🎰 RISK MANAGEMENT SYSTEM WITH DYNAMIC HEDGE
Enter odds (1 X 2): 2.15 3.40 3.50
Enter stakes (1 X 2): 100 80 60

---

## 📊 Example Output
📊 RISK ANALYSIS:
1 (@2.15): +50lv risk ⚠️
X (@3.40): -30lv risk ✅
2 (@3.50): -60lv risk ✅

🔍 HIGHEST RISK: 1 - 50lv
🛡️ RECOMMENDED HEDGE: 31lv @2.04

---

## 🧠 Use Case
This project is useful for:
- **Risk Management Analysts**
- **Betting Traders**
- **Quantitative Analysts** in betting firms
- Anyone learning **hedging logic and exposure balancing**

---

## 🚀 Future Improvements
- Add support for **live odds updates**
- Integrate **expected value (EV)** and **probability weighting**
- Allow **portfolio exposure** across multiple events
- Export results to **CSV / JSON** for further analysis

---

## 👤 Author
Developed by **DinkoTrendafilov**, a data analyst learning risk modeling and quantitative methods in sports betting.  
Goal: to bridge **data analytics** and **risk management automation** in real-world betting environments.
