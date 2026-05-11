# 🏢 Technical Showcase: The "Two Towers" Architecture

## 📡 System Design Philosophy
InWork-Ai is built on the principle of **Functional Decoupling**. We separate real-time interaction (Interaction Layer) from heavy data processing (Analytical Layer).

### ⚡ Interaction Layer (Cerebras/Groq)
*   **Focus:** Speed.
*   **Task:** Human-like dialogue during live calls (<100ms latency).

### 🧠 Analytical Brain (GLM-4 / GLM-5.1)
*   **Focus:** Reasoning and Precision.
*   **Task:** This layer, powered by **GLM**, kicks in immediately after a session ends. It analyzes the full transcript, extracts business-critical JSON, and synchronizes with Google Calendar, Sheets, and Notion Ledgers.

---

## 🏆 The GLM Integration Advantage
By utilizing **GLM** as our "Snabzhenets" (Supply/Analytical) engine, we have achieved:
1.  **Reliable JSON Extraction:** Zero-failure rate in mapping voice intent to our database schema.
2.  **Autonomous Code Generation:** Using GLM-4 to scaffold new niche-specific agent behaviors (e.g., specialized booking logic for dental vs. auto-repair).
3.  **Cross-Platform Consistency:** Maintaining a unified logic across our "Two Towers" domains.

---

## 📊 Data Layer: Flat Columns Strategy (SSOT)
Our **Flat Columns Strategy** maps 60+ business-critical parameters to physical database columns. This is verified and maintained by our GLM-based agents, ensuring that our "Single Source of Truth" is never compromised.

---

## 🔮 Why 1M Tokens?
While **GLM** provides the "Reasoning", **MiMo-V2.5** provides the "Context". 
*   **Synergy:** We will use GLM to process the insights extracted from MiMo's 1,000,000-token window. 
*   **Impact:** This allows us to load an entire business's history, brand guidelines, and pricing into a single context, creating the most context-aware B2B agent in existence.

---
*Architected for Intelligence. Powered by GLM. Scaling with MiMo.*
