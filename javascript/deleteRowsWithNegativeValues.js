function deleteRows() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var rows = sheet.getDataRange();
  var numRows = rows.getNumRows();
  var values = rows.getValues();
  /* change this to the column to check
     0 = column A, 1 = column B, etc. */
  var columnToCheck = 1;
  var rowsDeleted = 0;
  for (var i = 0; i <= numRows - 1; i++) {
    var row = values[i];
    if (parseInt(row[columnToCheck]) < 0) {
      sheet.deleteRow(parseInt(i) + 1 - rowsDeleted);
      rowsDeleted++;
    }
  }
}

/**
 * Adds a custom menu to the active spreadsheet, containing a single menu item
 * for invoking the readRows() function specified above.
 * The onOpen() function, when defined, is automatically invoked whenever the
 * spreadsheet is opened.
 * For more information on using the Spreadsheet API, see
 * https://developers.google.com/apps-script/service_spreadsheet
 */
function onOpen() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var entries = [
    {
      name: "Delete Data",
      functionName: "deleteRows",
    },
  ];
  sheet.addMenu("Script Center Menu", entries);
}
