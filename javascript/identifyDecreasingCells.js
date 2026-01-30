/**
 * Gemini prompt: Write a Google sheets macro that will identify all
 * cells in a column that are not greater than or equal to the cell
 * directly above.
 *
 * Follow on prompt: Handle dates as well as numbers.
 * Identifies cells smaller than the one above, handling numbers and dates.
 * Highlights cells in light red.
 *
 */
function identifyDecreasingCells() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const range = sheet.getActiveRange();
  const values = range.getValues();
  const backgrounds = range.getBackgrounds();

  for (let i = 1; i < values.length; i++) {
    let curr = values[i][0];
    let prev = values[i-1][0];

    // Helper to convert dates to numbers, or keep numbers as they are
    let currVal = (curr instanceof Date) ? curr.getTime() : curr;
    let prevVal = (prev instanceof Date) ? prev.getTime() : prev;

    // Check if both are valid for comparison (not empty strings or nulls)
    if (currVal !== "" && prevVal !== "" && currVal !== null && prevVal !== null) {
      if (currVal < prevVal) {
        backgrounds[i][0] = "#f4cccc"; // Highlight Red
      } else {
        backgrounds[i][0] = null; // Clear Highlight
      }
    }
  }

  range.setBackgrounds(backgrounds);
}
