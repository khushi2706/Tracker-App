class="form-control"<template>
  <main style="margin-top: 58px">
      <div class="container pt-4">
      <div class="container pt-4">

        <form class="p-4">
          <div class="form-group-row">
            <label>Title :</label>
            <input type="title" v-model="title" class="form-control"  required>
          </div>
          <div class="form-group-row">
            <label>Date :</label>
            <input type="date"  class="form-control"  required>
          </div>
          <div class="form-group-row">
            <label>distance :</label>  
            <input type="distance" class="form-control" >    
          </div>
          <div class="form-group-row">
            <label>activity_type</label>
            <select v-model="activity_type" class="form-control">
              <option value="0">Walking</option> 
              <option value="1">Cycling</option> 
            </select>
          </div>
          
          <div class="form-group-row">
            
            <label>start at :</label>  
            <input v-model="start_at" class="form-control"> 
            
            <label>End At:</label>  
            <input v-model="end_at"  class="form-control">  
          </div>
          <div class="form-group-row">
            <label>note:</label>  
            <input v-model="note" type="textarea"  class="form-control">  
          </div>

        <div class="button mt-3" >
            <button class="submit btn btn-primary mb-2 " v-on:click.prevent="handleSubmit()" type="submit">Update</button>
        </div>
</form>
</div>
</div>
</main>
</template>

<script>
import axios from "axios"
  export default {
     name: "ViewActivity",
   data() {
        return {
          activity:{
          title: "",
          distance: 0,
          activity_type: 0,
          note: "",
          start_at: "",
          end_at: ""
          }
        }
    },
     mounted () {
    axios
      .get('http://127.0.0.1:5000/v1/activity/1',
      {
     headers: {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU0MzA0NCwianRpIjoiYjA2NDJiMTUtMDE2My00MjIyLWExYTktYTdlOTViZjU2OGJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjY0NTQzMDQ0fQ.gSNC1plwVRu-lFa65yVdzPZmLUOxrdZ_ItltiHY1hoM" },}
      )
      .then(response => { this.activity = response.data.data.activity; console.log(this.info)})
  },
    methods: {
   
        handleSubmit() {
                console.log(this.title);
                console.log(this.start_at);
        }
    }
  }
</script>
<style lang="">
    
</style>