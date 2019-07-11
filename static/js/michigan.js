let width = 250;
let height = width;

//Create SVG element and append map to the SVG
let EMS = d3.select(".mapEMS")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

let ED = d3.select(".mapED")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

let ME = d3.select(".mapME")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

// Load topojson data
async function make_map(svgname, src) {
  // Append Div for tooltip to SVG
  let tooltipDiv = d3.select(".map" + src)
      .append("div")
      .attr("class", "tooltips")
      .attr("data-toggle", "tooltip")
      .attr("data-placement", "top")

  const MItopo = await d3.json('static/geojson/gz_2010_us_050_00_5m_MI_counties.topojson')
  const cities = await d3.csv('static/geojson/cities.csv')
  // convert to geojson
  const MIgeo = topojson.feature(MItopo, MItopo.objects.collection)

  // D3 Projection
  let projection = d3.geoMercator()
      .fitSize([width, height], MIgeo)

  // Define path generator
  let path = d3.geoPath() // path generator that will convert GeoJSON to SVG paths
      .projection(projection);

  // Bind the data to the SVG and create one path per GeoJSON feature
  svgname.selectAll("path")
      .data(MIgeo.features)
    .enter().append("path")
      .attr('class', src+' county')
      .attr("d", path)
      .attr("id", "tooltips")
      .attr("data-toggle", "tooltip")
      .attr("title", d => d.properties.name)
      .on("click", d => window.location.href = "/dashboard?src=" + src + "&county=" + d.properties.name)
      $(function() {
        $('[data-toggle="tooltip"]').tooltip()
      })

    svgname.selectAll('circle')
      .data(cities)
      .enter().append('circle')
        .attr('class', 'city')
        .attr('r', '3')
        .attr("data-toggle", "tooltip")
        .attr('cx', d => projection([d.lng,d.lat])[0])
        .attr('cy', d => projection([d.lng,d.lat])[1])
        .attr("title", d => d.name)
        .on("click", d => window.location.href = "/dashboard?src=" + src + "&city=" + d.name)
        $(function() {
          $('[data-toggle="tooltip"]').tooltip()
        })

  };

  function type(d) {
    d.lat = +d.lat;
    d.lng = +d.lng;
    return d
};
