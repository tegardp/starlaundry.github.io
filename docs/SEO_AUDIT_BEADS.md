# SEO & Technical Audit Report — starlaundry-byl.com
**Audit Date:** 10 Maret 2026
**Domain:** starlaundry-byl.com
**Hosting:** GitHub Pages (Static HTML)

---

## SITEMAP — Discovered Pages

| # | URL | Status | Type |
|---|-----|--------|------|
| 1 | `/` (index.html) | Live | Homepage |
| 2 | `/tentang-kami.html` | Live | About Us |
| 3 | `/kontak.html` | Live | Contact |
| 4 | `/syarat-ketentuan.html` | Live | Terms & Conditions |
| 5 | `/kebijakan-privasi.html` | Live | Privacy Policy |
| 6 | `/robots.txt` | **404 MISSING** | Technical |
| 7 | `/sitemap.xml` | **404 MISSING** | Technical |

---

## SEO AUDIT SUMMARY

### Per-Page Analysis

#### Homepage (index.html)
- **Title:** "Star Laundry Boyolali — Bersih Wangi, Pasti Rapi" (50 chars) ✅
- **Meta Desc:** 164 chars (slightly over 160 limit) ⚠️
- **H1:** "Bersih Wangi, Pasti Rapi" (1 H1) ✅
- **H2:** 6 headings, good hierarchy ✅
- **Content:** ~1,200-1,400 words ✅
- **Canonical:** MISSING ❌
- **OG Tags:** MISSING ❌
- **JSON-LD:** MISSING ❌
- **Images:** 2 images, no lazy loading, no width/height ❌
- **logo.png:** 91KB (oversized) ❌
- **mesin.jpg alt:** "Foto Mesin Logo" (misleading) ❌

#### Tentang Kami
- **Title:** "Tentang Kami — Star Laundry Boyolali" (37 chars) ✅
- **Meta Desc:** 138 chars ✅
- **Content:** ~350 words (**THIN**) ❌
- **Canonical/OG/JSON-LD:** ALL MISSING ❌

#### Kontak
- **Title:** "Kontak — Star Laundry Boyolali" (31 chars) ✅
- **Meta Desc:** 118 chars ✅
- **Content:** ~200 words (**VERY THIN**) ❌
- **Embedded Map:** MISSING ❌
- **Contact Form:** MISSING ❌
- **Operating Hours:** "Buka Setiap Hari" (no specific times) ❌
- **Street Address:** MISSING (only "Boyolali, Jawa Tengah") ❌

#### Syarat & Ketentuan
- **Title:** 44 chars ✅
- **Meta Desc:** 89 chars (short) ⚠️
- **Content:** ~1,200 words ✅

#### Kebijakan Privasi
- **Title:** 43 chars ✅
- **Meta Desc:** 115 chars ✅
- **Content:** ~1,200 words ✅

---

### Technical Issues

| Severity | Issue | Pages |
|----------|-------|-------|
| CRITICAL | robots.txt missing (404) | Site-wide |
| CRITICAL | sitemap.xml missing (404) | Site-wide |
| CRITICAL | No JSON-LD structured data | All 5 pages |
| CRITICAL | No canonical tags | All 5 pages |
| CRITICAL | No analytics/tracking | All 5 pages |
| CRITICAL | No street address (local SEO killer) | All pages |
| HIGH | No Open Graph tags | All 5 pages |
| HIGH | No Twitter Card tags | All 5 pages |
| HIGH | All CSS inline (~540 lines, not cacheable) | All 5 pages |
| HIGH | No image lazy loading | All 5 pages |
| HIGH | No image width/height (CLS issue) | All images |
| HIGH | logo.png 91KB (oversized) | All 5 pages |
| MEDIUM | Homepage logo not wrapped in `<a>` tag | index.html |
| MEDIUM | mesin.jpg alt text misleading | index.html |
| MEDIUM | No Google Search Console verification | Site-wide |
| MEDIUM | No preload/prefetch hints | All 5 pages |
| LOW | Pricelist.jpeg unreferenced | Dead asset |
| LOW | Copyright year hardcoded to 2026 | All pages |

---

### Local SEO Grade: D (Poor)

