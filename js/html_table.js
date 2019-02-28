async function make_html_table(filename, tableid) {
  const data = await d3.csv(filename);
  var floatFormat = d3.format(',.0f')
  var pctFormat = d3.format('+,.0%')
  
  var table = d3.select('#' + tableid)
    .append('table')
    .style('text-align','center');
  var headers = table.append('thead').append('tr')
    .selectAll('th')
      .data(data.columns)
    .enter().append('th')
    .text(d => d)

  if (tableid == 'summary') {
    table.append('tbody').selectAll('tr')
        .data(data)
      .enter().append('tr')
      .selectAll('td')
        .data(d => d3.values(d) ).enter()
      .append('td')
      .text((d,i) => i === 1 ? pctFormat(d) : floatFormat(d) );
  }else if (tableid == 'events') {
    table.append('tbody').selectAll('tr')
        .data(data)
      .enter().append('tr')
      .selectAll('td')
        .data(d => d3.values(d) )
      .enter().append('td')
      .text((d,i) => d);
    table.attr('class','table table-striped table-bordered')
      .attr('width', 500);

  }
};