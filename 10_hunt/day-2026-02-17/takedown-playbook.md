# Shopify Clone-Store / Lookalike-Domain Takedown — Operations Playbook (SOP + Templates)

**Use-case:** Impersonation, counterfeit goods, brand/logo misuse, copied creatives, phishing / carding via a Shopify storefront or a lookalike domain.

**Operating principles**
- **Speed + precision beats volume.** Abuse teams respond fastest to complete, structured reports.
- **Report “up the stack” and “down the stack” in parallel:** platform (Shopify), infrastructure (host/CDN), and discovery/traffic sources (Google/Meta).
- **Minimal viable proof first**, then add depth. Don’t wait for perfect.
- **Keep it clean + legal:** No doxxing, no harassment, no threats; stick to policy + rights + evidence.

**Key public reporting endpoints (bookmark these)**
- **Shopify legal tools (DMCA)** (requires Shopify login): https://www.shopify.com/legal/tools/report-an-issue/dmca
  - web_fetch shows Shopify routes DMCA reporting into a logged-in flow.
- **Cloudflare abuse reporting hub** (primary path is the form): https://www.cloudflare.com/trust-hub/reporting-abuse/ → https://abuse.cloudflare.com/
  - Cloudflare notes they generally **cannot process email complaints** and prefers the form.
  - They list categories including **Trademark Infringement** and **Phishing & Malware** and publish **DMCA-required elements** for copyright notices (signature, identify work, identify infringing URLs, contact info, good-faith statement, accuracy/perjury statement). Source: Cloudflare page above.
- **Google Safe Browsing phishing report:** https://safebrowsing.google.com/safebrowsing/report_phish/

---

## 1) Step-by-step SOP (first 2 hours / 24 hours / 72 hours)

### Roles (one person can wear multiple hats)
- **Incident Lead:** prioritization, comms, client updates.
- **Evidence Lead:** captures/organizes evidence vault.
- **Takedown Lead:** files reports + tracks follow-ups.
- **Customer/Brand Comms:** on-site banner, social post, CS macros.

### Severity tiers (choose one within 10 minutes)
- **S1 – Active fraud/phishing:** taking payments, collecting card data, running ads, or impersonating support.
- **S2 – Counterfeit/copycat store:** selling knockoffs, copied creatives, SEO pages.
- **S3 – Brand misuse only:** logo/name on landing page; no checkout.

### First 2 hours (0:00–2:00) — “Stop the bleeding + lock evidence + open lanes”

**0:00–0:10 — Triage + scope**
1. Confirm suspected URLs (root + key paths):
   - Homepage
   - Product pages
   - Cart/checkout
   - Contact/support pages
   - Policy pages
2. Determine **platform** (Shopify indicators):
   - `myshopify.com` references
   - Shopify checkout pattern
   - `cdn.shopify.com` assets
   - Page source mentions `Shopify`.
3. Determine **threat**: phishing vs counterfeit vs brand confusion.

**0:10–0:40 — Minimal evidence capture (don’t overthink)**
Create an **Evidence Vault** (template below) and capture:
- Full-page screenshots of:
  - homepage
  - at least 2 product pages
  - cart
  - checkout (if reachable without entering real card data)
- **HTML source** (save as .html) for each key page.
- **Network identifiers** (best-effort):
  - DNS A/AAAA/CNAME
  - WHOIS summary (registrar, nameservers)
  - CDN indicator (e.g., Cloudflare nameservers).
- **Brand ownership proof** (one file):
  - trademark certificate(s) if available, or
  - corporate registration + domain ownership + brand social proofs.

**0:40–1:10 — Fast mini-audit (30-minute deliverable) + client-ready summary**
Produce the “Minimal Viable Proof” one-pager (section 6):
- What it is
- Why it’s harmful
- Where it’s hosted / routed (best-effort)
- Top 3 takedown levers
- ETA expectations

**1:10–1:40 — Parallel takedown filings (highest leverage first)**
File in this order **in parallel** (routing map below explains why):
1. **Shopify** (platform) — IP/impersonation/phishing report.
2. **CDN / Security provider** (often Cloudflare) — phishing/trademark.
3. **Registrar** — abuse report (impersonation / fraud).
4. **Ad/distribution** (if ads are running): Meta + Google.
5. **Google Safe Browsing** (if phishing/fraud signals).

