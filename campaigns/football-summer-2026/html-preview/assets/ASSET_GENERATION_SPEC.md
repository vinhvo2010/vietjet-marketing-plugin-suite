# Asset Generation Specification

Campaign state: `BLOCKED_ASSET_QA`  
All outputs are draft-only and require human QA. No output may enter `approved/` or `release/` through this workflow.

| # | Required draft asset | MIME | Required ratio | Recommended size | Human QA | Release status |
|---:|---|---|---|---|---|---|
| 1 | `draft/hero-football-travel.jpg` | JPEG | 16:9 | 1920x1080 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 2 | `draft/kv-4x5-football-summer.jpg` | JPEG | 4:5 | 1080x1350 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 3 | `draft/story-9x16-football-travel.jpg` | JPEG | 9:16 | 1080x1920 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 4 | `draft/app-banner-football-summer.jpg` | JPEG | 3:1 | 1800x600 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 5 | `draft/airport-screen-football-summer.jpg` | JPEG | 16:9 | 1920x1080 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 6 | `draft/dashboard-funnel-abstract.jpg` | JPEG | 16:9 | 1920x1080 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 7 | `draft/carousel-01-hook.jpg` | JPEG | 4:5 | 1080x1350 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 8 | `draft/carousel-02-team.jpg` | JPEG | 4:5 | 1080x1350 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 9 | `draft/carousel-03-motion.jpg` | JPEG | 4:5 | 1080x1350 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 10 | `draft/carousel-04-community.jpg` | JPEG | 4:5 | 1080x1350 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 11 | `draft/carousel-05-travel.jpg` | JPEG | 4:5 | 1080x1350 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 12 | `draft/carousel-06-challenge.jpg` | JPEG | 4:5 | 1080x1350 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 13 | `draft/carousel-07-closing.jpg` | JPEG | 4:5 | 1080x1350 | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |
| 14 | `draft/video-8s-football-travel.mp4` | MP4 | 9:16 | 1080x1920, exactly 8 seconds | HUMAN_QA_REQUIRED | DO_NOT_RELEASE |

## Deterministic Requirements

- JPEG magic bytes must match `.jpg`.
- Dimensions and aspect ratio must match the table.
- MP4 must be an actual video file, 9:16, exactly eight seconds.
- Do not fabricate video by renaming or animating a still solely to satisfy preflight.
- Draft assets remain blocked from release until human visual QA and required governance reviews are logged.
