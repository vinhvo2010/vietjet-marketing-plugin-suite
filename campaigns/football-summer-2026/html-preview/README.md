# Vietjet Campaign Microsite Preview — BAY TỚI MÙA HÈ BÓNG ĐÁ

This directory contains a self-contained concept preview for internal review. It is not a production-ready microsite.

## Production Readiness Warning

- Audit score: **43/100**
- Current release status: **NOT RELEASE READY**
- The page must remain visibly labeled `CONCEPT PREVIEW — NOT PRODUCTION READY`.
- Planning numbers are assumptions only, not approved targets, forecasts, budgets, or business-case evidence.
- Existing generated assets require deterministic preflight and human QA.
- Missing promised video deliverables are P0 blockers.

## Files In This Folder

*   `index.html`: The main structured markup page using semantic HTML5 elements.
*   `styles.css`: Modern, premium styling featuring a Vietjet-inspired red-yellow energy palette, typography hierarchy, and fully responsive layouts.
*   `script.js`: Lightweight, native JavaScript for page interactivity (smooth scroll navigation highlights, business scenario selector, risk register mobile accordions, and a "Copy Summary" clipboard utility).
*   `README.md`: This guide.

## How To Open Locally

Simply open the `index.html` file in any modern web browser:
*   **Double-click** the [index.html](file://<REPO_ROOT>/campaigns/football-summer-2026/html-preview/index.html) file from your file manager.
*   **Or run** in your terminal:
    ```bash
    open campaigns/football-summer-2026/html-preview/index.html
    ```

*No build steps, node modules, or local web servers are required. The preview runs entirely locally and requires no active network connection.*

## Governance & Safety Warning

> [!WARNING]
> **INTERNAL WORKING DRAFT ONLY — NOT FOR EXTERNAL PUBLICATION**
> This microsite is for internal alignment and concept validation. It must not be deployed to public servers, shared externally, or used for commercial publishing.

*   **No Sponsor Implications:** All visual elements are abstract and generic. Do not add official tournament badges, logos, cúp, or FIFA/World Cup rights-related graphics.
*   **No Active Offers:** All commercial offers, pricing layers, and route inventories shown are purely theoretical planning assumptions and must be validated by Vietjet Commercial/Revenue management before launch.
*   **No Direct Budget Approval:** The scenarios presented here serve directional planning only and do not represent committed budgets.

## Asset Lifecycle

- `assets/draft/`: new AI-generated assets awaiting checks
- `assets/rejected/`: failed assets, moved only by an authorized human
- `assets/approved/`: assets with logged human QA evidence
- `assets/release/`: assets authorized for release

Only `assets/release/` may be loaded in release mode. Existing root-level assets remain untouched and blocked from release until remediated.

The concept preview now references corrected JPEG stills from `assets/draft/`. These files pass deterministic MIME, dimension, and ratio checks only. They remain `HUMAN_QA_REQUIRED` and `DO_NOT_RELEASE`. The promised eight-second MP4 remains blocked and missing.

## Preflight

Run from the repository root:

```bash
python3 scripts/preflight/run_preflight.py campaigns/football-summer-2026
```

Preflight checks claims, MIME/extension alignment, dimensions, intended ratios, promised video existence, and HTML release safety. It updates the campaign audit reports. A deterministic preflight never grants human QA or release approval.

## Moving Toward Release Safely

1. Resolve P0 claim and asset blockers using evidence or corrected deliverables.
2. Re-run preflight.
3. Log Brand, Legal/IP, Commercial, Revenue, Measurement, Creative QA, and Media QA reviews. Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.
4. Confirm the authorized final launch owner by policy.
5. Keep the campaign blocked until every release-gate condition is evidenced.

## AI Visuals Generation & Integration

This preview folder is configured to support generated mockup visuals dynamically:
1. Read the image generation guidelines and copy the specific prompts from [GEMINI_IMAGE_PROMPTS.md](file://<REPO_ROOT>/campaigns/football-summer-2026/html-preview/assets/GEMINI_IMAGE_PROMPTS.md).
2. Generate the visual assets using Google Gemini (or any local image generation tool).
3. Save new generated images to the `assets/draft/` directory using controlled filenames and log them in `audit/ASSET_MANIFEST.md`.
   *   `hero-football-travel.png` (Hero banner - 16:9)
   *   `kv-4x5-football-summer.png` (Key Visual - 4:5)
   *   `story-9x16-football-travel.png` (Reels/Story preview - 9:16)
   *   `app-banner-football-summer.png` (App banner preview - 3:1)
   *   `airport-screen-football-summer.png` (Airport screen preview - 16:9)
   *   `dashboard-funnel-abstract.png` (Data dashboard illustration - 16:9)
   *   `carousel-01-hook.png` through `carousel-07-closing.png` (Social carousel slides - 4:5 each)

### Graceful Fallbacks
If these image files are not present in the `assets/` folder, the microsite will fall back gracefully to beautiful, responsive CSS gradient placeholders with built-in loading shimmer animations, ensuring that the layout remains intact and executive-ready.

## How to Verify Layout

1.  Open the [index.html](file://<REPO_ROOT>/campaigns/football-summer-2026/html-preview/index.html) file locally in any browser.
2.  Inspect the slots. The placeholders should display with warm Vietjet-themed gradients and labels.
3.  Once you place any generated image inside `assets/`, refresh the page; the image will automatically fade in smoothly, replacing its placeholder card.
4.  Verify that all images conform to the IP/copyright governance constraints listed below.
