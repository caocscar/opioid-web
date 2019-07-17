function navPlace(){
  var placeName = document.querySelector("#searchthing").value;
  event.preventDefault();
  if(cities.includes(placeName)){

    globalCity = placeName;
    mapUpdateOnSearch(placeName);
    // console.log(globalCity);
  }
  else if(counties.includes(placeName)){
    globalCounty = placeName;
    mapUpdateOnSearch(placeName);
    // console.log(globalCounty);
  }
  else{
    alert("Invalid Location");
  }
};


function mapUpdateOnSearch(nameFromSearch){
  if (cities.includes(nameFromSearch)){
    let cityName = nameFromSearch.split(" (City)")[0];
    let selectedPlaceCity= document.querySelector("#" + cityName.replace(/\s+/g,"_").replace(/\./g, '_')+"_city");
    selectedPlaceCity.classList.add("focused");
  }
  if (counties.includes(nameFromSearch)){
    let selectedPlaceCounty = document.querySelector("#" + nameFromSearch.replace(/\s+/g,"_").replace(/\./g, '_')+"_county");
    selectedPlaceCounty.classList.add("focused")
  }
  cities_proper=[];
  counties_proper=[];
  for (i = 0 ; i < cities.length; i++){
    var eachCity = cities[i];
    if (eachCity != nameFromSearch){
      if (eachCity.includes("(City)")){
        var properCityName= cities[i].split(" (City)")[0];
        cities_proper.push(properCityName)
      }
      else{
        cities_proper.push(eachCity)
      }
    }
  }
  for (i = 0 ; i < counties.length; i++){
    var eachCounty = counties[i];
    if (eachCounty != nameFromSearch){
      counties_proper.push(eachCounty)
    }
  }

  for (i = 0; i < cities_proper.length; i++){
    var othercities = document.querySelector("#" + cities_proper[i].replace(/\s+/g,"_").replace(/\./g, '_')+"_city");
    othercities.classList.remove("focused");
  }
  for (i = 0 ; i < counties_proper.length; i++){
    var othercounties = document.querySelector("#" + counties_proper[i].replace(/\s+/g,"_").replace(/\./g, '_')+"_county");
    othercounties.classList.remove("focused");
  }
};
