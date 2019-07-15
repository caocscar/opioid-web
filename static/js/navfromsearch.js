function navPlace(){
event.preventDefault();

var placeName = document.querySelector("#searchthing").value;
var form = document.querySelector(".formthing");

if(cities.includes(placeName)){

  location.href = "/dashboard" + "?src=" + globalDataSource +"&" + "city="+placeName + "&T0=" + startTime + "&T1=" + endTime;

}
else if(counties.includes(placeName)){
  location.href  = "/dashboard" + "?src="+ globalDataSource + "&" + "county="+placeName + "&T0=" + startTime + "&T1=" + endTime;
}
else{
  alert("Invalid Location");
}
};
