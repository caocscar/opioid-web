function generateRep(){

if (globalCity.length > 0){
  location.href = "/dashboard?src=" + globalDataSource + "&city=" +  globalCity + "&T0=" + startTime + "&T1=" + endTime
}
if (globalCounty.length > 0){
  location.href = "/dashboard?src=" + globalDataSource + "&county=" +  globalCounty + "&T0=" + startTime + "&T1=" + endTime
}
}
