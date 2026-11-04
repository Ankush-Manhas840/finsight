# Data sources

All files are the official annual reports, saved in `data/raw/` (not pushed to GitHub).
FY2025 = 1 April 2024 to 31 March 2025.

| File | Company | Year | Pages | Money unit | URL | Downloaded on |
|---|---|---|---|---|---|---|
| `maruti_FY2025.pdf` | Maruti Suzuki India | FY2025 | 254 | ₹ million | [NSE filing](https://nsearchives.nseindia.com/annual_reports/AR_27293_MARUTI_2024_2025_A_05082025210558.pdf) | 2026-11-04 |
| `mahindra_FY2025.pdf` | Mahindra & Mahindra | FY2025 | 249 | ₹ crore | [NSE filing](https://nsearchives.nseindia.com/annual_reports/AR_26638_M%26M_2024_2025_A_28062025232952.pdf) | 2026-11-04 |
| `bajaj_FY2025.pdf` | Bajaj Auto | FY2025 | 300 | ₹ crore | [Bajaj investor site](https://investors.bajajauto.com/ar25/wp-content/uploads/2025/07/BAL_Annual_Report_2025.pdf) | 2026-11-04 |

## Traps to remember

- **Different units:** Maruti reports in ₹ million, Mahindra and Bajaj in ₹ crore. 1 crore = 10 million. Convert before comparing.
- **₹ symbol breaks in text:** in Bajaj's PDF, Python reads "₹ In Crore" as "H In Crore".
- **Extra pages at the start:** the Maruti and Mahindra NSE files begin with a cover letter to the stock exchange and the meeting notice; the report comes after.
- **Both sets of statements:** every report has standalone and consolidated statements.
- The NSE archive blocks automated downloads (503 error); download from a browser.
