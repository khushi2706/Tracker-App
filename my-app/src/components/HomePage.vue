<template lang="">
  <div>
    <!--Main layout-->
    <main style="margin-top: 58px">
      <div class="container pt-4">
        <!--Section: Sales Performance KPIs-->
        <section class="mb-4">
          <div class="card">
            <div class="card-header text-center py-3">
              <h5 class="mb-0 text-center">
                <strong>Your Weekly Report</strong>
              </h5>
            </div>
          </div>
        </section>
        <!--Section: Sales Performance KPIs-->

        <!--Section: Minimal statistics cards-->
        <section>
          <div class="row">
            <div class="col-xl-3 col-sm-6 col-12 mb-4">
              <div class="card">
                <div class="card-body">
                  <div class="d-flex justify-content-between px-md-1">
                    <div class="align-self-center">
                      <i class="fas fa-bicycle text-info fa-3x"></i>
                    </div>
                    <div class="text-end">
                      <h3>278</h3>
                      <p class="mb-0">Total Ride</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-sm-6 col-12 mb-4">
              <div class="card">
                <div class="card-body">
                  <div class="d-flex justify-content-between px-md-1">
                    <div class="align-self-center">
                      <i class="far fa-clock text-warning fa-3x"></i>
                    </div>
                    <div class="text-end">
                      <h3>156</h3>
                      <p class="mb-0">Total Hours</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-sm-6 col-12 mb-4">
              <div class="card">
                <div class="card-body">
                  <div class="d-flex justify-content-between px-md-1">
                    <div class="align-self-center">
                      <i class="fas fa-chart-line text-success fa-3x"></i>
                    </div>
                    <div class="text-end">
                      <h3>64.89 Km</h3>
                      <p class="mb-0">Total Distance</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!--Section: Minimal statistics cards-->

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
                  <tr>
                    <td>1</td>
                    <td>Value</td>
                    <td>27/6/2022</td>
                    <td>10:20</td>
                    <td>12:30</td>
                    <td>55</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>Value</td>
                    <td>27/6/2022</td>
                    <td>10:20</td>
                    <td>12:30</td>
                    <td>55</td>
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
export default {
  name: "HomePage",
};
</script>
<style lang=""></style>
