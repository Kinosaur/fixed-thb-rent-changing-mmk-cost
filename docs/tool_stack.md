# Mac-First Tool Stack

Use one tool per job. More tools will not make this project stronger.

| Need | Use | Do not add yet |
|---|---|---|
| Learn analytical thinking | DuckDB SQL | A cloud warehouse or multiple database systems |
| Review data / quick one-off chart | Excel for Mac | Power BI Desktop |
| Build a portfolio visual | Tableau Public locally, then publish only public-safe data | Tableau Prep or a second BI product |
| Automate and reproduce | Python + pandas | R, unless a course or target job specifically requires it |
| Show your work safely | GitHub with the current `.gitignore` | Private PDFs, screenshots, or raw rows |

## Why this fits a Mac

Power BI Desktop requires Windows, so it is not an efficient primary tool for this Mac project. Tableau supports Mac and Apple Silicon, and Tableau Public is suitable for learning and public portfolios. Save locally while working with private data: a Tableau Public publication makes the workbook and data publicly accessible.

DuckDB is already available through the local Python environment. DBeaver is optional—not a second skill to master—if a visual SQL editor helps you write and run queries.

## Why Python before R

Current Thailand and Taiwan analyst-job examples commonly ask for SQL, Python, and a dashboard tool such as Tableau, Power BI, or Looker. Some roles list R too, but learning Python and R together now would dilute practice time. Add R only if a course, professor, or specific target job requires it.

## Minimum portfolio stack

1. One SQL file with clear queries.
2. One Tableau story with a transparent source/method note.
3. One Python notebook or script that reproduces a result.
4. One concise README explaining the question, method, result, limits, and privacy choices.
