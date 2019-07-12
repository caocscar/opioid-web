function navPlace(){
event.preventDefault();

var placeName = document.querySelector("#searchthing").value;
var form = document.querySelector(".formthing");

if(cities.includes(placeName)){
  console.log("True");

  location.href = "/dashboard" + "?src=" + globalDataSource +"&" + "city="+placeName;

}
else{
  console.log("False");
  location.href  = "/dashboard" + "?src="+ globalDataSource + "&" + "county="+placeName;
};

console.log(location.href );
};
