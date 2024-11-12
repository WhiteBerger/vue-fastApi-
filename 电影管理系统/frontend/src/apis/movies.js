import { defineStore } from "pinia";
import { FASTAPI_BASE_URL } from "../constant";
import axios from "axios";

export const movieStore = defineStore("movies",{
    state : () => ({
        movies :[],
    }),
    getters : {

     },
    actions : {
        async loadMovie() {
            try {
                const response = await axios.get(`${FASTAPI_BASE_URL}/movies`)
                response.data.forEach(element => {
                    this.movies.push(element)
                });
            }catch(error){
                console.log(error);
            }
        },
        async getMovieByname(movie_name){
            try {
                const response = await axios.get(`${FASTAPI_BASE_URL}/movieN/${movie_name}`)
                if(this.movies !=null)
                    this.movies = [];
                response.data.forEach(element => {
                    this.movies.push(element)
                });
            }catch(error){
                console.log(error);
            }
        },
        async getMovieByYear(movie_year){
            try {
                const response = await axios.get(`${FASTAPI_BASE_URL}/movieT/${movie_year}`)
                if(this.movies !=null)
                    this.movies = [];
                response.data.forEach(element => {
                    this.movies.push(element)
                });
            }catch(error){
                console.log(error);
            }
        }
    }
    
})