| Signal | Status |
|--------|--------|
| Business name consistency | ⚠️ Mixed ("Star Laundry" vs "Star Laundry Boyolali") |
| Street address | ❌ MISSING — only "Boyolali, Jawa Tengah" |
| Phone (NAP) | ✅ Consistent: 0822-2567-2756 |
| Operating hours (specific) | ❌ Only "Buka Setiap Hari" |
| Embedded Google Map | ❌ Only external link |
| Google Business Profile link | ❌ MISSING |
| LocalBusiness schema | ❌ MISSING |
| Service area definition | ❌ Vague |
| Customer reviews/testimonials | ❌ MISSING |
| Local content (neighborhood targeting) | ❌ MISSING |

---

### Content Gaps

| Gap | Impact |
|-----|--------|
| No service-specific landing pages | Can't rank for "self service laundry Boyolali", "laundry antar jemput Boyolali", etc. |
| No dedicated pricing page | Can't capture "harga laundry Boyolali" searches |
| No FAQ page/section | Missing FAQ schema, missing informational search capture |
| No blog/articles | No long-tail keyword capture |
| No testimonials/reviews | No social proof, no Review schema |
| No gallery page | No visual trust-building content |
| Thin about page (~350 words) | Weak authority signal |
| Thin contact page (~200 words) | Weak local relevance signal |

---

### Keyword Opportunities

| Keyword | Intent | Priority | Current Page |
|---------|--------|----------|-------------|
| laundry Boyolali | Local discovery | HIGH | Homepage (weak) |
| harga laundry Boyolali | Price comparison | HIGH | None — need /harga.html |
| laundry kiloan Boyolali | Service type | HIGH | None — need landing page |
| self service laundry Boyolali | Service type | HIGH | None — need /self-service.html |
| laundry antar jemput Boyolali | Service type | HIGH | None — need /antar-jemput.html |
| laundry express Boyolali | Urgency search | HIGH | None — need landing page |
| laundry murah Boyolali | Price-sensitive | HIGH | None |
| jasa cuci baju Boyolali | Generic local | HIGH | Homepage |
| laundry terdekat | Local discovery | HIGH | None |
| cuci setrika Boyolali | Service specific | MEDIUM | Homepage section only |
| laundry selimut Boyolali | Niche service | MEDIUM | None |
| laundry sepatu Boyolali | Niche service | MEDIUM | None |
| laundry koin Boyolali | Self-service | MEDIUM | None |
| dry cleaning Boyolali | Premium service | MEDIUM | None |
| tips mencuci pakaian | Informational | MEDIUM | None — need blog |
| cara menghilangkan noda | Informational | MEDIUM | None — need blog |
| laundry hotel Boyolali | B2B | LOW | None |
| cuci gorden Boyolali | Niche | LOW | None |

---

## BEADS BACKLOG

---

### CRITICAL — Do Immediately

---

**BEAD-001**
- **Title:** Create robots.txt
- **Type:** SEO
- **Priority:** Critical
- **Description:** Create a robots.txt file with proper crawl directives. Currently returns 404.
- **Acceptance Criteria:**
  - robots.txt accessible at /robots.txt
  - Allow all crawlers
  - Reference sitemap.xml URL
  - Block sensitive paths if any
- **Technical Notes:**
```
User-agent: *
Allow: /
Sitemap: https://starlaundry-byl.com/sitemap.xml
```

---

**BEAD-002**
- **Title:** Create XML Sitemap
- **Type:** SEO
- **Priority:** Critical
- **Description:** Create sitemap.xml listing all public pages with lastmod dates and priority values. Currently returns 404.
- **Acceptance Criteria:**
  - sitemap.xml accessible at /sitemap.xml
  - Lists all 5 current pages (and future pages)
  - Includes lastmod, changefreq, priority
  - Valid per sitemap protocol
- **Technical Notes:** Static XML file. Update manually when adding new pages or use a generator.

---

