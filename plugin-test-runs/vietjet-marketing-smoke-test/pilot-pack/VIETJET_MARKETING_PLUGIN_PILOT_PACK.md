# Vietjet Marketing Plugin Pilot Pack

## 1. Executive Summary

- Tests run: **8**
- Passed: **6**
- Partially passed: **2**
- Failed: **0**
- Average score: **4.5/5**
- Recommendation: **Keep and improve**

The Vietjet Marketing plugin suite is suitable for controlled internal pilot use. It can accelerate drafting, governance checks, and internal review, but it is not external-publication automation.

## 2. What The Plugin Is Good At

- **Promo QA:** Finds expired periods, unclear 0Đ terms, unsupported inventory, and risky CTAs.
- **Route launch briefs:** Creates useful positioning, audience hypotheses, messaging, and channel plans without inventing route economics.
- **IP-safe cultural campaigns:** Converts risky football-event ideas into safe, travel-first creative platforms.
- **Aircraft and creative prompt discipline:** Applies locks, negative prompts, manual typography, and approved-reference requirements.
- **CRM governance:** Produces draft copy while flagging consent, suppression, privacy, and frequency-cap needs.
- **Visual QA:** Separates visual, IP, brand, and commercial issues and recommends revision when needed.
- **Business-scenario boundaries:** Avoids invented business cases, ROI, and incremental-revenue claims.
- **End-to-end mini campaigns:** Connects strategy, copy, creative prompts, measurement, and human review.

## 3. What Still Needs Improvement

- Command-level invocation and skill selection could be clearer.
- Output templates should be more standardized.
- Human approval gates should be easier for marketers to understand.
- Asset and video production should remain separate from campaign thinking.
- Production readiness must not be confused with concept readiness.

The pilot-confirmed orchestration gap is addressed by a small optional command set for high-risk
and multi-skill flows. Direct skill prompts remain the default for simpler work.

## 4. Recommended Pilot Scope

### In Scope

- Internal marketing planning
- Campaign ideation
- Promo copy QA
- Creative prompt drafting
- Route-launch first drafts
- CRM push drafts
- Visual QA checklists
- Leadership brief drafts

### Out Of Scope

- Automatic launch approval
- Automatic external publication
- Final legal approval
- Final fare, route, or revenue claims
- Final media-budget approval
- Final visual-asset approval
- Video-production approval

## 5. Best 3 Smoke Test Examples

### Promo QA

- **Why it worked:** Immediately detected the expired SALE66 booking period, unsafe CTA, unsupported inventory, and incomplete 0Đ terms.
- **Business value:** Reduces misleading promo copy and preventable launch errors.
- **Marketer use:** Paste a promo brief and channel copy before requesting Commercial, Revenue, and Legal review.

### Route Launch Brief

- **Why it worked:** Produced positioning, audiences, messages, and channels while keeping route, date, and aircraft as facts to verify.
- **Business value:** Gives teams a useful first draft without inventing demand, fare, frequency, or revenue.
- **Marketer use:** Start route-launch alignment before authorized route evidence and performance data arrive.

### Visual QA

- **Why it worked:** Correctly blocked fake logos, distorted text, official-looking sports assets, trophy-like objects, and unsupported 0Đ copy.
- **Business value:** Helps creative teams catch obvious visual, IP, brand, and commercial risks early.
- **Marketer use:** Review AI-generated concepts before sending them to Brand, Legal, or Commercial reviewers.

## 6. Two Partial Passes

### Creative Prompt For A330 KV

- **What worked:** Strong prompt structure, negative prompt, aircraft-lock categories, and manual-logo guidance.
- **What was missing:** An approved aircraft and livery reference, so exact identity details could not be confirmed.
- **How to improve:** Supply the approved reference and explicitly state visible side, angle, registration policy, and livery constraints.

### Business Scenario Planning

- **What worked:** Refused to invent a final business case, ROI, or incremental revenue; created a governed assumptions template.
- **What was missing:** Budget, baseline, CTR, conversion, ABV, and control/holdout evidence.
- **How to improve:** Use a shorter planning-scenario prompt and provide validated inputs before invoking a full Revenue PMO workflow.

## 7. Suggested Marketer Workflow

1. Start with the campaign request and available facts.
2. Use `vietjet-commercial-ops` for facts, claims, risks, and measurement boundaries.
3. Use `vietjet-creative-factory` for creative prompts and asset briefs.
4. Use visual QA before using any AI image.
5. Create a leadership brief with decisions and missing data.
6. Complete human reviews before external use.

## 8. Copy-Paste Prompts For Marketers

### 1. Promo QA

> Dùng `vietjet-commercial-ops` và skill `promo-qa`. Kiểm tra promo dưới đây về thời gian, claim giá, điều kiện vé, inventory và copy rủi ro. Tách rõ lỗi cần sửa và approval cần có: [dán brief].

### 2. Route Launch Brief

> Dùng `vietjet-commercial-ops`, skills `route-marketing` và `campaign-factory`. Tạo route-launch brief cho [route]. Tách facts, assumptions, missing data; không tự bịa fare, frequency, demand hoặc revenue.

### 3. Campaign Idea

> Dùng hai plugin để tạo campaign idea cho [chủ đề]. Giữ ý tưởng travel-first, kiểm tra claim/IP risk, và đề xuất thông điệp an toàn để team marketing phát triển tiếp.

### 4. Creative KV Prompt

> Dùng `vietjet-creative-factory` tạo prompt KV 4:5 cho [campaign]. Không tạo text/logo trong ảnh, chừa safe zone, thêm negative prompt và nêu rõ reference nào còn thiếu.

### 5. 9:16 Video Prompt

> Dùng `vietjet-creative-factory` tạo prompt video 9:16 dài [số giây]. No text, no subtitle, no logo. Viết shot list ngắn, continuity rules và negative prompt.

### 6. CRM Push Copy

> Dùng `vietjet-commercial-ops` và skill `crm-personalization`. Viết 5 app push ngắn cho [campaign]. Không claim personalization nếu chưa có data; flag consent, suppression và frequency cap còn thiếu.

### 7. Visual QA

> Dùng `vietjet-creative-factory` và skill `visual-qa`. Review visual/prompt này về logo, text lỗi, IP, anatomy, commercial claims và channel fit. Không approve; chỉ nêu blocker và revision cần làm.

### 8. Leadership Brief

> Dùng `vietjet-commercial-ops` tạo leadership brief một trang cho [campaign]. Tóm tắt quyết định cần đưa ra, facts, assumptions, missing data, risks và human approvals cần thiết.

## 9. Governance Rule Of Thumb

- Không có nguồn thì không claim.
- Không có Legal/IP review thì không dùng official event assets.
- Không có fare terms thì không nói 0Đ như chắc chắn.
- Không có human QA thì không dùng asset AI externally.
- Không có approval owner thì không gọi là approved.
- Gross revenue không phải incremental revenue.

## 10. Final Recommendation

Proceed with a controlled internal pilot. Use the suite to accelerate drafts and QA while keeping
human approval mandatory.

Command UX refinement starts with six thin commands only: promo QA, route launch, lightweight
planning scenario, end-to-end mini campaign, creative KV, and visual QA. Add further commands only
after pilot evidence shows a repeated need.
