# Data sources

All files are the official annual reports, saved in `data/raw/` (not pushed to GitHub).
FY2025 = 1 April 2024 to 31 March 2025.

| File | Company | Year | Pages | Money unit | URL | Downloaded on |
|---|---|---|---|---|---|---|
| `maruti_FY2025.pdf` | Maruti Suzuki India | FY2025 | 254 | ₹ million | [NSE filing](https://nsearchives.nseindia.com/annual_reports/AR_27293_MARUTI_2024_2025_A_05082025210558.pdf) | 2026-11-04 |
| `mahindra_FY2025.pdf` | Mahindra & Mahindra | FY2025 | 249 | ₹ crore | [NSE filing](https://nsearchives.nseindia.com/annual_reports/AR_26638_M%26M_2024_2025_A_28062025232952.pdf) | 2026-11-04 |
| `bajaj_FY2025.pdf` | Bajaj Auto | FY2025 | 300 | ₹ crore | [Bajaj investor site](https://investors.bajajauto.com/ar25/wp-content/uploads/2025/07/BAL_Annual_Report_2025.pdf) | 2026-11-04 |
| `maruti_FY2024.pdf` | Maruti Suzuki India | FY2024 | 252 | ₹ million | [NSE filing](https://nsearchives.nseindia.com/annual_reports/AR_26250_MARUTI_2023_2024_26092024102330.pdf) | 2026-11-07 |
| `mahindra_FY2024.pdf` | Mahindra & Mahindra | FY2024 | 268 | ₹ crore | [NSE filing](https://nsearchives.nseindia.com/annual_reports/AR_24243_M%26M_2023_2024_29062024183812.pdf) | 2026-11-07 |
| `bajaj_FY2024.pdf` | Bajaj Auto | FY2024 | 340 | ₹ crore | [NSE filing](https://nsearchives.nseindia.com/annual_reports/AR_24163_BAJAJ-AUTO_2023_2024_2106202418557.pdf) | 2026-11-07 |
| `maruti_FY2023.pdf` | Maruti Suzuki India | FY2023 | 226 | ₹ million | [NSE filing (zip)](https://nsearchives.nseindia.com/annual_reports/AR_22663_MARUTI_2022_2023_05082023185748_08052023190000.zip) | 2026-11-07 |
| `mahindra_FY2023.pdf` | Mahindra & Mahindra | FY2023 | 474 | ₹ crore | [NSE filing (zip)](https://nsearchives.nseindia.com/annual_reports/AR_22135_M%26M_2022_2023_03072023013854_07032023070001.zip) | 2026-11-07 |
| `bajaj_FY2023.pdf` | Bajaj Auto | FY2023 | 315 | ₹ crore | [NSE filing (zip)](https://nsearchives.nseindia.com/annual_reports/AR_22141_BAJAJ-AUTO_2022_2023_03072023160735_07032023170006.zip) | 2026-11-07 |

FY2024 = 1 April 2023 to 31 March 2024. FY2023 = 1 April 2022 to 31 March 2023.

**How the FY2023 and FY2024 files were downloaded:** NSE lists every company's reports at `https://www.nseindia.com/api/annual-reports?index=equities&symbol=<SYMBOL>` (symbols `MARUTI`, `M%26M`, `BAJAJ-AUTO`). The list must be requested with a normal browser user agent and a `Referer: https://www.nseindia.com/` header; the archive files then download normally. FY2023 reports come as **zip files** holding one PDF each.

**Also available:** FY2026 reports (published June to August 2026) are already listed on NSE. Not downloaded yet; the plan covers FY2023 to FY2025.

## Traps to remember

- **Different units:** Maruti reports in ₹ million, Mahindra and Bajaj in ₹ crore. 1 crore = 10 million. Convert before comparing.
- **₹ symbol breaks in text:** in Bajaj's PDF, Python reads "₹ In Crore" as "H In Crore".
- **Extra pages at the start:** the Maruti and Mahindra NSE files begin with a cover letter to the stock exchange and the meeting notice; the report comes after.
- **Both sets of statements:** every report has standalone and consolidated statements.
- The NSE archive blocked a plain automated download (503 error) on 2026-11-04. Using NSE's report list with browser-like headers (see above) worked on 2026-11-07.
- **Mahindra FY2023 is much longer** (474 pages, against 249 to 268 in other years), so expect more pages to search.