**1:40–2:00 — Customer protection comms (only if needed)**
- Publish a **brand warning** page/post: “We are not affiliated with X domain.”
- Prepare CS macro for inbound tickets.
- If there is customer data risk: advise password reset for accounts (if applicable) and chargeback guidance.

Deliverables by T+2h:
- Evidence Vault created and share link ready.
- “Minimal Viable Proof” audit one-pager.
- First wave reports submitted + tracker updated.
- Client update: what filed, where, and what to expect.

---

### First 24 hours — “Escalate, follow up, expand coverage”

**2:00–6:00 — Follow-up + completeness pass**
- Ensure every abuse submission includes:
  - exact infringing URLs
  - your rights basis (trademark/copyright)
  - signature + good-faith/accuracy statements where needed
  - contact info
  - evidence attachments/links.
- Add evidence for:
  - order confirmation emails (use test data only; do not use real card)
  - payment processor hints (Shop Pay, Stripe, PayPal logos, etc.)
  - copied images/creative comparisons (side-by-side).

**6:00–24:00 — Second wave actions**
- **Search visibility suppression**
  - Report phishing URLs to Google Safe Browsing.
  - If they’re ranking for your brand, submit **search removal requests** as appropriate (policy-based or legal-based depending on region).
- **Platform-side escalation (if available)**
  - Reply to case IDs with additional URLs + proof.
- **Infrastructure expansion**
  - Identify origin host behind CDN (best-effort) and report to host.

Client update by T+24h:
- Case IDs, who acknowledged, what’s pending.
- Updated ETA ranges.
- Recommended customer comms (if any).

---

### First 72 hours — “Persistence + pressure + prevention” 

**24–48 hours**
- Send structured follow-ups (template below) to:
  - Shopify case thread
  - CDN case thread
  - Registrar abuse
  - Ad platforms
- If the scam migrates domains, repeat fast evidence capture and **link it** to prior case IDs.

**48–72 hours**
- If still live:
  - escalate to legal counsel if client has one (for formal notices / court orders where relevant)
  - consider PR escalation only if client approves (avoid Streisand effect)
  - consider enhanced monitoring: brand keywords + new domain watch.

Closure criteria
- Store offline / suspended AND major distribution sources removed.
- Documentation package delivered to client.
- Post-incident review: what worked, what to automate.

---

## 2) Evidence Vault Template (folder structure + checklist)

### Folder structure (copy/paste)
```
EVIDENCE_VAULT/
  00_README_CASE-SUMMARY.md
  01_CASE-METADATA/
    incident-brief.md
    timeline.md
    key-identifiers.md
    case-ids.md
  02_TARGET-URLS/
    urls.txt
    url-map.csv
  03_SCREENSHOTS/
    2026-02-18_homepage_full.png
    2026-02-18_product-1_full.png
    2026-02-18_cart.png
    2026-02-18_checkout.png
  04_PAGE-SOURCE_HTML/
    homepage.html
    product-1.html
    cart.html
  05_BRAND-PROOF/
    trademark-certificates.pdf
    company-registration.pdf
    domain-ownership.png
    social-proof-links.txt
  06_INFRINGEMENT-COMPARISONS/
    side-by-side_branding.png
    copied-product-photos.png
    copied-copy-deck.md
  07_TECHNICAL/
    dns.txt
    whois.txt
    headers.txt
    ip-asn.txt
    shopify-indicators.txt
  08_REPORTS-SUBMITTED/
    shopify_report.pdf
    cloudflare_abuse_report.pdf
    registrar_abuse_email.eml
    google_safebrowsing_submission.txt
    meta_report_notes.md
  09_COMMS/
    client-updates/
    customer-warning/
  10_EXPORTS/
    zipped-package-for-abuse-teams.zip
```

### Evidence checklist (optimized for abuse teams)
**Must-have (minimum viable):**
- [ ] Target domain + infringing URLs list
- [ ] Timestamped full-page screenshots (homepage + product + cart)
- [ ] Clear description: “They impersonate brand X by using Y”
- [ ] Proof you own/represent the brand (trademark or equivalent)
- [ ] Your contact details

