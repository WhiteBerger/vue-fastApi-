import { defineStore } from "pinia";
import { FASTAPI_BASE_URL } from "../constant";
import axios from "axios";

export const animeStore = defineStore("animes",{
    state : () => ({
        animes :[],
        videos:[],
        total_video: []
    }),
    getters : {

     },
    actions : {
        async loadAnime() {
            try {
                const response = await axios.get(`${FASTAPI_BASE_URL}/animes`)
                this.animes = response.data;
            }catch(error){
                console.log(error);
            }
        },
        async animeVideo(i=1) {
            let anime_name = sessionStorage.getItem('name')
            const videoUrl = "http://localhost:5173/src/videos/animes/鬼灭之刃/柱训练篇"
            console.log();
            try {
                const res = await axios.get(`${FASTAPI_BASE_URL}/anime/${anime_name}`)
                if(this.videos !=null){
                    this.videos = []
                }
                if(this.total_video !=null){
                    this.total_video = []
                }
                const url = res.data[0].video.split(',')
                // 导入视频地址
                this.videos.push(videoUrl+url[i-1])
                //导入动漫集数
                url.forEach(element => {
                    this.total_video.push(element)
                });
                }catch(error){
                    console.log(error);
                }
        },
    }
})
