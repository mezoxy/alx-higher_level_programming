$(document).ready(function(){
    const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
    $.get(url, function(data, status){
        for (const obj of data.results){
            if "title" in obj{
                $("UL#list_movies").text(obj.title);
            }
        }
      //  $("UL#list_movies").text(data.results);
        //data.results[0].title
    });
});