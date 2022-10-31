<template lang="">
    <div>
      <!--Main layout-->
     
      <main style="margin-top: 58px">
        <div class="container pt-4">
          <section class="mb-4">
            <div class="card">
              <div class="card-header text-center py-3">
                <h5 class="mb-0 text-center">
                  <strong>All Activity</strong>
                </h5>
              </div>
            </div>
          </section>
        <section>
            <div class="card-body">
              <div class="table-responsive">
                <table class="table table-hover text-nowrap">
                  <thead>
                    <tr>
                      <th scope="col"></th>
                      <th scope="col">Title</th>
                      <th scope="col">Date</th>
                      <th scope="col">Start Time</th>
                      <th scope="col">End Time</th>
                      <th scope="col">Km</th>
                    </tr>
                  </thead>
                  <tbody>
                  <tr v-for="(inf, index) in info"  :key="inf.id">
                      <td>{{index}}</td>
                      <td><a href="/ViewActvity/"> {{inf.title}} </a></td>
                      <td>{{inf.date}}</td>
                      <td>{{inf.start_at}}</td>
                      <td>{{inf.end_at}}</td>
                      <td>{{inf.distance}}</td>
                    </tr>
              
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        </div>
      </main>
    </div>
  </template>
  <script>
  import axios from 'axios';
  export default {
      name:'AllActivity'
      ,
    data () {
      return {
        info: null
      }
    },
    mounted () {
      axios
        .get('http://127.0.0.1:5000/v1/activity/',
        {
       headers: {
      "accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU0MzA0NCwianRpIjoiYjA2NDJiMTUtMDE2My00MjIyLWExYTktYTdlOTViZjU2OGJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjY0NTQzMDQ0fQ.gSNC1plwVRu-lFa65yVdzPZmLUOxrdZ_ItltiHY1hoM" },}
        )
        .then(response => { this.info = response.data.data.activities; console.log(this.info)})
    }
  
  }
  </script>
  <style lang="">
      
  </style>