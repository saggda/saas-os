# Sprint Status Tracker — Shopify Clone Takedown Operations

**Purpose:** Real-time tracking of takedown sprints, follow-ups, and client communications. Use this for both internal operations and client transparency.

**Use this for:** Daily sprint management, follow-up cadence, client updates, and SLA tracking.

---

## 1. Master Ticket Tracker (CSV Format)

**Copy this into Google Sheets/Excel/Notion database:**

```csv
incident_id,client_brand,target_domain,severity,created_utc,shopify_case_id,shopify_status,cdn_case_id,cdn_status,registrar_case_id,registrar_status,ads_meta_case_id,ads_meta_status,ads_google_case_id,ads_google_status,search_case_id,search_status,overall_status,next_action,next_followup_utc,owner,notes
INC-0001,Example Brand,example-shop.com,S1,2026-02-18T10:00Z,SP-12345,Pending,CF-67890,Pending,REG-54321,Open,META-11111,Submitted,GOOG-22222,Submitted,SEARCH-33333,Pending,In Progress,File registrar follow-up,2026-02-19T10:00Z,alice,"Taking payments, running IG ads"
INC-0002,Test Store,fake-example.net,S2,2026-02-17T15:30Z,SP-12346,Resolved,CF-67891,Resolved,REG-54322,Closed,,,GOOG-22223,Resolved,Resolved,Client update & closure,2026-02-18T18:00Z,bob,"Down in 36h"
```

### Column Definitions

| Column | Description | Values/Format |
|--------|-------------|---------------|
| incident_id | Unique identifier | INC-XXXX |
| client_brand | Client/Brand name | Text |
| target_domain | Suspicious domain | example.com |
| severity | Threat level | S1 (phishing), S2 (counterfeit), S3 (brand misuse) |
| created_utc | Incident created | ISO 8601 |
| *_case_id | Platform ticket ID | Platform-specific |
| *_status | Ticket status | Open/Pending/Escalated/Resolved/Closed |
| overall_status | Summary status | New/In Progress/Resolved/Closed |
| next_action | Next manual action | Text description |
| next_followup_utc | Next follow-up time | ISO 8601 |
| owner | Primary assignee | Name |
| notes | Context & flags | Free text |

### Status Definitions

**Ticket Status:**
- **Open** — Initial submission, no acknowledgement
- **Pending** — Acknowledged, under review
- **Escalated** — Moved to specialist/supervisor
- **Resolved** — Action taken, site down/content removed
- **Closed** — Case closed (with or without resolution)

**Overall Status:**
- **New** — Intake complete, initial filings pending
- **In Progress** — Active filings & follow-ups
- **Resolved** — Primary threat neutralized
- **Closed** — Documentation delivered, case complete

---

## 2. Follow-Up Cadence System

### T+6 Hours — First Follow-Up

**Trigger:** No acknowledgement from S1 cases

**Checklist:**
- [ ] Verify all submissions include complete evidence
- [ ] Add additional URLs if discovered
- [ ] Reply to case thread with urgency note
- [ ] Update tracker with follow-up notes

**Template:**
> Following up on case **[ID]**. Additional URLs discovered: [list]. This is an active phishing/fraud incident — please prioritize review. Evidence pack: [link].

**T+:** 6h after initial filing
**For:** S1 cases only

---

### T+24 Hours — Second Follow-Up

**Trigger:** All unresolved cases

**Checklist:**
- [ ] Expanded URL list (if applicable)
- [ ] Additional evidence (customer complaints, chargebacks)
- [ ] Escalation request (if no response)
- [ ] Client update with current status

**Template:**
> Follow-up on case **[ID]** regarding **[domain]**. 
>
> **New information:**
> - Additional URLs: [list]
> - Customer impact: [chargebacks/complaints]
> - Evidence pack: [updated link]
>
> Please prioritize. Harm is ongoing.

**T+:** 24h after initial filing
**For:** All open cases

