//http://www.daterangepicker.com/

$(function() {

    var start = moment().subtract(13, 'days');
    var end = moment();

    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        startTime = formatDate(start);
        endTime = formatDate(end);
    }

    $('#reportrange').daterangepicker({

        startDate: start,
        endDate: end,
        ranges: {
           'Last 7 Days': [moment().subtract(6, 'days'), moment()],
           'Last 14 Days': [moment().subtract(13, 'days'), moment()],
           'Last Month': [moment().subtract(1, 'month').add(1, 'days'), moment()],
           'Last 3 Months': [moment().subtract(3, 'month').add(1, 'days'), moment()],
           'Year-to-Date' : [moment().startOf('year'), moment()]
        }
    }, cb);

    cb(start, end);

    // https://stackoverflow.com/questions/23593052/format-javascript-date-to-yyyy-mm-dd
    function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('');
}

});
