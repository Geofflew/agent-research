# Poland KAS: API and daily flat file of the VAT taxpayers register (white list)

URL: https://www.gov.pl/web/kas/api-wykazu-podatnikow-vat
Type: standard
Read in session: 0008B

Summary: Ministry of Finance / KAS page on machine access to the VAT taxpayer register that ties bank accounts to NIP. The "check" API answers YES/NO on whether an account is assigned to a NIP on a date; a flat file of hashed NIP-account pairs is published daily for bulk checks in finance systems. Quotas: "search" 100 queries/day of up to 30 entities; "check" 5000 entities; WL2 50,000 queries/day. Production host migrates 15 Oct 2026 (old host served to 1 Dec 2026).

Quotes:
- "zawiera pełną listę par NIP-rachunek, co pozwala na masową weryfikację transakcji w systemach finansowo-księgowych" — gov.pl KAS, on the flat file published since Nov 2019
- "TAK lub NIE – informacje, które oznaczają, że dany rachunek przypisany jest (lub nie jest) do wyspecyfikowanego numeru podmiotu" — gov.pl KAS, on the "check" method
- "Dane do pobrania są publikowane codziennie i aktualizowane raz na dobę w dni robocze." — gov.pl KAS, on the flat file
- "przy wykorzystaniu metody „search” możesz złożyć 100 zapytań dziennie o maksymalnie 30 podmiotów jednocześnie" — gov.pl KAS, on API limits
- "w przypadku API WL2 limit ten wynosi 50 000 zapytań na dzień" — gov.pl KAS, on API limits
