# 🏗️ InWork-Ai Showcase

> **Architecting the Future of Autonomous B2B Automation.**

This repository is a technical showcase of the **InWork-Ai** ecosystem—a high-performance, multi-agent SaaS platform designed for professional business automation. It demonstrates our core architectural principles, focusing on ultra-low latency interaction and secure, large-scale data analysis.

---

## 🏛️ Architecture: The "Two Towers" Strategy

InWork-Ai is built on the principle of **Functional Decoupling**, separating real-time human interaction from heavy cognitive processing.

### 1. 📡 The Interaction Tower (Operational Layer)
*   **Focus:** Human-like dialogue with <500ms response time.
*   **Stack:** Vapi (Voice Gateway), Cerebras/Groq (Llama 3.1 Inference).
*   **Task:** Executing immediate "spinal reflex" tasks (e.g., checking calendar slots, booking appointments) during live voice sessions.

### 2. 🧠 The Analytical Tower (Cognitive Layer)
*   **Focus:** Deep reasoning, structured data extraction, and business logic validation.
*   **Stack:** GLM-4 / GLM-5.1 (Analytical Brain), MiMo-V2.5 (Infinite Context).
*   **Task:** Post-session auditing, CRM synchronization, and generating dynamic "Smart-Links" for customer retention.

---

## 🛡️ Technical Pillar: Row-Level Security (RLS)

Security is not an afterthought; it is integrated into the database core. We utilize **SQLAlchemy 2.0 Global Criteria** to implement a robust RLS protocol.

*   **Zero-Crutch Security:** Every database query is automatically filtered by `tenant_id` at the session level.
*   **Data Isolation:** Multi-tenant data remains strictly segregated, preventing cross-tenant leaks on a system-wide scale.
*   **Architecture:**
    ```python
    # Example of our RLS implementation logic
    @event.listens_for(session, "do_orm_execute")
    def _rls_filter(orm_execute_state):
        if orm_execute_state.is_select:
            orm_execute_state.statement = orm_execute_state.statement.options(
                with_loader_criteria(Call, Call.tenant_id == active_tenant_id),
            )
    ```

---

## 🔮 The MiMo Advantage: 1,000,000 Token Context

While traditional models struggle with fragmented data, InWork-Ai utilizes the **1M Context Window** to build a **"Global Business Brain"**.

*   **Holistic Context:** We ingest entire business knowledge bases, months of interaction history, and complex pricing structures in a single pass.
*   **Proactive Intelligence:** Our agents don't just react; they cross-reference thousands of previous data points to provide highly personalized business outcomes.
*   **Deep Context Audits:** Analyzing long-form transcripts to ensure 100% compliance with Swiss IP and B2B quality standards.

---

## 🛠️ Technology Stack
*   **Backend:** FastAPI (titan-spine), SQLAlchemy 2.0 (ORM), PostgreSQL.
*   **Frontend:** Next.js (titan-facade), Tailwind CSS.
*   **Agents:** Multi-model orchestration (Claude / Gemini / GLM / MiMo).
*   **Infrastructure:** Titan VPS (Amsterdam), SIP/WebRTC Voice Gateways.

---

## 📝 About the Showcase
This repository contains "sterile" versions of our core components. Sensitive business logic, credentials, and proprietary IP have been removed to comply with our security protocols while demonstrating the underlying engineering maturity.

---
**#barBOSS**
