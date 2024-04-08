<script setup> 

import { ref, onMounted } from "vue"; 
let movies = ref([]); 

function fetchMovies(){
    fetch("/api/v1/movies", {
        method: 'GET'
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        movies.value = data.movies;
    })
    .catch(function (error) {
        console.log(error);
    })
}

onMounted(() => { 
    fetchMovies(); 
}); 

</script> 

<template>
<div>
    <h1>All Movies</h1>
    <br>
    <div>
        <div v-for="movie in movies" :key="movie.id" class="movie-card">
            <img :src="'/uploads/' + movie.poster" alt="poster">
            <h3>{{ movie.title }}</h3>
            <p>{{ movie.description }}</p>
        </div>
    </div>
</div>
</template>

<style>
.movie-card img {
  width: 300px;
}
</style>