**BEAD-003**
- **Title:** Add LocalBusiness JSON-LD Schema to All Pages
- **Type:** SEO
- **Priority:** Critical
- **Description:** Implement JSON-LD structured data using schema.org/Laundromat (subtype of LocalBusiness) on all pages. This is the single most impactful SEO fix for local visibility.
- **Acceptance Criteria:**
  - JSON-LD `<script type="application/ld+json">` in `<head>` of all pages
  - Schema type: Laundromat (or LocalBusiness)
  - Includes: name, url, telephone, address (full street), geo (lat/lng), openingHoursSpecification, image, priceRange, sameAs (Instagram, WhatsApp)
  - Passes Google Rich Results Test
- **Technical Notes:**
```json
{
  "@context": "https://schema.org",
  "@type": "Laundromat",
  "name": "Star Laundry Boyolali",
  "url": "https://starlaundry-byl.com",
  "telephone": "+6282225672756",
  "image": "https://starlaundry-byl.com/logo.png",
  "priceRange": "Rp 5.000 - Rp 13.000/kg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[FULL STREET ADDRESS]",
    "addressLocality": "Boyolali",
    "addressRegion": "Jawa Tengah",
    "postalCode": "[POSTAL CODE]",
    "addressCountry": "ID"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[LAT]",
    "longitude": "[LNG]"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
      "opens": "[HH:MM]",
      "closes": "[HH:MM]"
    }
  ],
  "sameAs": [
    "https://instagram.com/starlaundry.boyolali"
  ]
}
```

---

**BEAD-004**
- **Title:** Add Canonical Tags to All Pages
- **Type:** SEO
- **Priority:** Critical
- **Description:** Add self-referencing canonical tags to prevent duplicate content issues.
- **Acceptance Criteria:**
  - Every page has `<link rel="canonical" href="https://starlaundry-byl.com/[page]">`
  - Homepage canonical: `https://starlaundry-byl.com/`
  - Other pages: full absolute URL
- **Technical Notes:** Add to `<head>` of all 5 pages.

---

**BEAD-005**
- **Title:** Add Full Street Address Sitewide
- **Type:** SEO
- **Priority:** Critical
- **Description:** The site currently only shows "Boyolali, Jawa Tengah" — no street address. Google cannot place the business in local pack results without a specific address. Add the complete address (Jalan, kelurahan, kecamatan, kode pos) to all pages.
- **Acceptance Criteria:**
  - Full street address displayed on homepage footer, kontak.html, tentang-kami.html
  - Matches Google Business Profile address exactly
  - Consistent across all pages (NAP consistency)
- **Technical Notes:** Owner must provide the actual street address.

---

**BEAD-006**
- **Title:** Install Google Analytics 4 (GA4)
- **Type:** SEO
- **Priority:** Critical
- **Description:** No analytics tracking is installed. Cannot measure traffic, conversions, or user behavior.
- **Acceptance Criteria:**
  - GA4 tracking code installed on all 5 pages
  - Pageview tracking working
  - WhatsApp click events tracked as conversions
  - Real-time data visible in GA4 dashboard
- **Technical Notes:** Add GA4 gtag.js snippet to `<head>`. Consider GTM for future flexibility.

---

**BEAD-007**
- **Title:** Set Up Google Search Console
- **Type:** SEO
- **Priority:** Critical
- **Description:** No Search Console verification detected. Needed for indexing monitoring, search performance data, and sitemap submission.
- **Acceptance Criteria:**
  - Site verified in Google Search Console
  - Verification meta tag added to homepage `<head>`
  - sitemap.xml submitted
  - Index coverage report reviewed
- **Technical Notes:** Use HTML meta tag verification method.

---

### HIGH IMPACT

---

**BEAD-008**
- **Title:** Add Open Graph Tags to All Pages
- **Type:** SEO
- **Priority:** High
- **Description:** No Open Graph tags exist. When links are shared on WhatsApp, Facebook, or other platforms, there's no controlled preview image or description.
- **Acceptance Criteria:**
  - Every page has: og:title, og:description, og:image, og:url, og:type, og:locale
  - og:image is at least 1200x630px
  - og:locale set to "id_ID"
  - Validates with Facebook Sharing Debugger