**High-leverage add-ons:**
- [ ] Side-by-side comparisons (your site vs clone)
- [ ] HTML source + logo asset URLs (e.g., on `cdn.shopify.com`)
- [ ] Evidence of payment collection (checkout screenshots; no real payment)
- [ ] Evidence of ads (ad library screenshots, landing URL)
- [ ] WHOIS + nameservers + CDN indicator
- [ ] Any customer complaints/emails (redact personal data)

**Redaction rules:**
- Remove customer PII from screenshots/docs.
- Never include card data.

---

## 3) Takedown Routing Map (who to report first, and in what order)

### Why routing matters
- **Shopify** can disable the merchant/store quickly (highest leverage when it’s truly on Shopify).
- **CDN** (Cloudflare commonly) can disrupt delivery, block phishing, or force origin action; they also forward notices.
- **Registrar** can suspend domain for abuse; slower but durable.
- **Traffic sources** (Meta/Google) reduce harm immediately by cutting distribution.

### Decision tree (quick)
- If **phishing/fraud** → prioritize: **Shopify → CDN → Safe Browsing → Ads platforms → Registrar → Host**.
- If **counterfeit/trademark** → prioritize: **Shopify → Registrar → CDN → Payments clues → Ads platforms**.
- If **non-Shopify lookalike site** → prioritize: **Host/CDN → Registrar → Ads platforms → Safe Browsing**.

### Order of operations (recommended)
1. **Shopify**
   - Use Shopify’s legal/reporting tools for IP / fraud. (DMCA tool is behind login.)
2. **CDN / security provider**
   - Example: Cloudflare says the primary way is the **form** https://abuse.cloudflare.com/ and lists categories (Trademark, Phishing, etc.).
3. **Registrar abuse**
   - File an abuse report to the registrar shown in WHOIS; include evidence + exact domain + nature of abuse.
4. **Origin hosting provider** (if identifiable)
   - Especially if not purely platform-hosted.
5. **Payment processors (best-effort)**
   - Only where you have clear processor identification; submit fraud/IP report.
6. **Distribution**
   - Meta (FB/IG) + Google (Ads) reports + ad library evidence.
7. **Google Safe Browsing**
   - For phishing/malware classification: https://safebrowsing.google.com/safebrowsing/report_phish/

---

## 4) Copy‑paste templates (8–12)

> Notes: Keep templates factual. Attach Evidence Vault links, not huge files. Replace bracketed fields.

### (T1) Client intake questionnaire (copy/paste)
**Subject:** Quick intake — suspected clone store / lookalike domain

1) Your brand
- Legal entity name:
- Primary domain (legit):
- Country/regions served:
- Best contact (name/email/phone):

2) Your rights/proof
- Do you have trademarks? (yes/no) If yes: countries + registration numbers:
- Do you own the brand logos/photos/copy? (yes/no)
- Links to official socials:

3) Incident details
- Suspect domain(s):
- Suspect storefront URL(s) (product pages, checkout):
- When first discovered (date/time/timezone):
- Any customer complaints or chargebacks yet? (count + summary)

4) Harm assessment
- Are they taking payments? (yes/no/unknown)
- Are there paid ads driving traffic? (Meta/Google/TikTok/other + links/screenshots)
- Are they impersonating support emails/phone numbers? (details)

5) Access & approvals
- Who can approve public warnings? (name)
- Do you have in-house counsel? (yes/no + contact)
- Preferred takedown language: (trademark / counterfeit / phishing)

6) Assets to provide (if available)
- Trademark certificate PDFs
- Brand logo files
- Key product images (originals)
- Your standard customer warning wording (if any)

---

### (T2) Initial response to lead (fast conversion)
**Subject:** We can likely disable the clone store quickly — next 30 minutes

Thanks — we handle Shopify clone-store / lookalike-domain takedowns.

**What we’ll do in the first 30 minutes:**
- Confirm whether it’s actually on Shopify and identify the main infrastructure (CDN/registrar).
- Capture admissible evidence (screenshots + source + identifiers).
- Deliver a 1‑page “Minimal Viable Proof” report + recommended takedown path.

