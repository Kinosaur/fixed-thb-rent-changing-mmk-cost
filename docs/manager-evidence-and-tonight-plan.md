# Plan: Manager Evidence and Tonight

**Generated:** 2026-08-05
**Estimated effort:** 45–60 minutes, excluding waiting for a reply.

## Goal

Start an evidence-backed new-tenant asking-rent comparison without delaying the SQL learning project.

## Task 1: Ask the condo manager

Send the message below. Ask for current comparable asking rent first; historical prices are useful only if the manager already has them.

> Hello [Manager's name], I am currently renting Room B401. I am doing a personal student data-analysis project about housing costs. Could you please share the current asking-rent range for rooms comparable to mine in Building B? If you have it, I would also appreciate any past asking-rent information or approximate ranges for 2023–2025. For each figure, the room type, furnishing, floor, contract length, and whether utilities are included would be very helpful. I only need anonymous price information—no tenant or owner details—and I will label it as asking rent, not actual signed-contract rent. Thank you very much.

Thai version:

> สวัสดีค่ะ/ครับ คุณ[ชื่อผู้จัดการ] ตอนนี้เช่าห้อง B401 อยู่ และกำลังทำโปรเจกต์วิเคราะห์ข้อมูลส่วนตัวเกี่ยวกับค่าใช้จ่ายด้านที่อยู่อาศัย จึงอยากสอบถามช่วงราคาเช่าที่ประกาศสำหรับห้องที่ใกล้เคียงกับห้องของฉันในอาคาร B ในปัจจุบัน หากมีข้อมูล รบกวนขอราคาเช่าโดยประมาณในช่วงปี 2023–2025 ด้วยค่ะ/ครับ สำหรับแต่ละราคา หากทราบประเภทห้อง เฟอร์นิเจอร์ ชั้น ระยะเวลาสัญญา และรวมค่าสาธารณูปโภคหรือไม่ จะเป็นประโยชน์มาก ต้องการเฉพาะข้อมูลราคาแบบไม่ระบุตัวตน และจะระบุว่าเป็นราคาเสนอเช่า ไม่ใช่ราคาตามสัญญาที่เซ็นจริง ขอบคุณมากค่ะ/ครับ

## Task 2: Record any reply as evidence

When a reply arrives, add one row per price observation to the local file made from `data_templates/market_rent_listings.template.csv`.

Required fields:

- `observed_date`: today, when the manager gave the information.
- `listing_date`: only when the manager gives a specific historical date; otherwise leave blank.
- `source_name`: `Condo manager`.
- `building_name`, `room_type`, `floor`, `furnished_status`, `contract_term_months`, `listed_rent_thb`, and `utilities_included`: record only what was stated.
- `comparable_status`: use `Comparable` only when it is genuinely similar to B401; otherwise use `Needs review`.
- `comparison_reason` and `review_notes`: preserve the manager's wording and differences.

Do not manufacture missing monthly values. A current quote is still useful, but it supports a current snapshot—not a 2023–2026 trend.

### Initial manager evidence received

Four private evidence rows have been recorded on 2026-08-05: 7,000 THB for the manager-reported 2024 and 2025 prices, 7,000 THB before the reported 2026 promotion, and a 6,000 THB promotional price reported as occurring after April 2026. The user confirmed that these are for the same room and approved the annual/period assumption. A separate private monthly scenario applies 6,500 THB for 2023, 7,000 THB through March 2026, and 6,000 THB from April 2026 onward. It remains a manager-reported asking-rent scenario rather than actual market-rent history.

## Task 3: SQL practice while waiting

Create the next query: monthly utilities and utility share.

```sql
utility_cost_thb = total_housing_cost_thb - room_rent_thb
utility_share_pct = utility_cost_thb / total_housing_cost_thb * 100
```

The runnable queries are now `sql/02_monthly_utilities.sql` and `sql/03_contract_protection_scenario.sql`. The latter converts the +500 THB or −500 THB scenario difference to MMK using the monthly median Sell rate.

## Done for tonight

- Manager message sent.
- Reply is recorded faithfully if received.
- The utility-cost SQL query runs and you can explain its two calculated columns.
- The same-room asking-rent scenario runs and its promotion period is visibly labelled.

## Important boundary

The asking-rent comparison is an optional extension. It must be labelled as asking rent, not an actual market contract. The core portfolio continues even if the manager does not have historical prices.