---

### T+48 Hours — Escalation

**Trigger:** Still live after 48h

**Checklist:**
- [ ] Identify escalation path (supervisor, specialist, legal)
- [ ] Prepare escalation request with timeline
- [ ] Consider alternative actions (host, registrar, payment processor)
- [ ] Client consultation on next steps

**Escalation Template:**
> **Escalation Request — Case [ID]**
>
> **Timeline:**
> - Submitted: [date/time]
> - First follow-up: [date/time]
> - Second follow-up: [date/time]
> - Current: 48h+ with no resolution
>
> **Impact:** Active fraud/phishing — [harm details]
>
> **Request:** Please escalate to specialist/supervisor for immediate review.

**T+:** 48h after initial filing
**For:** All unresolved cases

---

## 3. Client-Facing Progress View

### Traffic Light System

- 🔴 **RED** — Active threat, no resolution yet
- 🟡 **YELLOW** — Some progress, partial resolution
- 🟢 **GREEN** — Threat neutralized, monitoring only

### Client Update Template (Initial)

> **Takedown Sprint — Status Update (2h)**
>
> **Brand:** [BRAND]
> **Incident ID:** INC-XXXX
> **Status:** 🔴 Active — Initial filings submitted
>
> **What's Been Done:**
> - ✅ Evidence Vault created: [link]
> - ✅ Shopify report filed: [ID]
> - ✅ CDN report filed: [ID]
> - ✅ Registrar report filed: [submitted/ID]
> - ✅ Ad platforms notified: [status]
>
> **What Happens Next:**
> - First acknowledgements: 2–24h
> - Initial takedowns: 24–72h
> - We follow up at 6h, 24h, 48h
>
> **Next Update:** [date/time]

---

### Client Update Template (24h)

> **Takedown Sprint — Status Update (24h)**
>
> **Brand:** [BRAND]
> **Incident ID:** INC-XXXX
> **Status:** [🔴/🟡/🟢]
>
> **Progress Since Last Update:**
> - [Platform]: [update] — [status]
> - [Platform]: [update] — [status]
> - [Platform]: [update] — [status]
>
> **Overall:** [summary sentence]
>
> **Next Steps:**
> - [action 1]
> - [action 2]
>
> **Next Update:** [date/time]

---

### Client Update Template (Closure)

> **Takedown Sprint — Closure Report**
>
> **Brand:** [BRAND]
> **Incident ID:** INC-XXXX
> **Status:** 🟢 Resolved
>
> **What Was Achieved:**
> - ✅ [Domain] — TAKEN DOWN
> - ✅ [Domain] — TAKEN DOWN
> - ✅ Ads removed from Meta/Google
> - ✅ Search results deindexed
>
> **Timeline:**
> - Started: [date/time]
> - Resolved: [date/time]
> - Total time: [X] hours
>
> **Documentation:**
> - Evidence Vault: [link]
> - Case IDs: [list]
> - Prevention Guide: [link]
>
> **Recommended Next Steps:**
> - [ ] Purchase domain variants
> - [ ] Set up brand monitoring
> - [�] Consider retainer for ongoing protection

---

## 4. Internal Ops View

### Severity Tiers & SLAs

| Severity | Description | Response SLA | Resolution Target | Follow-up Cadence |
|----------|-------------|--------------|-------------------|-------------------|
| **S1** | Active fraud/phishing (taking payments, data collection) | 1h | 24h | 6h, 24h, 48h |
| **S2** | Counterfeit/copycat (selling knockoffs) | 4h | 48h | 24h, 48h, 72h |
| **S3** | Brand misuse only (logo/name, no checkout) | 24h | 72h | 48h, 72h, 7d |

### Escalation Matrix

**When to escalate:**
- S1 case unresolved after 24h
- S2 case unresolved after 48h
- Any case with no acknowledgement after 48h
- Client requests escalation
- New domains appear (whack-a-mole pattern)