- **Technical Notes:**
```html
<meta property="og:title" content="Star Laundry Boyolali — Bersih Wangi, Pasti Rapi">
<meta property="og:description" content="Laundry modern dengan dryer profesional & setrika uap. Self service mulai 10rb. Antar jemput GRATIS!">
<meta property="og:image" content="https://starlaundry-byl.com/og-image.jpg">
<meta property="og:url" content="https://starlaundry-byl.com/">
<meta property="og:type" content="website">
<meta property="og:locale" content="id_ID">
```
Need to create an OG image (1200x630px) featuring logo + tagline.

---

**BEAD-009**
- **Title:** Extract Inline CSS to External Stylesheet
- **Type:** Performance
- **Priority:** High
- **Description:** ~540 lines of CSS are duplicated inline in every page's `<style>` tag. This means the CSS is re-downloaded with every page load and cannot be browser-cached.
- **Acceptance Criteria:**
  - Shared CSS extracted to `/styles.css`
  - All 5 pages reference `<link rel="stylesheet" href="styles.css">`
  - Page-specific CSS (if any) kept minimal inline or in separate files
  - No visual regressions
- **Technical Notes:** Browser will cache styles.css after first load, reducing subsequent page sizes by ~15-20KB each.

---

**BEAD-010**
- **Title:** Optimize Images (logo.png, mesin.jpg)
- **Type:** Performance
- **Priority:** High
- **Description:** logo.png is 91KB (should be <20KB for a logo). No images use lazy loading or explicit dimensions.
- **Acceptance Criteria:**
  - logo.png converted to WebP or optimized PNG (<20KB), or replaced with SVG
  - mesin.jpg optimized and served in WebP format
  - All `<img>` tags have `width` and `height` attributes (prevents CLS)
  - Below-fold images have `loading="lazy"`
  - All images have descriptive alt text
- **Technical Notes:**
  - Fix mesin.jpg alt from "Foto Mesin Logo" to "Mesin cuci kapasitas 20kg Star Laundry Boyolali"
  - Consider using `<picture>` element with WebP + PNG fallback

---

**BEAD-011**
- **Title:** Embed Google Maps on Contact Page
- **Type:** SEO / Feature
- **Priority:** High
- **Description:** Contact page only has an external link to Google Maps with a generic query. An embedded map iframe with the business's actual Place ID improves local SEO signals.
- **Acceptance Criteria:**
  - Google Maps iframe embedded on kontak.html
  - Uses Place ID (not generic query)
  - Map centered on the actual outlet location
  - Responsive (works on mobile)
  - Also embedded or linked on homepage location section
- **Technical Notes:** Get Place ID from Google Maps, use iframe embed code.

---

**BEAD-012**
- **Title:** Add Specific Operating Hours
- **Type:** SEO
- **Priority:** High
- **Description:** Current hours only say "Buka Setiap Hari" with no specific open/close times. Google needs structured hours for local pack display.
- **Acceptance Criteria:**
  - Specific open/close times displayed on kontak.html and homepage
  - Hours included in LocalBusiness JSON-LD schema (openingHoursSpecification)
  - Consistent across all pages and Google Business Profile
- **Technical Notes:** Owner must provide actual operating hours.

---

**BEAD-013**
- **Title:** Create Dedicated Pricing Page (/harga.html)
- **Type:** SEO / Feature
- **Priority:** High
- **Description:** No dedicated pricing page exists. "harga laundry Boyolali" is a high-intent search keyword with no landing page to capture it.
- **Acceptance Criteria:**
  - New page at /harga.html
  - Title: "Harga Laundry Star Laundry Boyolali — Daftar Harga Lengkap"
  - Complete pricing for all services (kiloan, self-service, drop-off)
  - Includes Pricelist.jpeg image (currently unreferenced)
  - FAQ section with pricing-related questions
  - Offer/PriceSpecification schema
  - Added to navigation, footer, and sitemap
- **Technical Notes:** Target keywords: "harga laundry Boyolali", "harga laundry per kg", "harga laundry kiloan Boyolali"

---

