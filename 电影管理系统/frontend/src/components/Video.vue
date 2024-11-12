<script setup>
import { computed, onMounted } from 'vue';

import { animeStore } from '../apis/animes';

const useAinmeStore = animeStore();

onMounted(()=>{
useAinmeStore.animeVideo()
})
const videos = computed(()=>useAinmeStore.videos)

const total = computed(()=>useAinmeStore.total_video)
function changeVideo(i) {
   useAinmeStore.animeVideo(i)
   document.querySelector('.in').classList.remove('in')
   document.querySelector(`li:nth-child(${i}).Animeitem`).classList.add('in')
   
}
</script>

<template>
       <div class="videoItem" v-for="video in videos" :key="video.id">
            <div class="showVideo">
                <div class="video">
                    <video controls class="myvideo"
                    autoplay
                    :src="video"
                    >
                    </video>
                </div>
                <div class="animeConuts">
                         <li :class="i==1 ? 'Animeitem in' : 'Animeitem'" v-for="i in total.length"  :kye="i" @click="changeVideo(i)" title="第1集">
                            <span  class="name">{{i}}</span>
                         </li>
                </div>
            </div>
       </div>
       <div class="discuss">
                    <div class="biaoqian">
                        <li class="appraise">
                            <span class="appItem">
                                <svg id="like_info_icon" class="icon" width="36" height="36" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.77234 30.8573V11.7471H7.54573C5.50932 11.7471 3.85742 13.3931 3.85742 15.425V27.1794C3.85742 29.2112 5.50932 30.8573 7.54573 30.8573H9.77234ZM11.9902 30.8573V11.7054C14.9897 10.627 16.6942 7.8853 17.1055 3.33591C17.2666 1.55463 18.9633 0.814421 20.5803 1.59505C22.1847 2.36964 23.243 4.32583 23.243 6.93947C23.243 8.50265 23.0478 10.1054 22.6582 11.7471H29.7324C31.7739 11.7471 33.4289 13.402 33.4289 15.4435C33.4289 15.7416 33.3928 16.0386 33.3215 16.328L30.9883 25.7957C30.2558 28.7683 27.5894 30.8573 24.528 30.8573H11.9911H11.9902Z"></path></svg>
                                <span style="margin-left: 10px;">123</span>
                            </span>
                        </li>
                    </div>
       </div>
</template>

<style>
.showVideo{
    display: flex;
    align-items: center;
    margin-left: 64px;
}
.showVideo video{
    min-width: 668px;
}
.animeConuts{
    display: flex;
    background-color: #F1F2F3;
    min-width:350px ;
    margin-left: 10px;
}
.biaoqian {
    height: 64px;
    display: flex;
    align-items: center;
}
.appItem {
    color:#61666D;
    fill: #61666D;
    display: flex;
    align-items: center;
    cursor: pointer;
}
.appraise:hover .appItem {
    fill:#00AEEC ;
    color: #00AEEC;
}
.appraise >span .icon {
    width: 28px;
    height: 28px;
}
.Animeitem {
    border: 1px solid pink;
    margin-right: 20px;
    cursor: pointer;
    height: 50px;
    width: 50px;
}
.Animeitem span {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height:100%;
}
.Animeitem:hover span {
    background-color: pink;
}
.in {
    background-color: pink;
}
</style>