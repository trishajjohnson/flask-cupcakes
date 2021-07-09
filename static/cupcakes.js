const BASE_URL = "http://127.0.0.1:5000/api";

function generateCupcakeHTML(cupcake) {
    return `
        <div data-cupcake-id=${cupcake.id}>
            <img class="cupcake-img" src="${cupcake.image}">
            <li>
                ${cupcake.flavor}  ${cupcake.size}  ${cupcake.rating}
            </li>
        </div>
    `;
}

async function getDisplayCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);

    for(let cupcake of response.data.cupcakes){
        let newCup = $(generateCupcakeHTML(cupcake));
        $("#list-all-cupcakes").append(newCup);
    }
}

$("#add-cupcake-form").on("submit", async function(evt){
    evt.preventDefault();

    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();

    const response = await axios.post(`${BASE_URL}/cupcakes`, {
        "flavor": flavor,
        "size": size,
        "rating": rating,
        "image": image
    });

    let cupcake = generateCupcakeHTML(response.data.cupcake);
    $("#list-all-cupcakes").append(cupcake);
    $("#add-cupcake-form").trigger("reset");
})