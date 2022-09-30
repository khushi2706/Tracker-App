class="form-control"<template>
  <main style="margin-top: 58px">
      <div class="container pt-4">
      <div class="container pt-4">

        
        <form >
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
            <button class="submit btn btn-primary mb-2 " v-on:click.prevent="handleSubmit()" type="submit">Add</button>
        </div>
</form>
</div>
</div>
</main>
</template>

<script>
  export default {
     name: "AddActivity",
   data() {
        return {
            title: "",
          distance: 0,
          activity_type: 0,
          note: "",
          start_at: "",
          end_at: ""
        }
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