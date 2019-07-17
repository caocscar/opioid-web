function navPlace(){
  var placeName = document.querySelector("#searchthing").value;
  event.preventDefault();
  if(cities.includes(placeName)){

    globalCity = placeName;
    mapUpdateOnSearch(placeName);
    previous = placeName;
    // console.log(globalCity);
  } else if (counties.includes(placeName)) {
    globalCounty = placeName;
    mapUpdateOnSearch(placeName);
    previous = placeName;
    // console.log(globalCounty);
  } else {
    document.querySelector("#searchthing").value = "INVALID NAME";
  }
};

var previous=""

function mapUpdateOnSearch(nameFromSearch){
  if (cities.includes(nameFromSearch)){
    let cases = ['Kalamazoo (City)', 'Saginaw (City)', 'Muskegon (City)'];
    if (cases.includes(nameFromSearch)) {
      let cityName = nameFromSearch.split(" (City)")[0];
      var selectedPlaceCity= document.querySelector("#" + cityName.replace(/\s+/g,"_").replace(/\./g, '_')+"_city");
    } else {
      var selectedPlaceCity = document.querySelector("#" + nameFromSearch.replace(/\s+/g,"_").replace(/\./g, '_'));
    }
    selectedPlaceCity.classList.add("focused");
    if (!(previous === "")){
      // previous has a name in it

      // previous is a case
      if (cases.includes(previous)) {
        fixedName = previous.split(" (City)")[0];

        document.querySelector("#" + fixedName.replace(/\s+/g,"_").replace(/\./g, '_')+"_city").classList.remove("focused");
      } else {
        document.querySelector("#" + previous.replace(/\s+/g,"_").replace(/\./g, '_')).classList.remove("focused");
      }
    }
  };
  if (counties.includes(nameFromSearch)){
    let cases = ['Kalamazoo (City)', 'Saginaw (City)', 'Muskegon (City)'];

    let selectedPlaceCounty = document.querySelector("#" + nameFromSearch.replace(/\s+/g,"_").replace(/\./g, '_'));
    selectedPlaceCounty.classList.add("focused");

    if (!(previous === "")){
      if (cases.includes(previous)) {
        fixedName = previous.split(" (City)")[0];
        document.querySelector("#" + fixedName.replace(/\s+/g,"_").replace(/\./g, '_')+"_city").classList.remove("focused");
      } else {
        document.querySelector("#" + previous.replace(/\s+/g,"_").replace(/\./g, '_')).classList.remove("focused");
      };
    }
  }
};
