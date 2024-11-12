import { createRouter, createWebHistory } from "vue-router";
import MovieView from '../views/MovieView.vue'

import RegisterView from "../views/RegisterView.vue";
import userView from "../views/userView.vue";
import HistoryView from "../views/HistoryView.vue";
import VideoView from "../views/VideoView.vue";
import HomeView from "../views/HomeView.vue";
import AnimeView from "../views/AnimeView.vue";
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes :[
      {
        path : "/",
        name : "home",
        component: HomeView
      },
      {
        path : "/anime",
        name : "anime",
        component: AnimeView
      },
      {
        path : "/movie",
        name : "movie",
        component: MovieView
      },
      {
        path :"/register",
        name : "register",
        component:RegisterView
      },
      {
        path :"/user",
        name : "user",
        component:userView
      },
      {
        path :"/moviehistory",
        name : "history",
        component:HistoryView
      },
      {
        path :"/watch",
        name : "watchVideo",
        component:VideoView
      },
    ]
})
export default router;