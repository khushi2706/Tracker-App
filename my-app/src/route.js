import { createWebHistory, createRouter } from "vue-router";

import HomePage from "./components/HomePage.vue"
import AllActivity from "./components/AllActivity"
import AddActivity from "./components/AddActivity"
import ViewActvity from "./components/ViewActvity"

const routes = [{
    path: "/",
    name: "Home",
    component: HomePage,
},
{
    path: "/AllActivity",
    name: "AllActivity",
    component: AllActivity
},
{
    path : "/AddActivity",
    name: "AddActivity",
    component: AddActivity
},
{
    path:"/ViewActvity",
    name:"ViewActivity",
    component:ViewActvity
}
// {
//     path: "/AddActivity",
//     name: "AddActivity",
//     component: HomePage,
// }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;