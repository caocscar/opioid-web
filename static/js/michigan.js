let width = 550;
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

let ONE = d3.select(".onemap")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

// Load topojson data
async function make_map(svgname) {
  // Append Div for tooltip to SVG
  let tooltipDiv = d3.select(".onemap")
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
      .attr('class','county')
      .attr("d", path)
      .attr("id", d => d.properties.name.replace(/\s+/g,"_").replace(/\./g, '_'))
      .attr("data-toggle", "tooltip")
      .attr("title", d => d.properties.name)
      .on('click', function(d) {
        let element = this;
        focus_on_citycounty(element);
        globalCounty = d.properties.name;
        previous = globalCounty;
        document.querySelector("#searchthing").value = d.properties.name;
        })
      $(function() {
        $('[data-toggle="tooltip"]').tooltip()
      })

    svgname.selectAll('circle')
      .data(cities)
      .enter().append('circle')
        .attr('class', 'city')
        .attr("id", d => {
          array = ['Kalamazoo', 'Saginaw', 'Muskegon']
          if (array.includes(d.name)) {
            return d.name.replace(/\s+/g,"_").replace(/\./g, '_')+"_city"
          }
          else{
            return d.name.replace(/\s+/g,"_").replace(/\./g, '_')
          }
        })
        .attr('r', '4')
        .attr("data-toggle", "tooltip")
        .attr('cx', d => projection([d.lng,d.lat])[0])
        .attr('cy', d => projection([d.lng,d.lat])[1])
        .attr("title", d => d.name)
        .on('click', function(d) {
          let element = this
          focus_on_citycounty(element);
          globalCity = d.name;
          previous = globalCity;
          document.querySelector("#searchthing").value = d.name;
          })
        $(function() {
          $('[data-toggle="tooltip"]').tooltip()
        })

  function focus_on_citycounty(element){
    //https://jaketrent.com/post/d3-class-operations/
    const activeClass = "focused";
    const alreadyIsActive = d3.select(element).classed(activeClass);
    svgname.selectAll('.city, .county')
      .classed(activeClass, false);
    d3.select(element).classed(activeClass, !alreadyIsActive);
  };

};


function type(d) {
    d.lat = +d.lat;
    d.lng = +d.lng;
    return d
};
