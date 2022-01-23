RECIPE_BASE_URL = "http://127.0.0.1:8000";

// $("#RecipeButton").click(function (event) {
//     $.getJSON(RECIPE_BASE_URL + '/recipes/', {

//     }).done(function (data) {
//         console.log(data);
//     });
// });


$("#RandomRecipeButton").click(function (event) {
    $.getJSON(RECIPE_BASE_URL + '/recipes/random/', {

    }).done(function (data) {
        $("#RecipeName").text(data.name);
        console.log(data.name);
        console.log(data);
    });
});