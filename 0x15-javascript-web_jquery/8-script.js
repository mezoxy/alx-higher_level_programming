$(document).ready(function(){
    const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
    $.get(url, function(data, status){
        const res = data.results;
        for (const num in res){
            $("UL#list_movies").append("<li>" + res[num].title + "</li>");
        }
    });
});