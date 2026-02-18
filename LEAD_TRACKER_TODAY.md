# Lead Tracker - Daily Operating System

## Quick Start Guide

1. **Morning Routine (5 min)**
   - Open CSV in Google Sheets/Excel
   - Filter by: status = new OR status = contacted
   - Sort by: urgency_score DESC, incident_date ASC

2. **Daily Outreach**
   - Contact 5-10 new leads (priority order)
   - Update status and next_followup_date
   - Add notes from conversations

3. **End of Day (2 min)**
   - Mark completed follow-ups
   - Schedule tomorrow's actions
   - Calculate daily stats

---

## Column Definitions

| Column | Type | Description | Format |
|--------|------|-------------|--------|
| lead_id | String | Unique identifier | L001, L002, etc. |
| brand_name | String | Company/brand name | Plain text |
| contact_handle | String | Social handle/username | @username |
| contact_email | String | Email address | email@domain.com |
| source_type | String | Lead source | reddit/meta_ads/agency/referral/cold_outreach |
| source_url | String | Original source URL | https://... |
| suspect_urls | String | URLs with stolen content | comma separated |
| incident_date | Date | When content was stolen | YYYY-MM-DD |
| status | String | Current lead status | See Status Workflow |
| urgency_score | Number | Priority level (1-5) | 1=Low, 5=Critical |
| next_followup_date | Date | Next contact date | YYYY-MM-DD |
| next_followup_action | String | Planned action | call/email/message |
| estimated_value | Number | Potential deal value | Numeric (USD) |
| notes | String | Conversation notes | Free text |

---

## Status Workflow Diagram

```
                    ┌─────────────┐
                    │    NEW      │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ CONTACTED   │◄─────────┐
                    └──────┬──────┘          │
                           │                 │
                           ▼                 │
                    ┌─────────────┐          │
                    │  REPLIED    │          │
                    └──────┬──────┘          │
                           │                 │
                           ▼                 │
                    ┌─────────────┐          │
                    │ CALL_BOOKED │          │
                    └──────┬──────┘          │
                           │                 │
                           ▼                 │
                    ┌─────────────┐          │
                    │    PAID     │          │
                    └─────────────┘          │
                           │                 │
                           ▼                 │
                           └─────────────────┘
                                 │
                                 │ (At any stage)
                                 ▼
                    ┌─────────────┐
                    │    LOST     │
                    └─────────────┘
```

### Status Definitions & Transition Rules

| Status | Definition | How to Transition | Next Action |
|--------|------------|-------------------|-------------|
| **new** | Unprocessed lead | Auto on import | Research & contact |
| **contacted** | Sent initial message | After first outreach | Wait 48-72h |
| **replied** | Lead responded | When lead replies | Schedule call |
| **call_booked** | Meeting scheduled | Calendar confirmed | Prepare pitch |
| **paid** | Converted to client | Payment received | Onboarding |
| **lost** | Not interested | Declined/ghosted (7+ days) | Archive |

---

## Daily Operating Routine

### Morning Review (9:00 AM)
1. **Check urgency**
   - Filter: urgency_score >= 4, status = "new"
2. **Review overdue follow-ups**
   - Filter: next_followup_date < TODAY()

### Outreach Cadence
| Day Since Contact | Action | Status Update |
|-------------------|--------|---------------|
| Day 0 | Initial outreach | new → contacted |
| Day 2 | Second attempt | contacted → contacted |
| Day 5 | Final attempt | contacted → lost (if no response) |
| Day 7 | Re-engagement (optional) | lost → contacted |

### Priority Matrix
1. **Urgency 5 + Status = new** → Contact immediately
2. **Urgency 4-5 + Status = replied** → Schedule call today
3. **Urgency 3+ + overdue follow-up** → Re-engage
4. **High estimated_value (> $5k)** → Personal outreach

---

## Example Rows (10 Realistic Leads)

Here are realistic examples to guide your data entry:

1. **Reddit Lead - High Urgency**
   - Brand: "TetonGlow" stole UGC ad creatives
   - Source: r/advertising thread
   - Urgency: 5/5 (active theft, losing revenue)

2. **Meta Ads Discovery**
   - Brand: "Biossance" running stolen creatives
   - Source: Facebook Ad Library
   - Urgency: 4/5 (large brand, high value)

3. **Agency Referral**
   - Brand: "SkinFix" - creative agency referral
   - Source: Agency partner
   - Urgency: 3/5 (warm lead, slower process)

4. **Cold Outreach - D2C Brand**
   - Brand: "Vitality Labs" - Instagram DM
   - Source: Instagram research
   - Urgency: 3/5 (prospect, not incident)

5. **Repeat Offender**
   - Brand: "LuxeBeauty" (2nd time offender)
   - Source: Existing client report
   - Urgency: 5/5 (legal escalation needed)

---

## CSV Export Block

**Copy this block and paste into Google Sheets/Excel:**

