# Ranked Niches — Wave 0900

Scoring model (0–5 each): **pain, WTP, frequency, distribution, feasibility (solo), advantage, retention, risk_inverse**.
Weighted scoring computed by `tools/score_ideas.py`.

> Decisions: BUILD_NOW (≥80) | VALIDATE_HARD (65–79.99) | HOLD (50–64.99) | KILL (<50)

## Ranking

1) **Shopify clone-store + lookalike domain takedown ops (SLA + monitoring)** — **80.0** — **BUILD_NOW**
- Why it wins: direct money loss + urgent + clear deliverable + easy to sell as a service first.
- Evidence: clone stores/lookalike domains thread; domain/DNS escalation patterns; adjacent monitoring tools.

2) **Microsoft 365 bulk-email guardrails (deliverability firewall + policy)** — **78.0** — **VALIDATE_HARD**
- Why it wins: boring but budgeted; MSP channel; clear ROI (deliverability).
- Caveat: needs careful implementation around M365 sending paths.

3) **Facebook Lead Ads bot-lead filter + auto-pausing + CRM quarantine** — **76.5** — **VALIDATE_HARD**
- Why it wins: high frequency + immediate ROI.
- Caveat: competitive space; must ship proof fast.

4) **AI agent/skill supply-chain scanner (signed manifest + secret exfil detection)** — **65.5** — **VALIDATE_HARD**
- Why it’s borderline: real pain + strong trend, but buyer maturity varies; sales cycles can stretch.

5) **Shopify POS pain: Square migration kit + cashflow/loyalty parity checklist** — **65.0** — **VALIDATE_HARD**
- Why it’s borderline: pain is real for brick-and-mortar, but distribution + retention are weaker unless paired with ongoing service.

---

## Score breakdown table

| Rank | Niche | pain | wtp | freq | dist | feas | adv | ret | risk_inv | total | decision |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Shopify clone-store + lookalike domain takedown ops (SLA + monitoring) | 5.0 | 4.5 | 3.0 | 4.0 | 4.0 | 3.5 | 3.0 | 3.0 | 80.0 | BUILD_NOW |
| 2 | Microsoft 365 bulk-email guardrails (deliverability firewall + policy) | 4.0 | 4.5 | 4.0 | 3.5 | 4.0 | 3.0 | 4.0 | 3.5 | 78.0 | VALIDATE_HARD |
| 3 | Facebook Lead Ads bot-lead filter + auto-pausing + CRM quarantine | 4.5 | 4.0 | 4.5 | 4.0 | 3.0 | 2.5 | 3.5 | 2.5 | 76.5 | VALIDATE_HARD |
| 4 | AI agent/skill supply-chain scanner (signed manifest + secret exfil detection) | 4.0 | 3.5 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | 2.5 | 65.5 | VALIDATE_HARD |
| 5 | Shopify POS pain: Square migration kit + cashflow/loyalty parity checklist | 4.0 | 3.5 | 2.0 | 3.0 | 4.0 | 3.0 | 2.5 | 3.5 | 65.0 | VALIDATE_HARD |


## Artifacts
- Moltbook extracted lines: `../raw/moltbook-0900.md`
- Wave notes + evidence: `../notes/run-0900.md`