**BEAD-014**
- **Title:** Create FAQ Page with FAQ Schema
- **Type:** SEO / Feature
- **Priority:** High
- **Description:** No FAQ content exists. FAQ schema enables rich results (expandable Q&A) in Google search, significantly increasing click-through rate.
- **Acceptance Criteria:**
  - New page at /faq.html OR FAQ section added to homepage
  - Minimum 10 Q&As covering: pricing, turnaround time, service area, self-service process, payment methods, garansi cuci ulang, pickup delivery area, paket bulanan, etc.
  - FAQPage JSON-LD schema implemented
  - Passes Google Rich Results Test
  - Added to navigation and sitemap
- **Technical Notes:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Berapa harga laundry per kg di Star Laundry?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mulai dari Rp 5.000/kg untuk cuci lipat 1 hari..."
      }
    }
  ]
}
```

---

**BEAD-015**
- **Title:** Create Service Landing Pages
- **Type:** SEO / Feature
- **Priority:** High
- **Description:** All services are only listed on the homepage. Each service needs its own dedicated landing page to rank for service-specific keywords.
- **Acceptance Criteria:**
  - `/self-service.html` — targeting "self service laundry Boyolali"
  - `/antar-jemput.html` — targeting "laundry antar jemput Boyolali"
  - `/cuci-setrika.html` — targeting "cuci setrika Boyolali", "laundry kiloan Boyolali"
  - Each page: 500+ words, unique title/meta, service details, pricing, CTA, schema
  - Added to navigation, footer, and sitemap
- **Technical Notes:** Each page should target 2-3 keyword variations. Include internal links to pricing page and WhatsApp CTA.

---

### MEDIUM IMPACT

---

**BEAD-016**
- **Title:** Add Twitter Card Meta Tags
- **Type:** SEO
- **Priority:** Medium
- **Description:** No Twitter Card tags on any page. Limits sharing preview on Twitter/X.
- **Acceptance Criteria:**
  - All pages have: twitter:card, twitter:title, twitter:description, twitter:image
  - Card type: summary_large_image
- **Technical Notes:**
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Star Laundry Boyolali">
<meta name="twitter:description" content="Laundry modern...">
<meta name="twitter:image" content="https://starlaundry-byl.com/og-image.jpg">
```

---

**BEAD-017**
- **Title:** Standardize Business Name (NAP Consistency)
- **Type:** SEO
- **Priority:** Medium
- **Description:** Business name is inconsistent: "Star Laundry" (logo, headings) vs "Star Laundry Boyolali" (titles, schema). Pick one and use it everywhere.
- **Acceptance Criteria:**
  - Decide canonical business name (recommend: "Star Laundry Boyolali")
  - Update all references across all pages
  - Match Google Business Profile name exactly
- **Technical Notes:** Consistent NAP is a fundamental local SEO ranking factor.

---

**BEAD-018**
- **Title:** Expand Tentang Kami Page Content
- **Type:** SEO / Content
- **Priority:** Medium
- **Description:** Currently only ~350 words. Thin content signals low-quality to Google.
- **Acceptance Criteria:**
  - Expand to 800+ words
  - Add: founding story, team/staff, facility details, service area description, mission
  - Add photos of outlet, team, facilities
  - Include local keywords naturally
- **Technical Notes:** Focus on E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness).

---

**BEAD-019**
- **Title:** Expand Kontak Page Content
- **Type:** SEO / Content
- **Priority:** Medium
- **Description:** Currently only ~200 words with no embedded map or contact form.
- **Acceptance Criteria:**
  - Expand to 500+ words
  - Add embedded Google Maps iframe
  - Add specific operating hours
  - Add service area description with nearby landmarks
  - Add directions from key locations (e.g., "5 menit dari Alun-alun Boyolali")
  - Consider adding simple contact form
- **Technical Notes:** Rich contact pages with maps and detailed info improve local SEO signals.

---

**BEAD-020**
- **Title:** Wrap Homepage Logo in Anchor Tag
- **Type:** Bug
- **Priority:** Medium
- **Description:** On index.html, the navbar logo `<img>` is not wrapped in an `<a>` tag, unlike all other pages where it links to index.html.
- **Acceptance Criteria:**
  - Homepage logo wrapped in `<a href="index.html">`
  - Consistent behavior across all pages
- **Technical Notes:** Line 551 of index.html.

---

