import { defineStore } from "pinia";
import { FASTAPI_BASE_URL } from "../constant";
import axios from "axios";
export const watchStore = defineStore("watc", {
    state : () => ({
        watchs :[],
    }),

    actions : {
        async addWatch(data) {
        
            const userdata = {movie_id :data.id,
                              movie_name : data.name,
                              movie_image : data.image
                              }
            try {
                const response = await axios.post(`${FASTAPI_BASE_URL}/userwatch`,userdata,
                    {
                        headers:{
                            'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                        }
                    });
                    this.watchhistory()
                }catch(error) {
                    console.log(error);
                }
        },

        async watchhistory() {
            try {
                const response = await axios.get(`${FASTAPI_BASE_URL}/watch`,
                    {
                        headers:{
                            'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                        }
                    });
                    if(this.watchs !=null){
                        this.watchs=[]
                    }
                    response.data.forEach(element => {
                        this.watchs.push(element)
                    })
            }catch(error){
                console.log(error);
            }
        },
        async searchHistory(name){
            try{
                const response = await axios.get(`${FASTAPI_BASE_URL}/watch/${name}`,
                    {
                        headers:{
                            'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                        }
                    });
                    this.watchhistory()
            }catch(error){
                console.log(error);
            }
        },
        async delete_by_id(id){
            try{
                const response = await axios.delete(`${FASTAPI_BASE_URL}/userwatch/${id}`,
                    {
                        headers:{
                            'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                        }
                    });
                    this.watchhistory()
            }catch(error){
                console.log(error);
            }
        },
        async delete_all_by_user_id(){
            try{
                const response = await axios.delete(`${FASTAPI_BASE_URL}/userwatch`,
                    {
                        headers:{
                            'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                        }
                    });
                  this.watchhistory()
            }catch(error){
                console.log(error);
            }
        },
    }
})