<script setup>
import {onMounted, computed } from 'vue';
import { movieStore } from '../apis/movies';
import { watchStore } from '../apis/watch';
import Sift from './Sift.vue';
const useMovieStore = movieStore();
const useWatchStore = watchStore();
const addHistiry = (item) => {
    useWatchStore.addWatch(item)
    localStorage.setItem("id",item.id)
    // router.push('/watch')
} 
//使用onMounted钩子函数，在组件挂载后执行的操作，可以用来初始化界面
onMounted(()=> {
    useMovieStore.loadMovie();
})
const movies = computed(()=>useMovieStore.movies);
</script>

<template>
    <div class="content">
        <ul class="ul_cont">
            <div class="movieList">
                <li class="movieItem" v-for="movie in movies" :key="movie.id" >
                        <el-container>
                            <el-header   type="button" @click="addHistiry(movie)">
                                   <img  :src="movie.image" />
                            </el-header>
                            <el-main>
                                <span style="cursor: pointer;" type="button" @click="addHistiry(movie.id)">{{ movie.name }}</span>
                            </el-main>
                        </el-container>
                </li>
                <!-- <div>
                      <li style="width: 50px;height: 50px;">
                         <img src="../images/鬼灭.jpg">
                      </li>
                </div> -->
            </div>
            <Sift/>
        </ul>
    </div>
</template>
<style>
*{
    padding: 0;
    margin: 0;
}
img {
    width: 100%;
    height: 100%;
}
.content {
    margin-top: 32px;
    display: flex;
}
.ul_cont {
    display: flex;
}
.movieList {
    width: 1200px;
    display: flex;
    flex-wrap: wrap;
    margin-left: 24px;
}
.movieItem {
    margin-right: 24px;
    margin-bottom: 60px;
    /* box-shadow: 2px 2px 2px 2px #e2e8f0; */
    width: 160px;
}
.el-header {
    width: 100%;
    height: 214px;
    cursor: pointer;
}
.el-header,.el-main {
    padding: 0;
}
</style>