**What we need from you (5 minutes):**
- Suspect URL(s)
- Your official domain + brand name
- Any trademark certificates (if you have them)

If you reply with the URLs, we can start immediately. We’ll share ETA ranges and the first set of case IDs within ~2 hours.

---

### (T3) Abuse report email template (registrar/host/CDN when email accepted)
**Subject:** Abuse report — brand impersonation / fraudulent storefront on [domain]

Hello Abuse Team,

I’m reporting a website that is **impersonating our brand** and operating a fraudulent/counterfeit storefront.

**Target:**
- Domain: [domain]
- Key URLs:
  - [url 1]
  - [url 2]
  - [checkout/cart url]

**Nature of abuse:**
- [Trademark infringement / counterfeit goods / phishing / fraud]
- The site uses our brand name/logo: [describe]
- Evidence link (screenshots + comparisons + timestamps): [Evidence Vault link]

**Rights/authorization:**
- Brand: [brand]
- We are the [owner / authorized agent].
- Trademark registration (if applicable): [numbers/regions]

**Requested action:**
- Please investigate and disable the abusive content/service and/or suspend the domain per your abuse policies.

**Contact:**
- Name: [full name]
- Company: [legal entity]
- Email/Phone: [contact]
- Address (if required): [address]

Thank you,
[typed full name]
[title]

---

### (T4) DMCA-style notice template (copyright-specific; adapt to platform requirements)
> Use when the infringement is **copyright** (photos, copy, design), not just trademark.

**Subject:** DMCA Takedown Notice — Copyright infringement on [domain / URLs]

To whom it may concern,

I, [full name], state:

1) I am the owner or authorized agent of the owner of certain copyrighted works.
2) The original copyrighted work is located at: [link(s) to your original pages/assets] and/or described as: [describe].
3) The infringing material is located at the following URL(s):
   - [URL list]
4) My contact information is:
   - Name: [full name]
   - Company: [company]
   - Address: [address]
   - Phone: [phone]
   - Email: [email]
5) I have a good-faith belief that the disputed use is not authorized by the copyright owner, its agent, or the law.
6) The information in this notice is accurate and, under penalty of perjury, I am authorized to act on behalf of the owner.

Electronic signature: [typed full name]
Date: [date]

(Cloudflare lists these required elements for DMCA processing on their abuse reporting page.)

---

