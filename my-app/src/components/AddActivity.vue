class="form-control"<template>
  <main style="margin-top: 58px">
    <div class="container pt-4">
      <div class="container pt-4">
        <form>
          <div class="form-group-row">
            <label>Title :</label>
            <input type="title" v-model="title" class="form-control" required />
          </div>
          <div class="form-group-row">
            <label>Date :</label>
            <input type="date" class="form-control" required />
          </div>
          <div class="form-group-row">
            <label>distance :</label>
            <input type="distance" class="form-control" />
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
            <input
              v-model="start_at"
              type="datetime-local"
              class="form-control"
            />

            <label>End At:</label>
            <input
              v-model="end_at"
              type="datetime-local"
              class="form-control"
            />
          </div>
          <div class="form-group-row">
            <label>note:</label>
            <input v-model="note" type="textarea" class="form-control" />
          </div>

          <div class="button mt-3">
            <button
              class="submit btn btn-primary mb-2"
              v-on:click.prevent="handleSubmit()"
              type="submit"
            >
              Add
            </button>
          </div>
        </form>
      </div>
    </div>
  </main>
</template>

<script>
import axios from "axios";
export default {
  name: "AddActivity",
  data() {
    return {
      title: "",
      distance: 0,
      activity_type: 0,
      note: "",
      start_at: "",
      end_at: "",
    };
  },
  methods: {
    handleSubmit() {
      const data = {
        title: this.title,
        distance: Number(this.distance),
        start_at: this.start_at,
        end_at: this.end_at,
        note: this.note,
        activity_type: Number(this.activity_type),
      };

      axios
        .post("http://127.0.0.1:5000/v1/activity/", data, {
          headers: {
            accept: "application/json",
            "Content-Type": "application/json",
            Authorization:
              "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU0MzA0NCwianRpIjoiYjA2NDJiMTUtMDE2My00MjIyLWExYTktYTdlOTViZjU2OGJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjY0NTQzMDQ0fQ.gSNC1plwVRu-lFa65yVdzPZmLUOxrdZ_ItltiHY1hoM",
          },
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (err) {
          console.log(err);
        });
    },
  },
};
</script>
<style lang="">
</style>