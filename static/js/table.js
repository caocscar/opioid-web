async function makeTable(tableName, fileName) {
    data = await d3.csv(fileName);
    table = d3.select("#" + tableName)
    thead = table.append('thead').append('tr')
      .selectAll('th')
      .data(data.columns)
      .join('th')
        .text(d => d);
    tbody = table.append('tbody');
    rows = tbody.selectAll('tr')
        .data(data)
        .join('tr')

    rows.selectAll('td')
        .data((d) => d3.values(d))
        .join('td')
        .text((d,i) => i > 0 ? d : d)
};


async function makeFreqTable(tableName, fileName) {
    data = await d3.csv(fileName);
    table = d3.select("#" + tableName)
    thead = table.append('thead').append('tr')
      .selectAll('th')
      .data(data.columns)
      .join('th')
        .text(d => d);
    tbody = table.append('tbody');
    rows = tbody.selectAll('tr')
        .data(data)
        .join('tr')

    rows.selectAll('td')
        .data((d) => d3.values(d))
        .join('td')
        .text((d,i) => i > 0 ? d : d)
};


async function makeMeanTable(tableName, fileName) {
    data = await d3.csv(fileName);
    table = d3.select("#MeanAndChange")
    thead = table.append('thead').append('tr')
      .selectAll('th')
      .data(data.columns)
      .join('th')
        .text(d => d);
    tbody = table.append('tbody');
    rows = tbody.selectAll('tr')
        .data(data)
        .join('tr')

    rows.selectAll('td')
        .data((d) => d3.values(d))
        .join('td')
        .text((d,i) => i > 0 ? d : d)
        .attr("style", (d, i) => i & 1 ? colorCode(d) : d)
        .html((d, i) => i & 1 ? arrowDirection(d) : d)
};

function colorCode(d){
    if ( d >= 20){
      return 'color: #92140c';
    }
    else if (d <= -20){
     return 'color: #001B56';
    }
    else {
      return 'color: black';
    }
};

function arrowDirection(d){
  if (d >= 20){
    return d + "%" +' <i class= "fa fa-arrow-up"></i>';
  }
  else if (d <= -20){
    return d + "%" +' <i class= "fa fa-arrow-down"></i>';
  }
  else{
    return d + "%" + ' <i class= "fa fa-arrow-right"></i>';
  }
};
  // color and arrow based on whether or not number is between, greater or equal than 0.2, or less than or equal to -0.2
