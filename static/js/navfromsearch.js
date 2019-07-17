function navPlace(){
event.preventDefault();

var placeName = document.querySelector("#searchthing").value;
var form = document.querySelector(".formthing");

if(cities.includes(placeName)){

  globalCity = placeName;
  // console.log(globalCity);
}
else if(counties.includes(placeName)){
  globalCounty = placeName;
  // console.log(globalCounty);
}
else{
  alert("Invalid Location");
}
};