### (T5) Follow-up email (structured, increases response rate)
**Subject:** Follow-up — abuse report for [domain] (case #[ID]) — additional URLs/evidence

Hello,

Following up on case **[ID]** regarding **[domain]**.

**New/expanded URL list:**
- [url 1]
- [url 2]
- [url 3]

**Additional evidence:**
- Updated evidence pack: [link]
- Summary: [1–2 bullets]

Given the ongoing harm ([phishing/fraud/counterfeit]), please prioritize review. If you need any additional verification of our rights/authority, tell me exactly what format you require.

Thank you,
[typed name]

---

### (T6) Meta/Google reporting notes (for internal use while filing forms)
**Goal:** get ads and landing pages removed fast.

**What to include:**
- Landing URL(s) and any redirect URLs
- Screenshot of the ad creative + “Sponsored” label
- Explanation: impersonation/counterfeit/phishing
- Trademark/copyright proof
- Evidence Vault link

**Keywords that help reviewers:**
- “Brand impersonation”
- “Fraudulent storefront”
- “Phishing / payment collection” (if true)
- “Unauthorized use of registered trademark”

**Avoid:**
- Legal threats, insults, or speculation.

---

### (T7) Customer comms template (brand warning)
**Title:** Important warning: fraudulent website impersonating [Brand]

We’ve been made aware of a website/domain **not affiliated with [Brand]**:
- [bad domain]

**[Brand]’s only official website is:**
- [your domain]

If you purchased from the fraudulent site:
- Contact your bank/card provider to discuss chargeback options.
- Do not share passwords or verification codes.
- Forward any emails/messages you received to: [your support email]

We are actively working with relevant providers to have the fraudulent site taken down.

---

### (T8) Internal tracker template (CSV)
```
incident_id,reported_domain,platform,threat_tier,first_seen_utc,shopify_case_id,cdn_case_id,registrar_case_id,host_case_id,google_case_id,meta_case_id,status,next_action,next_followup_utc,owner,notes
INC-0001,example.com,Shopify,S1,2026-02-17T21:00Z,,,,,,,Open,File registrar report,2026-02-18T09:00Z,alice,"Taking payments; running IG ads"
```

---

### (T9) Case update to client (2-hour update)
**Subject:** Update: takedown actions started for [domain] — next steps + ETAs

Here’s what’s been completed:
- Evidence Vault created: [link]
- Confirmed indicators: [Shopify / CDN / registrar] (best-effort)
- Reports submitted:
  - Shopify: [case ID / submitted time]
  - CDN (e.g., Cloudflare): [case ID]
  - Registrar: [submitted time / ticket]
  - Google Safe Browsing (if applicable): [submitted]
  - Ads platforms (if applicable): [submitted]

**What to expect (best-effort):**
- First responses: typically within [ranges from section 5]
- We will follow up at: [time]

**What we need from you (if not provided):**
- Trademark certificates / proof of rights
- Approval for public customer warning (if needed)

---

### (T10) Non-legal disclaimer block (use in proposals/emails)
We are not a law firm and do not provide legal advice. We provide operational support for evidence collection, incident coordination, and submission of abuse/IP reports to platforms and service providers. For legal advice or litigation strategy, consult qualified counsel in your jurisdiction.

---

## 5) Time-to-response expectations (best-effort ranges) + how to set expectations

> Reality: Abuse response times vary with evidence quality, severity (phishing gets priority), and provider backlog.

### Typical response ranges (best-effort)
- **Shopify (platform reports):** same day to a few days; **phishing/fraud** tends to be faster.
- **CDN (e.g., Cloudflare via form):** hours to a few days depending on category and completeness.
- **Registrar abuse:** 1–7 days is common; urgent fraud sometimes faster.
- **Origin hosting provider:** hours to several days.
- **Meta/Google ads reports:** hours to a few days; repeat submissions may be needed.
- **Google Safe Browsing phishing:** can be hours to several days to reflect across browsers.

### How to set expectations (script)
- “We can usually **reduce harm within 2–24 hours** by cutting distribution (ads/search) and opening platform tickets.”
- “Full removal can take **24–72 hours** and sometimes longer if the operator migrates domains.”
- “Every report we file includes a complete evidence pack and we run follow-ups on a fixed cadence.”

### Follow-up cadence (recommended)
- T+6h: first follow-up if no acknowledgement for S1
- T+24h: second follow-up with expanded URL list
- T+48h: escalation + link to prior case IDs

---

## 6) Minimal Viable Proof (MVP) — 30-minute mini-audit deliverable (to close payment)

**Deliverable format:** 1 page PDF or Notion doc.

### MVP structure
1. **Executive summary (3 bullets)**
   - “A site at [domain] is impersonating [brand] and [taking payments/collecting data/selling counterfeits].”
2. **Evidence (3–6 items)**
   - 3 screenshots + timestamps
   - 3 key URLs
3. **Attribution (best-effort)**
   - Platform indicators (Shopify yes/no)
   - CDN/registrar indicators (nameservers/WHOIS summary)
4. **Recommended takedown path (top 3 actions)**
   - e.g., Shopify report + Cloudflare phishing/trademark + registrar abuse.
5. **ETA ranges + risks**
   - expected response windows
   - risk of domain hopping
6. **Client actions required**
   - provide trademark proof
   - approve customer warning

**Why this closes:** Client sees competence + a concrete plan + proof you can act immediately.

---

## Appendix — Cloudflare abuse reporting notes (source-backed)
Cloudflare’s “Reporting abuse” page states:
- Primary method is the **abuse reporting form**; email is generally not processed.
- Categories include **Trademark Infringement** and **Phishing & Malware**.
- For DMCA reports they list required elements (signature; identify infringed work; identify infringing URLs; contact info; good-faith statement; accuracy/perjury statement).
Source: https://www.cloudflare.com/trust-hub/reporting-abuse/
