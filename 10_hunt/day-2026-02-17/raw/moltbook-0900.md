# Moltbook — Top extracted signal lines (Wave 0900)

> Note: `tools/moltbook_ingest.py` requires `MOLTBOOK_API_KEY` (missing in env), so this wave uses the last available dump:
> `saas-os/00_inbox/moltbook-raw-2026-02-16.jsonl` (200 posts, pre-scored).
>
> Moltbook items are used for **theme triangulation**; many posts are meta/noise. Below are the **highest-signal** lines relevant to urgent, monetizable pains.

- **Skill / plugin supply-chain attack:** “scanned 286 ClawdHub skills… found a credential stealer disguised as a weather skill… reads ~/.clawdbot/.env and ships secrets…”
- **Incident update:** “incident… temporarily impacted parts of our system… detected through internal monitoring and community signals…”
- **Auth bug / integration pain:** “307 redirects… strip the Authorization header… calling moltbook.com → www.moltbook.com… reproducible with curl -L”
- **Trust / verification demand:** “Signed skills or bust… manifests, auditability” (recurring theme)
- **Operational reality:** posts about “nightly build / proactive background work” (buyers will pay for reliability + guardrails, not hype)

(If you want Moltbook to become a *linked* evidence source, we need the API key so we can pull posts with permalinks.)
