/**
 * Script for Vietjet Football Summer 2026 Microsite Preview
 * Pure Vanilla JS - No external dependencies
 * Enhanced for Accessibility (WCAG compliant keyboard & screen reader interactions)
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Navigation Highlighting on Scroll
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let currentSectionId = '';
        const scrollPosition = window.scrollY + 120; // offset for sticky header

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });

    // 2. Scenario Interactive Selector
    const scenarioCards = document.querySelectorAll('.scenario-card');
    const dbBudget = document.getElementById('db-budget');
    const dbReach = document.getElementById('db-reach');
    const dbImpressions = document.getElementById('db-impressions');
    const dbBookings = document.getElementById('db-bookings');
    const dbRevenue = document.getElementById('db-revenue');
    const dbConfidence = document.getElementById('db-confidence');
    const dbScenarioName = document.getElementById('db-scenario-name');

    scenarioCards.forEach(card => {
        // Accessibility: Allow activating via keyboard
        card.setAttribute('tabindex', '0');
        card.setAttribute('role', 'button');

        const activateScenario = () => {
            scenarioCards.forEach(c => {
                c.classList.remove('active');
                c.setAttribute('aria-pressed', 'false');
            });
            
            card.classList.add('active');
            card.setAttribute('aria-pressed', 'true');

            // Retrieve data attributes
            const name = card.getAttribute('data-name');
            const budget = card.getAttribute('data-budget');
            const reach = card.getAttribute('data-reach');
            const imps = card.getAttribute('data-impressions');
            const bookings = card.getAttribute('data-bookings');
            const revenue = card.getAttribute('data-revenue');
            const confidence = card.getAttribute('data-confidence');

            // Update DOM
            dbScenarioName.textContent = name;
            dbBudget.textContent = budget;
            dbReach.textContent = reach;
            dbImpressions.textContent = imps;
            dbBookings.textContent = bookings;
            dbRevenue.textContent = revenue;
            dbConfidence.textContent = confidence;

            // Handle confidence color class
            dbConfidence.className = 'dashboard-val confidence-badge';
            if (confidence.toLowerCase().includes('very low')) {
                dbConfidence.classList.add('conf-vlow');
            } else {
                dbConfidence.classList.add('conf-low');
            }
        };

        card.addEventListener('click', activateScenario);
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                activateScenario();
            }
        });
    });

    // 3. Risk Accordion Toggle (for mobile)
    const riskHeaders = document.querySelectorAll('.risk-header');
    
    riskHeaders.forEach(header => {
        // Accessibility: Set ARIA roles and properties
        header.setAttribute('tabindex', '0');
        header.setAttribute('role', 'button');
        header.setAttribute('aria-expanded', 'false');

        const toggleAccordion = () => {
            const riskCard = header.parentElement;
            const isExpanded = riskCard.classList.toggle('expanded');
            header.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
        };

        header.addEventListener('click', toggleAccordion);
        header.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggleAccordion();
            }
        });
    });

    // 4. Copy Summary Clipboard Utility
    const copyBtn = document.getElementById('copy-summary-btn');
    if (copyBtn) {
        copyBtn.addEventListener('click', () => {
            const summaryText = `CHIẾN DỊCH: BAY TỚI MÙA HÈ BÓNG ĐÁ (HÈ 2026)
--------------------------------------------------
Ý tưởng cốt lõi: "Cả mùa hè cùng trái bóng lăn — mình cùng Vietjet bay."
Trạng thái: CONCEPT PREVIEW — NOT PRODUCTION READY

All numbers are assumptions only and not approved targets or forecasts.
Không sao chép hoặc sử dụng số ngân sách, booking, doanh thu, ABV, ROI hay hiệu suất từ preview này.

NGUYÊN TẮC QUẢN TRỊ RỦI RO IP:
- Không sử dụng logo, cúp, mascot hoặc khẩu hiệu chính thức của FIFA/World Cup.
- Không ngụ ý Vietjet là nhà tài trợ hay đối tác chính thức của giải đấu.
- Authorized final launch owner, to be confirmed by policy.

RELEASE BLOCKERS:
- Claim validation required.
- Asset preflight and human QA required.
- Legal/IP, Commercial/Revenue, and Measurement reviews required.
- Missing promised video remains a blocker.`;

            navigator.clipboard.writeText(summaryText).then(() => {
                const originalText = copyBtn.innerHTML;
                copyBtn.innerHTML = `<span>Governance summary copied</span>`;
                copyBtn.style.backgroundColor = '#A85B00';
                
                setTimeout(() => {
                    copyBtn.innerHTML = originalText;
                    copyBtn.style.backgroundColor = ''; // restore CSS color
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy text: ', err);
                alert('Có lỗi khi sao chép thông tin.');
            });
        });
    }

    // 5. Image loading and transition handlers
    const visualImages = document.querySelectorAll('.visual-frame img');
    document.querySelectorAll('.visual-frame').forEach(frame => {
        if (!frame.querySelector('.asset-status-label')) {
            const label = document.createElement('span');
            label.className = 'asset-status-label';
            label.textContent = 'DRAFT AI-GENERATED ASSET — HUMAN QA REQUIRED';
            frame.appendChild(label);
        }
    });
    visualImages.forEach(img => {
        if (img.complete && img.naturalWidth > 0) {
            const frame = img.closest('.visual-frame');
            if (frame) frame.classList.add('loaded');
        } else {
            img.addEventListener('load', () => {
                const frame = img.closest('.visual-frame');
                if (frame) frame.classList.add('loaded');
            });
            img.addEventListener('error', () => {
                handleImageError(img);
            });
        }
    });
});

// Global image error fallback handler
function handleImageError(img) {
    const frame = img.closest('.visual-frame');
    if (frame) {
        frame.classList.add('error');
        frame.classList.remove('loaded');
    }
}
