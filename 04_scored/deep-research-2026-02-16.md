# Deep Research — 2026-02-16

## 0) Source scan (deep)
**Сканировано:** Reddit RSS (r/smallbusiness, r/shopify, r/marketing, r/sysadmin, r/Entrepreneur, r/freelance), HN (ask/newest/show), Product Hunt feed, TechCrunch RSS, NIST news, EDPB news.

**Недоступно/пропущено:**
- ICO news URL из whitelist вернул 404 (страница не найдена).
- Indie Hackers feed (ранее: JS-shell/no usable payload).
- FT/The Information/G2/Capterra/Trustpilot: в рамках этого прогона не использованы (временной приоритет на pain-first RSS).

---

## 1) Raw signals (30)
> Фильтр: боль + повторяемость/готовность платить/слабость текущего решения.

1. Google AI Overview рекомендует конкурента по брендовому запросу SMB → прямая потеря лидов.  
   https://www.reddit.com/r/smallbusiness/comments/1r6de4t/google_overview_is_crediting_the_wrong_brand_for/
2. SMB не умеют ловить жалобы до 1★ review (реактивный режим).  
   https://www.reddit.com/r/smallbusiness/comments/1r6es31/yeah_so_i_went_down_a_rabbit_hole_on_reviews/
3. Shopify merchant: 14-day payout hold из‑за несовпадения юр. адреса/KYC.  
   https://www.reddit.com/r/shopify/comments/1r6ctw8/your_shopify_payments_address_must_perfectly/
4. Shopify merchant: повторные иски за “marked down pricing” (compliance-law risk).  
   https://www.reddit.com/r/shopify/comments/1r6azs0/sued_again_over_marked_down_pricing_warning_to/
5. Shopify merchants фиксируют shift: SEO трафик вниз, важнее AI discovery (ChatGPT/Gemini).  
   https://www.reddit.com/r/shopify/ (post: AI visibility optimization)
6. Marketing teams шлют bulk из Microsoft inbox → fear доменной репутации и спама.  
   https://www.reddit.com/r/marketing/comments/1r6anft/mass_email_service_thats_trustworthy/
7. SEO топ-3 в Google, но 0 упоминаний в AI answers → новый “visibility gap”.  
   https://www.reddit.com/r/marketing/comments/1r617ad/how_to_improve_ai_brand_visibility_when_your_site/
8. Sysadmin: shared/default password culture + pushback execs на mandatory reset.  
   https://www.reddit.com/r/sysadmin/comments/1r691da/why_are_people_like_this/
9. Sysadmin: cloud outage noise (AWS/Cloudflare/X), маленьким ИТ сложно быстро понять blast radius.  
   https://www.reddit.com/r/sysadmin/comments/1r6agfw/huge_spike_in_downdetector_for_x_aws_cloudflare/
10. Ask HN: нужен feedback loop для coding agents (UI click-through/test-in-the-loop).  
    https://news.ycombinator.com/item?id=47038200
11. HN: open source agent testing (prompt injection/tool misuse/PII leakage) как явный pain category.  
    https://news.ycombinator.com/item?id=47036689
12. HN: “AI with license to drive app state” — спрос на agent QA automation.  
    https://news.ycombinator.com/item?id=47036273
13. HN: интерес к auditable AI chains / semantic firewall (trust/governance gap).  
    https://news.ycombinator.com/item?id=47036691
14. Product Hunt: SearchSeal “Track what AI says about your brand” — рынок уже голосует за GEO/AEO tools.  
    https://www.producthunt.com/products/searchseal
15. Product Hunt: Toolspend — tracking AI spend/usage/cost (FinOps боль в AI-стеках).  
    https://www.producthunt.com/products/toolspend
16. Product Hunt: HookWatch — webhook monitoring для small teams (ops reliability pain).  
    https://www.producthunt.com/products/hookwatch
17. Product Hunt: MockAPI Dog — instant mock REST+LLM APIs (dev velocity спрос).  
    https://www.producthunt.com/products/mockapi-dog
18. Product Hunt: agent tooling launches кластером (Agent Bar/JDoodle MCP/chowder.dev) → новый distribution channel и перегретая конкуренция в generic agent-tools.  
    https://www.producthunt.com/products/agent-bar
19. NIST: запрос на информацию по securing AI agent systems (регуляторный/enterprise pressure).  
    https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems
20. NIST: draft guidance по cybersecurity в AI era (требования будут ужесточаться).  
    https://www.nist.gov/news-events/news/2025/12/draft-nist-guidelines-rethink-cybersecurity-ai-era
21. TechCrunch: India AI Summit с Big Tech + policy фокус (ускорение enterprise adoption + compliance).  
    https://techcrunch.com/2026/02/16/all-the-important-news-from-the-ongoing-india-ai-summit/
22. TechCrunch: persistent investor fear around AI economics (давление на measurable ROI).  
    https://techcrunch.com/2026/02/16/fractal-analytics-muted-ipo-debut-signals-persistent-ai-fears-in-india/
23. TechCrunch: data-center power bottleneck в AI (cost pressure, нужен контроль AI-расхода).  
    https://techcrunch.com/2026/02/15/as-ai-data-centers-hit-power-limits-peak-xv-backs-indian-startup-c2i-to-fix-the-bottleneck/
24. r/freelance: anti-real-world assessments (без docs/AI/internet) + zero feedback → боль dev screening quality.  
    https://www.reddit.com/r/freelance/comments/1r1a4yu/rejected_by_proxify_despite_years_of_professional/
25. r/freelance: scope creep/бесплатные “добавки” от клиентов → recurring conflict ops.  
    https://www.reddit.com/r/freelance/
26. r/Entrepreneur: burn $40k без валидации, акцент на customer interviews/MVP early.  
    https://www.reddit.com/r/Entrepreneur/comments/1r663ou/the_hardest_lesson_i_learned_after_burning/
27. r/Entrepreneur: distrust в founder communities/доказательство revenue (trust verification pain).  
    https://www.reddit.com/r/Entrepreneur/comments/1r6cy1x/the_tall_poppy_syndrome_in_this_sub_is_diabolical/
28. HN Show: C2PA hardware-signed photos для insurance/KYC/inspection use-cases (fraud-proof media demand).  
    https://news.ycombinator.com/item?id=47038153
29. HN Show: Wheelchair accessibility scoring API (данные качества локаций, отраслевые vertical APIs).  
    https://news.ycombinator.com/item?id=47038151
30. HN/PH общий паттерн: много “agent wrappers”, мало доказанного retention/ROI → окно для vertical outcome tools.  
    https://hnrss.org/show

---

## 2) Консолидация в ниши (10)

1. **AI Brand Visibility Ops (GEO/AEO)** — мониторинг/ремедиация упоминаний в AI answers.  
2. **Shopify Compliance & Payout Guard** — preflight KYC + pricing/legal checks.  
3. **Pre-Review Recovery for SMB** — перехват негатива до публичного review.  
4. **Sender Reputation Control Plane (SMB)** — policy/guardrails для bulk email.  
5. **Agent QA Feedback Loop Platform** — агент кликает UI, гоняет smoke/e2e, отчитывается.  
6. AI Agent Security Testing (red-team, injection, data leakage).  
7. AI Spend Governance / Mini FinOps for SMB+midmarket.  
8. MSP Security Adoption Copilot (change-management + risk comms).  
9. Ecommerce Legal Radar (региональные “drive-by” claims alerts).  
10. Verified Photo Evidence API (C2PA) для insurance/field ops.

---

## 3) Ranking top-5 (счёт 0–100)

| Rank | Ниша | Score |
|---|---|---:|
| 1 | AI Brand Visibility Ops (GEO/AEO) | **87** |
| 2 | Shopify Compliance & Payout Guard | **84** |
| 3 | Sender Reputation Control Plane | **79** |
| 4 | Pre-Review Recovery for SMB | **76** |
| 5 | Agent QA Feedback Loop Platform | **72** |

---

## 4) Top-5: практические карты

### 1) AI Brand Visibility Ops (GEO/AEO) — **87/100**
**ICP:** SMB/DTC brands (маркетинг-лид/основатель), SEO-агентства 3–30 клиентов.  
**Острая боль:** бренд теряет конверсию: в AI-ответах рекомендуют конкурента или не цитируют бренд вообще.  
**Evidence:**
- r/smallbusiness: wrong brand in Google Overview.  
  https://www.reddit.com/r/smallbusiness/comments/1r6de4t/google_overview_is_crediting_the_wrong_brand_for/
