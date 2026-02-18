# Ranked candidates — wave 1300

Scoring: 1–5 (higher is better). Notes are biased toward **first revenue in 14–30 days** for a solo builder.

Dimensions:
- Pain
- WTP (willingness to pay)
- Frequency
- Distribution (repeatable lead source)
- Feasibility (solo execution drag)
- Advantage (unfair edge / differentiation)
- Retention (stickiness)
- Risk (regulatory/ops/competition; 5 = low risk)

---

## 1) Agent skill/plugin supply-chain security gate (signing + SBOM + scanner + policy)
**Thesis:** ecosystems are shipping executable “skills/plugins” with weak verification; one credible breach drives budgets fast.

Evidence anchors:
- Moltbook supply-chain/credential-stealer signal + “signed skills or bust” theme (molt:cbd6… + molt:b9ad…)
- NIST/C AISI RFI re: securing AI agent systems: https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems
- ProductHunt: agent observability product exists (buyers exist): https://www.producthunt.com/products/clawmetry

**MVP offer:**
- GitHub Action / CI gate: verify signatures, generate SBOM, scan for secret access + suspicious network exfil patterns, produce audit PDF.
- Hosted dashboard optional; start as CLI + reports.

| Pain | WTP | Freq | Dist | Feas | Adv | Ret | Risk | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | 4 | 3 | 4 | 4 | 4 | 3 | **32/40** |

Why it wins: direct security budget + clear buyer + crisp first deliverable (gate + report).

---

## 2) Shopify chargeback dispute automation (evidence pack builder + tracking)
**Thesis:** chargebacks are a direct cash leak; merchants will pay quickly for recovered revenue + time savings.

Evidence anchors:
- Shopify pain post: https://www.reddit.com/r/shopify/comments/1r7x8oa/why_does_it_feel_impossible_to_fight_chargebacks/

**MVP offer:**
- “Dispute Pack” generator: pulls order timeline, tracking, comms, ToS checkbox proof, refund policy, customer history → issuer-ready PDF + templated response.
- Price: per dispute pack or % of wins.

| Pain | WTP | Freq | Dist | Feas | Adv | Ret | Risk | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | 4 | 4 | 3 | 3 | 4 | 3 | **31/40** |

Main risk: competitive market + integration complexity; but first-money path is very strong.

---

## 3) Agent audit logs / “judgment receipts” compliance kit
**Thesis:** as agents touch real systems, teams will need auditability (tool calls, data lineage, redaction) for internal compliance.

Evidence anchors:
- Moltbook “audit trail/judgment receipts”: molt:0252…
- NIST/C AISI agent security RFI: https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems

| Pain | WTP | Freq | Dist | Feas | Adv | Ret | Risk | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 4 | 4 | 2 | 3 | 3 | 5 | 3 | **28/40** |

Main issue: longer sales cycles unless you target small teams with an “audit export” immediate need.

---

## 4) Log-investigation assistant for sysadmins (incident “case file” generator)
**Thesis:** sysadmins burn hours correlating logs; a tool that creates a shareable timeline + evidence bundle saves time.

Evidence anchors:
- Log spelunking pain: https://www.reddit.com/r/sysadmin/comments/1r7lq7t/i_will_happily_spend_hours_combing_through_logs/

| Pain | WTP | Freq | Dist | Feas | Adv | Ret | Risk | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 3 | 4 | 3 | 3 | 2 | 4 | 4 | **27/40** |

Main issue: many teams already have SIEM/observability; need a very sharp wedge ("case file" export + receipts) to avoid commodity trap.

---

# Verdict (this wave)
Top 2:
1) **Agent skill supply-chain security gate** — best budget alignment + regulatory tailwind. Confidence: **High**.
2) **Shopify chargeback dispute packs** — fastest first-money, but more competition/integration risk. Confidence: **Medium-High**.
