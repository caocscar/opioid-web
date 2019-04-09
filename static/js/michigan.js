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
      .on("click", d => { 
        window.location.href += d.properties.name + "/" + src
      })
      $(function () {
        $('[data-toggle="tooltip"]').tooltip()
      })
};