- r/marketing: ranking в Google есть, AI mentions нет.  
  https://www.reddit.com/r/marketing/comments/1r617ad/how_to_improve_ai_brand_visibility_when_your_site/
- PH: SearchSeal launch (категория уже платит).  
  https://www.producthunt.com/products/searchseal
**Почему сейчас:** shift from classic SEO to AI answers + рынок ещё фрагментирован, мало “actionable remediation”.  
**MVP за 14 дней:**
- Трекинг 50–200 queries/бренд (ChatGPT/Gemini/Perplexity вручную+скрипт).
- Детект: cited / not cited / misattributed.
- “Fix queue”: schema/entity mismatch, citation gaps, PR pages, directory updates.
- Weekly proof report: visibility delta.
**GTM первых 10 клиентов:**
1) Аутрич к SEO/контент-агентствам (cold email + LinkedIn) с free audit 20 queries.  
2) Посты-кейсы в r/marketing/r/smallbusiness + X с before/after скринами.  
3) 2 пилота “pay on uplift”.
**Pricing гипотеза:** $149/mo (1 бренд), $399/mo (агентство до 5 брендов), setup $300 one-time.  
**Главные риски:** API/ToS ограничения, волатильность AI answer formats, шум в attribution.  
**Scoring breakdown (0–5):** Pain 5, WTP 4.5, Frequency 4.5, Distribution 4.5, Feasibility 4, Advantage 4, Retention 4.5, Risk 3.5.

---

### 2) Shopify Compliance & Payout Guard — **84/100**
**ICP:** Shopify merchants $20k–$500k MRR, ops/finance owner.  
**Острая боль:** payout hold и юридические претензии бьют по кэшу и марже.  
**Evidence:**
- 14-day payout hold через KYC mismatch.  
  https://www.reddit.com/r/shopify/comments/1r6ctw8/your_shopify_payments_address_must_perfectly/
- lawsuits over marked-down pricing.  
  https://www.reddit.com/r/shopify/comments/1r6azs0/sued_again_over_marked_down_pricing_warning_to/
**Почему сейчас:** tightening KYC/compliance, рост правовых рисков в ecommerce.  
**MVP за 14 дней:**
- Checklist engine: юр. имя/адрес/доки consistency.
- Monitor storefront promo rules (compare-at, price history flags).
- Alert board + “fix steps before hold/risk”.
**GTM первых 10 клиентов:**
1) Партнёрство с 2–3 Shopify agencies/бухгалтерами.  
2) Бесплатный “Compliance preflight” на 30 мин.  
3) Кейсы в Shopify community + targeted DMs в founder groups.
**Pricing гипотеза:** $199/mo store + $500 onboarding audit.  
**Главные риски:** legal liability wording, региональные различия законов, false positives.  
**Scoring:** Pain 5, WTP 4.5, Frequency 4, Distribution 3.5, Feasibility 4, Advantage 4, Retention 4, Risk 3.

---

### 3) Sender Reputation Control Plane — **79/100**
**ICP:** SMB 20–300 сотрудников на Microsoft 365/Google Workspace, маркетинг+IT.  
**Острая боль:** сотрудники шлют mass emails из рабочих inbox → spam placement и испорченный домен.  
**Evidence:**
- explicit pain thread в r/marketing про central admin/safeguards/reporting.  
  https://www.reddit.com/r/marketing/comments/1r6anft/mass_email_service_thats_trustworthy/
- recurring community-level concern по deliverability governance.  
  https://www.reddit.com/r/marketing/.rss
**Почему сейчас:** больше outbound у lean teams, но нет email-ops экспертизы.  
**MVP за 14 дней:**
- SMTP/API monitor входящих bulk-паттернов.
- Policy guardrails: block/route-to-ESP при N recipients.
- DKIM/SPF/DMARC health + sender score dashboard.
**GTM первых 10 клиентов:**
- MSP/IT-аутсорсеры как канал.  
- Cold outreach к Head of Marketing + IT Admin.  
- Offer: “2-week sender risk audit”.
**Pricing гипотеза:** $99–299/mo по объёму доменов/ящиков.  
**Главные риски:** интеграции с O365/Gmail, perceived overlap with ESPs, support load.  
**Scoring:** Pain 4.5, WTP 4, Frequency 4.5, Distribution 3.5, Feasibility 4, Advantage 3.5, Retention 4, Risk 4.

---

