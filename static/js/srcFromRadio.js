function updateGlobal() {
  var emsButton = document.querySelector("#EMSRadio");
  // console.log(emsButton);

  var edButton = document.querySelector("#EDRadio");
  // console.log(edButton);

  var meButton = document.querySelector("#MERadio");
  // console.log(meButton);

if (emsButton.checked){
  globalDataSource = emsButton.value;
  // console.log(globalDataSource);
}

if (edButton.checked){
  globalDataSource = edButton.value;
  // console.log(globalDataSource);
}

if (meButton.checked){
  globalDataSource = meButton.value;
  // console.log(globalDataSource);
}

}