```csv
lead_id,brand_name,contact_handle,contact_email,source_type,source_url,suspect_urls,incident_date,status,urgency_score,next_followup_date,next_followup_action,estimated_value,notes
L001,TetonGlow,@tetonglow,hello@tetonglow.com,reddit,https://reddit.com/r/advertising/comments/abc123,https://tetonglow.com/products/glow-serum-ad,2026-02-15,new,5,2026-02-18,email,2500,"Stole UGC ad creative from our client. Active Meta Ads campaign using stolen video. High urgency - client losing revenue daily."
L002,Biossance,@biossance,legal@biossance.com,meta_ads,https://www.facebook.com/ads/library,https://biossance.com/pages/squalane-serum,2026-02-10,contacted,4,2026-02-20,email,5000,"Facebook Ad Library search shows stolen carousel ad. Email sent 2026-02-16. Waiting for response."
L003,SkinFix,@skinfix,partners@skinfix.com,agency,Agency referral - Creative Partners,N/A,2026-02-12,replied,3,2026-02-19,call,3500,"Warm intro from Creative Partners agency. Sarah responded positively. Call scheduled for 2026-02-19 2pm EST."
L004,Vitality Labs,@vitalitylabs,info@vitalitylabs.com,cold_outreach,Instagram research,N/A,2026-02-18,new,3,2026-02-18,instagram_dm,4000,"Prospect via Instagram. They are scaling quickly, likely need creative protection. No incident yet - proactive outreach."
L005,LuxeBeauty,@luxebeauty,legal@luxebeauty.com,referral,Existing client - GlowGlow,https://luxebeauty.com/ads/new-launch,2026-02-14,new,5,2026-02-18,call,7500,"REPEAT OFFENDER - 2nd time stealing creatives. Client is furious. Escalate to legal. Demand immediate takedown + payment."
L006,PureRadiance,@pureradiance,contact@pureradiance.com,reddit,https://reddit.com/r/tiktokmarketing/comments/xyz789,https://pureradiance.com/tiktok-ads,2026-02-08,contacted,2,2026-02-22,email,1500,"Small brand, stolen TikTok creative. Low value. Sent initial email, following up in 4 days."
L007,ElevateSkin,@elevateskin,team@elevateskin.com,meta_ads,https://www.facebook.com/ads/library,https://elevateskin.com/shop/best-sellers,2026-02-16,new,4,2026-02-19,email,6000,"Multiple stolen ads visible. Well-funded brand (5M+ funding). High value target."
L008,GlowProtocol,@glowprotocol,founder@glowprotocol.com,reddit,https://reddit.com/r/redditads/comments/def456,https://glowprotocol.com/ads/valentine,2026-02-17,lost,2,N/A,N/A,0,"Responded - created content in-house. Not interested. No payment potential."
L009,LuminaBeauty,@luminabeauty,sales@luminabeauty.com,agency,Agency: Scale Media,N/A,2026-02-11,call_booked,4,2026-02-21,call,4500,"Agency partner referred. Discovery call on calendar. Prepare case studies + pricing."
L010,RadiantGlow,@radiantglow,help@radiantglow.com,cold_outreach,LinkedIn prospecting,N/A,2026-02-18,new,3,2026-02-18,linkedin_message,3000,"D2C brand scaling paid spend. No incident yet - offering creative protection retainer."
```

---

## Quick Stats Formulas

**For Google Sheets/Excel automation:**

### Total Pipeline Value
```
=SUMIF(I:I, "<>lost", O:O)
```

### Leads by Status
```
=COUNTIF(I:I, "new")
=COUNTIF(I:I, "contacted")
=COUNTIF(I:I, "replied")
=COUNTIF(I:I, "call_booked")
=COUNTIF(I:I, "paid")
=COUNTIF(I:I, "lost")
```

### Average Deal Value (Closed)
```
=AVERAGEIF(I:I, "paid", O:O)
```

### Urgent Leads (Score 4-5)
```
=COUNTIF(J:J, ">=4")
```

### Overdue Follow-ups
```
=COUNTIF(L:L, "<" & TODAY())
```

### Conversion Rate
```
=COUNTIF(I:I, "paid") / COUNTA(I:I)
```

### Today's Tasks
```
=FILTER(A:O, (L:L = TODAY()) + ((J:J >= 4) * (I:I = "new")))
```

---

## Tips for Success

1. **Update status immediately** after each interaction
2. **Set estimated_value** based on: 
   - Brand size (startup: $1-3k, mid-market: $3-7k, enterprise: $7-15k)
   - Urgency (add 20% for urgency 4-5)
3. **Check suspect_urls personally** before outreach
4. **Personalize first message** - reference specific stolen creative
5. **Archive lost leads** after 30 days (move to separate "Lost Leads" sheet)
6. **Batch outreach** - set 2-hour blocks for messaging (10am-12pm, 3pm-5pm)

---

## Status: Daily Template

**Last Updated:** 2026-02-18  
**Version:** 1.0  
**Maintained By:** SaaS Operations Team

*For questions or suggestions, contact the operations lead.*
