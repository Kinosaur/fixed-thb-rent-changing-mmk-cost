#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const root = path.resolve(import.meta.dirname, "..");
const inputPath = path.join(root, "data_public", "myanmar_market_price_monthly_summary.csv");
const outputPath = path.join(root, "workbook", "FX_Exploration.xlsx");

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/);
  const headers = lines[0].split(",");
  return lines.slice(1).map((line) => {
    const values = [];
    let current = "";
    let inQuotes = false;
    for (let index = 0; index < line.length; index += 1) {
      const char = line[index];
      if (char === '"') {
        if (inQuotes && line[index + 1] === '"') {
          current += '"';
          index += 1;
        } else {
          inQuotes = !inQuotes;
        }
      } else if (char === "," && !inQuotes) {
        values.push(current);
        current = "";
      } else {
        current += char;
      }
    }
    values.push(current);
    return Object.fromEntries(headers.map((header, index) => [header, values[index] ?? ""]));
  });
}

function asNumber(value) {
  return Number(value);
}

const csvText = await fs.readFile(inputPath, "utf8");
const rows = parseCsv(csvText);
if (rows.length !== 44) {
  throw new Error(`Expected 44 monthly FX rows; found ${rows.length}.`);
}

const workbook = Workbook.create();
const chartSheet = workbook.worksheets.add("FX Chart");
const dataSheet = workbook.worksheets.add("FX Data");
const guideSheet = workbook.worksheets.add("Read Me");

for (const sheet of [chartSheet, dataSheet, guideSheet]) {
  sheet.showGridLines = false;
}

const navy = "#17365D";
const blue = "#2F75B5";
const lightBlue = "#D9EAF7";
const paleBlue = "#EEF5FB";
const gray = "#595959";
const border = "#D9E2F3";

chartSheet.mergeCells("A1:I1");
chartSheet.getRange("A1").values = [["THB/MMK Sell Rate by Month"]];
chartSheet.getRange("A1:I1").format = {
  fill: navy,
  font: { bold: true, color: "#FFFFFF", size: 16 },
  horizontalAlignment: "center",
  verticalAlignment: "center",
};
chartSheet.getRange("A1:I1").format.rowHeight = 28;

chartSheet.mergeCells("A2:I2");
chartSheet.getRange("A2").values = [["All monthly points retained · start, peak, and latest values highlighted · Sell rate used for MMK → THB cost scenario"]];
chartSheet.getRange("A2:I2").format = {
  fill: paleBlue,
  font: { color: gray, italic: true, size: 10 },
  horizontalAlignment: "center",
  verticalAlignment: "center",
  wrapText: true,
};
chartSheet.getRange("A2:I2").format.rowHeight = 28;

chartSheet.getRange("A4").formulas = [["=\"Start • \"&A9"]];
chartSheet.getRange("B4").formulas = [["=\"Peak • \"&INDEX(A9:A52,MATCH(MAX(B9:B52),B9:B52,0))"]];
chartSheet.getRange("C4").formulas = [["=\"Latest • \"&A52"]];
chartSheet.getRange("A4:C4").format = {
  fill: lightBlue,
  font: { bold: true, color: navy },
  horizontalAlignment: "center",
  wrapText: true,
};
chartSheet.getRange("A4:C4").format.rowHeight = 28;
chartSheet.getRange("A5").formulas = [["=B9"]];
chartSheet.getRange("B5").formulas = [["=MAX(B9:B52)"]];
chartSheet.getRange("C5").formulas = [["=B52"]];
chartSheet.getRange("A5:C5").format.numberFormat = "#,##0.00";
chartSheet.getRange("A5:C5").format = {
  fill: "#FFFFFF",
  horizontalAlignment: "center",
  borders: { preset: "outside", style: "thin", color: border },
};
chartSheet.getRange("A5:B5").format.font = { bold: true, color: navy };

