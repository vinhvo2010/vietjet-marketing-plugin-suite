---
title: "Vietjet Delivery Standard"
trigger: always_on
version: 5.0
---

# CHUẨN BÀN GIAO: MISSION → EVIDENCE → DECISION → RELEASE → LEARN

Đây là quy trình chung cho mọi specialist và workflow. Nó áp dụng tinh thần của gstack — vai trò rõ, đầu ra nối tiếp, kiểm tra độc lập và bàn giao có bằng chứng — vào môi trường marketing hàng không. Đây không phải tiêu chuẩn chính thức hay sự chứng thực của Y Combinator.

## 1. Chuỗi trạng thái công việc

| Trạng thái | Câu hỏi phải trả lời | Đầu ra tối thiểu |
|---|---|---|
| `MISSION` | Quyết định kinh doanh hoặc thay đổi hành vi nào cần đạt, trong scope nào? | Mission Brief hợp lệ, outcome, người sở hữu và thời hạn |
| `EVIDENCE` | Điều gì đã biết, chưa biết và cần kiểm chứng? | Evidence ledger có nguồn, ngày, nhãn dữ liệu |
| `PLAN` | Phương án hẹp nhất tạo giá trị là gì? | Lựa chọn khuyến nghị, trade-off, dependency |
| `DRAFT` | Tài sản hoặc quyết định nháp trông như thế nào? | Bản nháp dùng được, không chỉ danh sách ý tưởng |
| `REVIEW` | Điều gì có thể sai khi vận hành thật? | Kiểm tra chuyên môn, pháp lý, dữ liệu, thương hiệu |
| `RELEASE` | Ai được quyền phát hành và bằng chứng duyệt ở đâu? | Trạng thái `READY`, `BLOCKED` hoặc `DRAFT ONLY` |
| `LEARN` | Kết quả làm thay đổi quyết định tiếp theo thế nào? | Learning Record có effect, giới hạn, owner và next decision |

Không bỏ qua trạng thái vì “đang gấp”. Có thể rút gọn tài liệu, không được rút gọn cổng an toàn.

## 2. Evidence ledger bắt buộc

Mỗi đầu ra có claim, số liệu hoặc khuyến nghị phải duy trì bảng:

| Claim / input | Nhãn | Nguồn | Ngày kiểm chứng | Chủ sở hữu | Hạn dùng |
|---|---|---|---|---|---|

- Phân biệt rõ `OBSERVED` (đã quan sát), `INFERENCE` (suy luận) và `PROPOSAL` (đề xuất).
- Mọi số liệu tiếp tục dùng ba nhãn tại `vietjet-data-integrity.md`; ledger không thay thế nhãn trong nội dung.
- Nguồn web phải là nguồn công khai, đáng tin cậy; không vượt anti-bot, không phụ thuộc dữ liệu reach không công khai.
- Khi nguồn không có hoặc đã hết hạn, ghi `không công khai / không xác minh được`, không suy diễn thành dữ kiện.

## 3. Cổng chất lượng

Trước bàn giao, specialist tự kiểm:

1. Outcome có gắn với quyết định kinh doanh, không chỉ vanity metric.
2. Operating entity, point of sale, source market hoặc route corridor đã được khai báo đúng.
3. Claim, con số, luật, giá, lịch bay và đội tàu có nguồn/ngày/nhãn phù hợp.
4. Công thức và giả định có thể kiểm tra lại.
5. One-Way Door có cờ chờ duyệt và tên vai trò phê duyệt.
6. Nội dung có PII, phát ngôn an toàn, chi tiền hoặc phát hành công khai chưa bị thực thi tự động.
7. File đầu ra đã chạy `python3 scripts/check_output.py <path>` khi có thể.

## 4. Hợp đồng bàn giao

Mọi báo cáo cuối phải kết thúc bằng:

- `STATUS`: `READY` / `PARTIAL` / `BLOCKED_INPUT` / `BLOCKED_APPROVAL` / `ESCALATED`.
- `DECISION`: quyết định cần người dùng hoặc BOD đưa ra.
- `EVIDENCE`: nguồn đã xác thực trong phiên và các khoảng trống.
- `OUTPUT`: artifact hoặc nội dung cụ thể được bàn giao.
- `APPROVALS`: người/đơn vị cần duyệt trước khi phát hành hoặc chi tiền.
- `NEXT`: hành động tiếp theo hẹp nhất, có người sở hữu.

`READY` chỉ có nghĩa là sẵn sàng cho bước được nêu; không bao giờ ngầm nghĩa là đã được phép phát hành, chi tiền hay thay đổi hệ thống thật.

<!-- check-output: rules-doc -->