### 4) Pre-Review Recovery for SMB — **76/100**
**ICP:** локальные сервисные SMB (клиники, авто, home services, hospitality-lite).  
**Острая боль:** негативные отзывы появляются раньше, чем бизнес успевает исправить проблему.  
**Evidence:**
- “как перехватывать complaints до 1-star” from r/smallbusiness.  
  https://www.reddit.com/r/smallbusiness/comments/1r6es31/yeah_so_i_went_down_a_rabbit_hole_on_reviews/
- связка с discoverability pain (reviews влияют на local + AI recommendations).  
  https://www.reddit.com/r/smallbusiness/comments/1r6de4t/google_overview_is_crediting_the_wrong_brand_for/
**Почему сейчас:** репутационный signal всё сильнее влияет на AI-mediated discovery.  
**MVP за 14 дней:**
- SMS/WhatsApp post-service pulse (NPS+issue capture).
- Escalation inbox для менеджера до публикации review.
- “Rescue playbooks” + auto-followup.
**GTM первых 10 клиентов:**
- 2 локальных агентства как реселлеры.  
- Door-to-door/LinkedIn to multi-location owners.  
- Free first month за кейс/отзыв.
**Pricing гипотеза:** $79/location/mo + usage.  
**Главные риски:** churn у микробизнесов, “review gating” policy boundaries, операционный onboarding.  
**Scoring:** Pain 4, WTP 3.5, Frequency 4.5, Distribution 4, Feasibility 4.5, Advantage 3.5, Retention 3.5, Risk 3.5.

---

### 5) Agent QA Feedback Loop Platform — **72/100**
**ICP:** AI-native dev teams 3–30 инженеров, shipping web apps weekly.  
**Острая боль:** coding agents генерят код, но не закрывают надёжно UI verification loop.  
**Evidence:**
- Ask HN про feedback loop with coding agents.  
  https://news.ycombinator.com/item?id=47038200
- HN “AI can drive app state” prototype interest.  
  https://news.ycombinator.com/item?id=47036273
- HN/PH saturation в generic agent wrappers (нужна outcome-ориентированная QA ниша).  
  https://hnrss.org/show
**Почему сейчас:** adoption coding agents уже есть, а QA/verification слой отстаёт.  
**MVP за 14 дней:**
- Browser runner + сценарии smoke tests.
- Assertion templates (“button exists”, “form submits”, “error absent”).
- PR comment summary + replay video.
**GTM первых 10 клиентов:**
- OSS repo launch + devtool communities/HN Show.  
- Direct outreach to teams already using Claude Code/Cursor/OpenClaw.  
- 14-day free trial + concierge setup.
**Pricing гипотеза:** $49/dev/mo или usage-based по test runs.  
**Главные риски:** высокая конкуренция в devtools, flaky tests, сложный onboarding.  
**Scoring:** Pain 4, WTP 3.5, Frequency 4, Distribution 3.5, Feasibility 3.5, Advantage 3.5, Retention 4, Risk 3.5.

---

## 5) Жёсткая рекомендация (actionable)

### Build Now (1)
1. **AI Brand Visibility Ops (GEO/AEO).**  
Причина: самый высокий score + явная денежная боль + быстрый MVP + понятный канал через агентства.

### Validate (2)
1. **Shopify Compliance & Payout Guard** — 7-дневный smoke test с 10 магазинами.  
2. **Sender Reputation Control Plane** — 10 discovery calls (IT+Marketing) + 2 pilot домена.

### Hold / Kill (остальные)
- **Hold:** Pre-Review Recovery (годно, но меньше ACV и выше SMB churn).  
- **Hold:** Agent QA Feedback Loop (перегретая devtool конкуренция).  
- **Hold:** MSP Security Adoption Copilot (service-heavy motion).  
- **Hold:** AI Spend Governance mini-FinOps (нужны deeper integrations).  
- **Kill (на сейчас):** Generic agent wrapper / broad “AI employee” tools без чёткой вертикальной боли.

---

## 6) Next 7 days (без воды)
- Day 1–2: 20 интервью (10 SMB brands + 10 SEO agencies) по GEO pain.  
- Day 3: wizard для query-set + baseline report (ручной backend).  
- Day 4–5: remediation checklist engine + weekly delta report.  
- Day 6: 5 paid pilot офферов ($149/mo, first month -50%).  
- Day 7: решение go/no-go по conversion to paid (цель: >=2 paid pilots).