**Escalation paths:**
- Platform: Request supervisor/specialist review
- Client: Discuss legal escalation options
- Internal: Engage additional resources

---

## 5. Automation & Tools

### Calendar Reminders

**For each incident:**
- T+6h reminder: Check S1 cases
- T+24h reminder: Check all open cases
- T+48h reminder: Escalate unresolved

**Daily:**
- 09:00: Review all open cases
- 14:00: Check for acknowledgements
- 18:00: Send client updates

### Auto-Follow-Up Triggers

**Set up:**
- If [status] = "Open" AND [next_followup_utc] < NOW → Alert
- If [severity] = "S1" AND [last_update] > 6h ago → Alert
- If [overall_status] = "In Progress" AND [next_followup_utc] < NOW → Alert

### Status Update Templates

**Initial (2h):** See Client Update Template above
**24h Update:** See Client Update Template above
**48h Update:** Similar to 24h, add escalation notice if needed
**Closure:** See Closure Template above

---

## 6. Quick Reference

### Platform Abuse Links

**Shopify:** https://www.shopify.com/legal/tools/report-an-issue/dmca
**Cloudflare:** https://abuse.cloudflare.com/
**Google Safe Browsing:** https://safebrowsing.google.com/safebrowsing/report_phish/
**Meta (for internal notes):** Use ad library + reporting forms
**Google Ads:** Use policy feedback forms

### Response Time Expectations

**Best-case:**
- CDN (Cloudflare): 4–24h (phishing prioritized)
- Meta Ads: 12–48h
- Shopify: 24–72h

**Typical:**
- CDN: 24–48h
- Registrar: 48–72h
- Shopify: 48–96h
- Search removal: 72–96h

**Worst-case:**
- Any platform: 7–14 days (backlog, incomplete evidence, legal complexity)

### Common Blockers & Solutions

| Blocker | Solution |
|---------|----------|
| No acknowledgement | Re-submit with additional evidence, follow up in 24h |
| "Not our jurisdiction" | Escalate to correct platform/host/registrar |
| "Insufficient evidence" | Add side-by-side comparisons, customer complaints |
| "No violation found" | Re-review evidence threshold, consider legal counsel |
| Domain hopping | Expand monitoring, recommend domain variant purchase |
| Counter-notice | Consult legal counsel, respond within window |

---

## 7. Dashboard Metrics to Track

**Per Sprint:**
- Time to first acknowledgement
- Time to resolution (per platform)
- Total resolution time
- Follow-ups sent vs responses received
- Escalation rate

**Aggregate:**
- Sprints by severity tier
- Resolution rate (platform success)
- Average resolution time
- Client satisfaction (if tracked)
- Repeat incident rate (for retainer value)

---

## 8. Example Scenarios

### Scenario 1: Fast Resolution (24h)

**INC-0001** — S1 phishing site
- 09:00: Intake + evidence + filings
- 11:00: Cloudflare acknowledges
- 14:00: Site behind Cloudflare challenge page
- 09:00 (+1d): Site fully offline
- **Total:** 24h

**What worked:**
- Complete evidence pack
- Parallel filings (Shopify + Cloudflare)
- Phishing category (high priority)

---

### Scenario 2: Slow Resolution (7d)

**INC-0002** — S2 counterfeit store
- Day 0: Initial filings
- Day 2: Follow-ups (no response)
- Day 3: Escalation requested
- Day 5: Registrar responds (requesting more info)
- Day 6: Additional evidence submitted
- Day 7: Domain suspended
- **Total:** 7 days

**What slowed it down:**
- Non-urgent category (counterfeit vs phishing)
- Incomplete initial evidence
- Registrar response time
- Multiple back-and-forth requests

**Learnings:**
- Submit complete evidence upfront
- Mark as urgent if harm is ongoing
- Consider legal escalation earlier

---

**Last updated:** 2026-02-18
**Version:** 1.0

