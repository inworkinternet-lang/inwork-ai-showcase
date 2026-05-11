# 📊 Proof of Usage: InWork-Ai Infrastructure & AI Expenses

This document summarizes the current operational investments of **InWork-Ai**, demonstrating our commitment to scaling a professional, multi-agent SaaS ecosystem. These expenses justify our application for the **MiMo Orbit Max Plan** as we transition from MVP to a full-scale industrial production.

## 🏛️ AI & Cognitive Layer Investment
We utilize a multi-model strategy, investing heavily in SOTA LLMs and agentic frameworks.
*   **Z.ai (Zhipu AI / BigModel):** Our primary "Reasoning Brain". We currently use **GLM-4-Plus** for complex business logic and CRM synchronization. Active payment history since February 2026.
*   **OpenAI API:** Consistent usage for baseline reasoning and prototyping.
*   **Hanabi.ai (Plus):** Monthly subscription for advanced model access.

## ⚙️ Production Billing Engine
InWork-Ai features a production-ready billing system (see `titan-spine/app/billing.py`) that handles per-minute and per-token billing with enterprise precision:
*   **Smart Minute Calculation:** Uses `math.ceil` for 60-second intervals to ensure accurate carrier cost recovery.
*   **Multi-Tenant Accounting:** Tracks `minutes_used` and `wallet_balance` per tenant with automatic tariff validation.
*   **Scalability:** Designed to handle thousands of concurrent voice sessions with real-time balance updates.

## 🎙️ Voice AI & Interaction Layer
*   **Vapi.ai:** High-frequency usage for real-time voice orchestration.
*   **Fish Audio:** Premium TTS investment for human-like voice synthesis (250k+ credits).
*   **Zadarma / Twilio:** Dedicated international number procurement (Swiss/EU) for B2B voice routing.

## 🌐 Infrastructure & Global Presence
*   **Titan VPS (Amsterdam Hub):** Dedicated high-performance hosting for the Titan Spine (Backend).
*   **Proxy Gold:** Industrial-scale IPv6 proxy packs for data harvesting and scraping.
*   **Enterprise Domains:** Ownership of `inwork-ai.pro` (B2B Platform) and `inwork-ai.com` (Global Brand).

## 📈 Summary of Recent Operations (Q1 2026)
| Category | Status | Role in InWork-Ai |
| :--- | :--- | :--- |
| **Model Usage** | Active | Reasoning, JSON Extraction, Coding |
| **Voice Interaction** | Active | Customer Service, Lead Generation |
| **Data Infrastructure** | Active | Global Connectivity, RLS-Security |
| **Market Expansion** | Scaling | Swiss/EU B2B Onboarding |

---
## 🚀 Why We Need MiMo Orbit
With our current burn rate across multiple AI providers, the **1,000,000 token context window** and the **1.6B credit grant** from Xiaomi will allow us to consolidate our "Infinite Memory" layer, significantly reducing operational friction while enabling the processing of massive enterprise knowledge bases that are currently cost-prohibitive.

#barBOSS
