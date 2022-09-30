<template>
  <main style="margin-top: 58px">
      <div class="container pt-4">
<form >
         <label>Title :</label>
        <input type="title" v-model="title"   required>

        <label>distance :</label>  
        <input type="distance"  >    

        <label>activity_type</label>
        <select v-model="activity_type">
            <option value="0">Walking</option> 
            <option value="1">Cycling</option> 
        </select>

      <label>note:</label>  
        <input v-model="note"  >  
        
        <label>start at :</label>  
        <input v-model="start_at"> 

        <label>End At:</label>  
        <input v-model="end_at" >  

        <div class="button">
            <button class="submit" v-on:click.prevent="handleSubmit()" type="submit">Sign up here</button>
        </div>
</form>
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