chartSheet.getRange("A8:C8").values = [["Month", "Monthly median Sell rate (MMK per 1 THB)", "Screenshot count"]];
chartSheet.getRange("A8:C8").format = {
  fill: navy,
  font: { bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center",
  wrapText: true,
};

const firstDataRow = 9;
const lastDataRow = firstDataRow + rows.length - 1;
for (let i = 0; i < rows.length; i += 1) {
  const excelRow = firstDataRow + i;
  const sourceRow = 7 + i;
  chartSheet.getRange(`A${excelRow}:C${excelRow}`).formulas = [[
    `='FX Data'!A${sourceRow}`,
    `='FX Data'!F${sourceRow}`,
    `='FX Data'!B${sourceRow}`,
  ]];
}
chartSheet.getRange(`A${firstDataRow}:A${lastDataRow}`).format.numberFormat = "@";
chartSheet.getRange(`B${firstDataRow}:B${lastDataRow}`).format.numberFormat = "#,##0.00";
chartSheet.getRange(`C${firstDataRow}:C${lastDataRow}`).format.numberFormat = "#,##0";
chartSheet.getRange(`A${firstDataRow}:C${lastDataRow}`).format.borders = {
  preset: "insideHorizontal",
  style: "thin",
  color: "#E7EEF7",
};

chartSheet.mergeCells("E27:M31");
chartSheet.getRange("E27").values = [[
  "Source: Myanmar Market Price (https://www.myanmarmarketprice.com/). Values were manually transcribed from user-supplied dated app screenshots and summarized as the median of available observations in each month. Sell rate is used for the user's MMK-to-THB cost scenario. This is not an official or complete daily-rate series.",
]];
chartSheet.getRange("E27:M31").format = {
  fill: paleBlue,
  font: { color: gray, size: 9 },
  wrapText: true,
  verticalAlignment: "top",
  borders: { preset: "outside", style: "thin", color: border },
};

chartSheet.getRange("A1:M31").format.font = { name: "Aptos", size: 10 };
chartSheet.getRange("A1:I1").format.font = { bold: true, color: "#FFFFFF", size: 16 };
chartSheet.getRange("A1:C5").format.borders = { preset: "outside", style: "thin", color: border };
chartSheet.getRange("A1").format.columnWidth = 23;
chartSheet.getRange("B1").format.columnWidth = 33;
chartSheet.getRange("C1").format.columnWidth = 18;
chartSheet.getRange("D1").format.columnWidth = 4;
chartSheet.getRange("E1:M1").format.columnWidth = 13;
chartSheet.freezePanes.freezeRows(8);

const dataHeaders = [
  "Observation month",
  "Screenshot count",
  "First observation date",
  "Last observation date",
  "Buy median (MMK per THB)",
  "Sell median (MMK per THB)",
  "Midpoint median (MMK per THB)",
  "Median spread (MMK per THB)",
  "Quality status",
  "Coverage note",
];
dataSheet.mergeCells("A1:J1");
dataSheet.getRange("A1").values = [["Myanmar Market Price — Public Monthly Screenshot Sample"]];
dataSheet.getRange("A1:J1").format = {
  fill: navy,
  font: { bold: true, color: "#FFFFFF", size: 14 },
  horizontalAlignment: "center",
};
dataSheet.getRange("A3").values = [["Source website"]];
dataSheet.getRange("B3").values = [["https://www.myanmarmarketprice.com/"]];
dataSheet.getRange("A4").values = [["Method"]];
dataSheet.getRange("B4").values = [["Monthly median of supplied dated screenshot observations; Sell is the selected personal cost scenario."]];
dataSheet.getRange("A3:A4").format = { fill: lightBlue, font: { bold: true, color: navy } };
dataSheet.getRange("A3:B4").format.borders = { preset: "outside", style: "thin", color: border };
dataSheet.getRange("A6:J6").values = [dataHeaders];
dataSheet.getRange("A6:J6").format = {
  fill: navy,
  font: { bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center",
  wrapText: true,
};
dataSheet.getRange(`A7:J${6 + rows.length}`).values = rows.map((row) => [
  row.observation_month,
  asNumber(row.observation_count),
  row.first_observation_date,
  row.last_observation_date,
  asNumber(row.buy_mmk_per_thb_median),
  asNumber(row.sell_mmk_per_thb_median),
  asNumber(row.midpoint_mmk_per_thb_median),
  asNumber(row.median_spread_mmk_per_thb),
  row.quality_status,
  row.coverage_note,
]);
dataSheet.getRange(`B7:B${6 + rows.length}`).format.numberFormat = "#,##0";
dataSheet.getRange(`E7:H${6 + rows.length}`).format.numberFormat = "#,##0.00";
dataSheet.getRange(`A7:J${6 + rows.length}`).format.borders = { preset: "insideHorizontal", style: "thin", color: "#E7EEF7" };
dataSheet.getRange("A1:A1").format.columnWidth = 15;
dataSheet.getRange("B1:B1").format.columnWidth = 14;
dataSheet.getRange("C1:D1").format.columnWidth = 16;
dataSheet.getRange("E1:H1").format.columnWidth = 17;
dataSheet.getRange("I1:I1").format.columnWidth = 27;
dataSheet.getRange("J1:J1").format.columnWidth = 58;
dataSheet.freezePanes.freezeRows(6);
dataSheet.tables.add(`A6:J${6 + rows.length}`, true, "FxMonthlySampleTable");

const chart = chartSheet.charts.add("line", chartSheet.getRange(`A8:B${lastDataRow}`));
chart.title = "MMK needed for 1 THB — Monthly Median Sell Rate";
chart.hasLegend = false;
chart.setPosition("E4", "M25");

guideSheet.mergeCells("A1:H1");
guideSheet.getRange("A1").values = [["How to Read This Workbook"]];
guideSheet.getRange("A1:H1").format = {
  fill: navy,
  font: { bold: true, color: "#FFFFFF", size: 14 },
  horizontalAlignment: "center",
};
guideSheet.getRange("A3:B7").values = [
  ["What this chart shows", "How the monthly median Myanmar Market Price Sell rate changed over time."],
  ["Why Sell", "The user confirmed Sell is the rate used when converting MMK to THB."],
  ["Why median", "Each month may have several screenshots. The median reduces the influence of one unusually high or low observation."],
  ["Screenshot count", "The number of screenshot observations used that month. A count of 1 is still an observation, but has less within-month coverage."],
  ["What it cannot show", "It cannot prove a new-tenant condo price or an official daily exchange-rate series."],
];
guideSheet.getRange("A3:A7").format = { fill: lightBlue, font: { bold: true, color: navy }, wrapText: true };
guideSheet.getRange("B3:B7").format = { wrapText: true, verticalAlignment: "top" };
guideSheet.getRange("A3:B7").format.borders = { preset: "all", style: "thin", color: border };
guideSheet.getRange("A1:A1").format.columnWidth = 25;
guideSheet.getRange("B1:B1").format.columnWidth = 92;
guideSheet.getRange("A3:B7").format.rowHeight = 34;

await fs.mkdir(path.dirname(outputPath), { recursive: true });
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);

const tableCheck = await workbook.inspect({
  kind: "table",
  range: "FX Chart!A1:C12",
  include: "values,formulas",
  tableMaxRows: 12,
  tableMaxCols: 3,
});
console.log(tableCheck.ndjson);
const errorCheck = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "formula error scan",
});
console.log(errorCheck.ndjson);
for (const sheetName of ["FX Chart", "FX Data", "Read Me"]) {
  const preview = await workbook.render({ sheetName, autoCrop: "all", scale: 1.5, format: "png" });
  const previewPath = `/private/tmp/fx_exploration_${sheetName.replaceAll(" ", "_")}.png`;
  await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));
  console.log(`Rendered ${previewPath}`);
}
console.log(`Created ${outputPath}`);
