RECIPE_BASE_URL = "http://127.0.0.1:8000";

$("#RandomRecipeButton").click(function (event) {
    $.getJSON(RECIPE_BASE_URL + '/recipes/random/', {

    }).done(function (data) {
        $("#RecipeName").text(data.name);
    });
});

function populateTable() {
    $.getJSON(RECIPE_BASE_URL + '/recipes/', {

    }).done(function (data) {
        $('table').bootstrapTable({
            data: data
        });
        $("table").linkify();
    });
}

$(document).ready(function () {
    populateTable();
});