**BEAD-021**
- **Title:** Add Customer Testimonials Section
- **Type:** Feature / SEO
- **Priority:** Medium
- **Description:** No social proof on the website. No customer reviews or testimonials displayed.
- **Acceptance Criteria:**
  - Testimonials section on homepage (3-5 reviews)
  - Optional dedicated testimonials page
  - Review schema (AggregateRating) on homepage
  - Include customer name, rating, and review text
- **Technical Notes:** Can pull from Google Maps reviews (with attribution) or collect directly.

---

**BEAD-022**
- **Title:** Create Blog Section for Informational Content
- **Type:** Feature / SEO
- **Priority:** Medium
- **Description:** No informational content exists. A blog targeting educational keywords ("tips mencuci pakaian", "cara menghilangkan noda") can drive organic traffic.
- **Acceptance Criteria:**
  - Blog index page at `/blog.html` or `/artikel.html`
  - Individual blog post pages
  - Article schema on each post
  - Minimum 3 initial articles (500+ words each)
  - Internal links to service/pricing pages
  - Added to navigation and sitemap
- **Technical Notes:** Suggested initial articles from MARKETING_BLUEPRINT.md content ideas.

---

**BEAD-023**
- **Title:** Add Breadcrumb Schema and Navigation
- **Type:** SEO
- **Priority:** Medium
- **Description:** No breadcrumb navigation or schema exists. Breadcrumbs improve navigation UX and can appear in Google search results.
- **Acceptance Criteria:**
  - Visual breadcrumb navigation on all subpages (not homepage)
  - BreadcrumbList JSON-LD schema on all subpages
  - Format: Beranda > [Page Name]
