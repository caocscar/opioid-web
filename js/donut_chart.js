async function make_donut_chart(filename, column) {
  const data = await d3.csv(filename)

  var margin = {top: 10, right: 10, bottom: 10, left: 20},
      width = 400 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom + 50,
      radius = Math.min(width, height) / 2;
  
  n = column == 'Age' ? 0 : column == 'Gender' ? 6 : 8
  var color = d3.schemePaired.slice(n);

  var pie = d3.pie()
      .value(d => d.value)
      .sort(null);

  var arc = d3.arc()
      .innerRadius(radius - 100)
      .outerRadius(radius - 20);

  var svg = d3.select("." + column).append("svg")
      .attr("width", width)
      .attr("height", height)
    .append("g")
      .attr("transform", "translate(" + width/2 + "," + height/2 + ")");

  // arc slice
  var path = svg.datum(data).selectAll("path")
      .data(pie)
    .enter().append("path")
      .attr("fill", (d,i) => (color[i]) )
      .attr("d", arc);

  // label placement
  var text = svg.datum(data).selectAll('text')
      .data(pie)
    .enter().append('text')
      .attr('transform', d => 'translate(' + arc.centroid(d) + ')')
      .attr('dy','0.35em')
  
  // label line 1
  text.filter(d => d.data.value > 0)
    .append("tspan")
      .attr("x", 0)
      .attr("y", "-0.7em")
      .style("font-weight", "bold")
      .style('text-anchor', 'middle')
      .text(d => d.data.index);
  
  // label line 2
  var total = 0
  text.filter(d => d.data.value > 0.25)
    .append("tspan")
      .attr("x", 0)
      .attr("y", "1.0em")
      .style('text-anchor', 'middle')
      .text(d => {
        total += parseInt(d.data.value)
        return d.data.value
      });
  
  // middle text
  svg.append('text')
      .attr('class', 'toolCircle')
      .attr('dy', '0.35em')
      .text(total) // add text to the circle.
      .style('font-size', '3em')
      .style('text-anchor', 'middle')

  // title
  svg.append('text')
      .attr('class', 'chart_title')
      .attr('x', 0)
      .attr('y', -height/2 + 15)
      .attr('dy', '0.35em')
      .style('font-size', '2em')
      .style("font-weight", 500)
      .style('text-anchor', 'middle')
      .text(column)      

};