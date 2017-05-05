function onEdit() {
  // column f has dates and you want to color column b based on those dates
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  var date_range = sheet.getRange('f2:f30');
  var amount_range = sheet.getRange('b2:b30');
  var num_rows = date_range.getNumRows();
  // Logger.log(num_rows);
  var date_values = date_range.getValues();
  // Logger.log(date_values);
  for (var i = 0; i <= num_rows -1; i++) {
    var n = i + 2;
    var curDate = new Date(date_values[i][0]);
    // Logger.log(date_values[i]);
    // Logger.log(curDate);
    if ((curDate.getDate()     == 24) &&
        (curDate.getMonth()    == 4)  && // Enum -> Month - 1
        (curDate.getFullYear() == 2013)) {
      sheet.getRange('b'+n).setBackgroundColor('green');
    } else {
      sheet.getRange('b'+n).setBackgroundColor('none');
    }
  }
}