- **Technical Notes:**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Beranda", "item": "https://starlaundry-byl.com/"},
    {"@type": "ListItem", "position": 2, "name": "Kontak"}
  ]
}
```

---

**BEAD-024**
- **Title:** Add hreflang Tag for Indonesian Language
- **Type:** SEO
- **Priority:** Medium
- **Description:** No hreflang tag present. While the site is Indonesian-only, an hreflang signals regional targeting to Google.
- **Acceptance Criteria:**
  - `<link rel="alternate" hreflang="id" href="...">` on all pages
- **Technical Notes:** Helps with geo-targeting in Google Search.

---

**BEAD-025**
- **Title:** Display Pricelist Image on Website
- **Type:** Content
- **Priority:** Medium
- **Description:** Pricelist.jpeg (72KB) exists in the repo but is not linked from any page. This visual pricelist should be shown on the pricing or homepage.
- **Acceptance Criteria:**
  - Pricelist.jpeg displayed on harga.html (when created) or homepage pricing section
  - Proper alt text: "Daftar Harga Star Laundry Boyolali"
  - Lazy loaded, optimized
- **Technical Notes:** Could serve as a downloadable/shareable pricelist image.

---

### NICE TO HAVE

---

**BEAD-026**
- **Title:** Add Resource Preload Hints
- **Type:** Performance
- **Priority:** Low
- **Description:** No resource hints exist. Preloading critical assets (logo, fonts) can improve perceived load time.
- **Acceptance Criteria:**
  - `<link rel="preload" as="image" href="logo.png">` for above-fold logo
  - Consider preloading any fonts if added in future
- **Technical Notes:** Only preload resources that are immediately needed for above-fold content.

---

**BEAD-027**
- **Title:** Create Service Area Pages (Neighborhood Targeting)
- **Type:** SEO / Content
- **Priority:** Low
- **Description:** No location-specific pages exist beyond generic "Boyolali". Creating pages targeting specific kecamatan/neighborhoods can capture hyper-local searches.
- **Acceptance Criteria:**
  - Landing pages for key areas: "Laundry di Pulisen", "Laundry dekat Kampus", etc.
  - Each page: unique content, area-specific info, directions, embedded map
  - 300+ words each
- **Technical Notes:** Only create if the business actually serves these areas. Avoid doorway pages.

---

**BEAD-028**
- **Title:** Add WhatsApp Click Tracking
- **Type:** Feature
- **Priority:** Low
- **Description:** WhatsApp CTAs are the primary conversion action but clicks are not tracked.
- **Acceptance Criteria:**
  - GA4 event tracking on all WhatsApp link clicks
  - Event name: "whatsapp_click"
  - Track which CTA was clicked (hero, navbar, floating, footer, etc.)
  - Set up as conversion event in GA4
- **Technical Notes:** Use `onclick` event or GTM click trigger.

---

**BEAD-029**
- **Title:** Dynamic Copyright Year in Footer
- **Type:** Improvement
- **Priority:** Low
- **Description:** Footer copyright year is hardcoded to "2026". Will become outdated.
- **Acceptance Criteria:**
  - Year dynamically generated via JavaScript
  - `new Date().getFullYear()`
- **Technical Notes:** Minor but prevents annual maintenance.

---

**BEAD-030**
- **Title:** Add Gallery/Portfolio Page
- **Type:** Feature
- **Priority:** Low
- **Description:** No visual content showcasing the business facilities, equipment, or results. Only mesin.jpg exists.
- **Acceptance Criteria:**
  - Gallery page at `/galeri.html`
  - Photos of: outlet exterior/interior, machines, dryers, ironing process, folded laundry, delivery service
  - All images optimized, lazy loaded, with descriptive alt text
  - ImageGallery schema
- **Technical Notes:** Builds trust and provides visual content for social sharing.

---

## PRIORITY MATRIX

### 🔴 Critical (Do This Week)
| BEAD | Task | Impact |
|------|------|--------|
| 001 | Create robots.txt | Crawl directives |
| 002 | Create sitemap.xml | Indexing |
| 003 | Add LocalBusiness JSON-LD | Local pack ranking |
| 004 | Add canonical tags | Duplicate content prevention |
| 005 | Add full street address | Local SEO fundamental |
| 006 | Install GA4 | Measurement |
| 007 | Set up Search Console | Indexing & monitoring |

### 🟠 High Impact (Do Within 2 Weeks)
| BEAD | Task | Impact |
|------|------|--------|
| 008 | Add Open Graph tags | Social sharing |
| 009 | Extract CSS to external file | Page speed / caching |
| 010 | Optimize images | Core Web Vitals (CLS, LCP) |
| 011 | Embed Google Maps | Local SEO signal |
| 012 | Add specific operating hours | Local pack display |
| 013 | Create pricing page /harga.html | Capture high-intent keyword |
| 014 | Create FAQ page with schema | Rich results in SERP |
| 015 | Create service landing pages | Service keyword rankings |

### 🟡 Medium Impact (Do Within 1 Month)
| BEAD | Task | Impact |
|------|------|--------|
| 016 | Twitter Card tags | Social sharing |
| 017 | Standardize business name | NAP consistency |
| 018 | Expand tentang-kami content | Content quality signal |
| 019 | Expand kontak page | Local SEO signal |
| 020 | Fix homepage logo link | Navigation consistency |
| 021 | Add testimonials section | Trust / Review schema |
| 022 | Create blog section | Long-tail traffic |
| 023 | Add breadcrumb schema | SERP enhancement |
| 024 | Add hreflang tag | Geo-targeting |
| 025 | Display Pricelist image | Content completeness |

### 🟢 Nice to Have (Backlog)
| BEAD | Task | Impact |
|------|------|--------|
| 026 | Resource preload hints | Minor performance |
| 027 | Service area pages | Hyper-local SEO |
| 028 | WhatsApp click tracking | Conversion measurement |
| 029 | Dynamic copyright year | Maintenance reduction |
| 030 | Gallery page | Visual trust / content |

---

## KEYWORD STRATEGY SUMMARY

### Primary Keywords (Homepage + Pricing Page)
- laundry Boyolali
- harga laundry Boyolali
- laundry kiloan Boyolali
- laundry murah Boyolali

### Service Keywords (Service Landing Pages)
- self service laundry Boyolali
- laundry antar jemput Boyolali
- laundry express Boyolali
- cuci setrika Boyolali
- jasa cuci baju Boyolali

### Long-Tail / Informational (Blog)
- tips mencuci pakaian
- cara menghilangkan noda baju
- bedanya laundry kiloan dan satuan
- cara merawat baju agar awet

### Local Modifiers (All Pages)
- laundry terdekat [area]
- laundry dekat [landmark]
- laundry di Pulisen / [neighborhood]
