<template>
  <div>
    <h1>Add a Movie</h1>
    <form id="movieForm" @submit.prevent="saveMovie">

      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title:</label>
        <input type="text" name="title" class="form-control">
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description:</label>
        <textarea name="description" class="form-control">Give a description of the movie.</textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster:</label>
        <input type="file" name="poster" class="form-control-file" accept="image/jpeg, image/png">
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>

    </form>
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
let csrf_token = ref("");

const router = useRouter();

onMounted(() => { 
    getCsrfToken(); 
}); 

function saveMovie (){
    let movieForm = document.getElementById('movieForm'); 
    let form_data = new FormData(movieForm);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value 
        }
    })
    .then(function (response) { 
        return response.json(); 
    })
    .then(function (data) {
        // Display success message or perform other actions
        console.log(data);
        router.push('/movies/');
    })
    .catch(function (error) {
        console.log(error);
    });
};

function getCsrfToken() { 
    fetch('/api/v1/csrf-token') 
    .then((response) => response.json()) 
    .then((data) => { 
        console.log(data); 
        csrf_token.value = data.csrf_token; 
    }) 
} 

</script>
