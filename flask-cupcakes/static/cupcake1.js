//const BASE_URL = "http://localhost:5000/api";
const BASE_URL = "http://127.0.0.1:5000/api";

/** put initial cupcakes on page. */
async function showInitialCupcakes() {
  const response = await axios.get(`${BASE_URL}/cupcakes`);
  ccList = $("#cupcakes-list")

  for (let cupcakeData of response.data.cupcakes) {   
    //console.log(cupcakeData.id);
    let cupcakeId = cupcakeData.id;
    let cupcakeFlavor = cupcakeData.flavor;
    //$("#cupcakes-list").append(`<div>hello</div>`)
    $("#cupcakes-list").append(`<div>${cupcakeId}</div>`)

    // let newCupcake = $(generateCupcakeHTML(cupcakeData));
    // $("#cupcakes-list").append(newCupcake);
  }
}
showInitialCupcakes()