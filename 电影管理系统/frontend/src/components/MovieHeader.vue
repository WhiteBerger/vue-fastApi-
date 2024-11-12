<script setup>
import {Search,Eleme} from '@element-plus/icons-vue'
import { useRouter,RouterLink } from 'vue-router';
import {reactive} from 'vue'
import { onMounted,computed } from 'vue';
import {watchStore}  from '../apis/watch'
import { movieStore } from '../apis/movies';
import userMesage from './userMesage.vue';
import LoginView from "../views/LoginView.vue";

let nowDate = new Date()
let day = nowDate.getDate()
let month = nowDate.getMonth()
const router= useRouter()
const SearchForm = reactive({
    name:""
})
const useWatchStore = watchStore();
//引入登录状态
let isLoggedIn = localStorage.getItem('isLoggedIn')
//获取观影记录
const useMovieStore = movieStore();
const search =() => {
    useMovieStore.getMovieByname(SearchForm.name)
}
//点击跳转至用户个人界面
const touser =() => {
    if(isLoggedIn){
      logginBtn = document.getElementsByClassName("showLogin")
      logginBtn.style.display ==="none"
    }
}
const N = ()=>{
   useWatchStore.watchhistory()
}
onMounted(()=>{
    useWatchStore.watchhistory()
})
const watchs = computed(() => useWatchStore.watchs)

const login = () =>{
    logginBtn = document.getElementsByClassName("showLogin")
    logginBtn.style.display ==="block"
}
</script>
<template>
    <div class="header">
        <ul class="left">
            <li class="log">
                <img src="../images/totoro.gif">
            </li>
            <li class="item">
                <RouterLink to="/">
                    <span>
                        首页
                    </span>
                </RouterLink>
            </li>
            <li class="item">
                <RouterLink to="/movie" target="_blank">
                    <span >
                        电影
                    </span>
                </RouterLink>
            </li>
            <li class="item">
                <RouterLink to="/Anime" target="_blank">
                    <span>
                        番剧
                    </span>
                </RouterLink>
            </li>
        </ul>
        <div class="search">
            <el-input v-model="SearchForm.name" style="min-width: 275px; outline: none;border: none; "/>
            <el-button @click="search" type="primary">
                <el-icon style="vertical-align: middle">
                    <Search />
                </el-icon>
            </el-button>
        </div>
        <ul class="right">
            <li class="userFunction" @click="touser">
                <el-dropdown  :hide-on-click="false">
                        <div class="user">
                            <!-- <el-icon :size="20">
                                    <UserFilled/>
                            </el-icon> -->
                            <el-avatar :size="50" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
                        </div>
                            <template #dropdown >
                                <el-dropdown-menu>
                                    <el-dropdown-item v-if="isLoggedIn !=null">
                                        <userMesage/>
                                    </el-dropdown-item>
                                    <el-dropdown-item v-if="isLoggedIn==null" >
                                                <el-button @click ="login" >登录</el-button>
                                    </el-dropdown-item>
                                </el-dropdown-menu>
                            </template>
                </el-dropdown>
            </li>
            <li class="watchHistory">
                <el-dropdown max-height="375px">
                    <RouterLink to="/moviehistory"  style="outline: none;">
                        <div class="Eleme" @mouseenter="N">
                            <el-icon :size="22">
                                    <Eleme />
                            </el-icon>
                        </div>  
                    </RouterLink>
                    <template #dropdown >
                        <el-dropdown-menu>
                            <el-dropdown-item v-if="isLoggedIn==null" >
                                <div class="promptMseg">
                                        <p>登录立即查看历史记录</p>
                                        <el-button @click ="login" type="primary" style="width: 150px;">立即登录</el-button>
                                </div>
                            </el-dropdown-item>
                            <div class="alertMsg">
                                <p v-if="watchs.length==0 && isLoggedIn!=null">你还没有观影记录,快去观影吧</p>
                            </div>
                            <el-dropdown-item  v-for="watch in watchs" :key="watch.movie_id">
                                <div class="movie">
                                        <div class="movieImage">
                                            <img :src="watch.movie_image">
                                        </div>
                                        <div class="movieMsg">
                                            <p style="font-size: 14px;color: #222;">{{ watch.movie_name }}</p>
                                            <div class="watcime" >
                                                <div v-if="new Date(watch.watchTime).getDate() == day && new Date(watch.watchTime).getMonth() ==month">
                                                    <span style="font-size: 12px;color: #99a2aa;" >今天{{ new Date(watch.watchTime).getHours()+8}}:{{ new Date(watch.watchTime).getMinutes() }}</span>
                                                </div>
                                                <div v-if="new Date(watch.watchTime).getDate() ==day - 1 ">
                                                    <span style="font-size: 12px;color: #99a2aa;" >昨天{{ new Date(watch.watchTime).getHours()+8}}:{{ new Date(watch.watchTime).getMinutes() }}</span>
                                                </div>
                                                <div v-if="new Date(watch.watchTime).getMonth() ==month && day - new Date(watch.watchTime).getDate() >=3 ">
                                                    <span style="font-size: 12px;color: #99a2aa;" >{{new Date(watch.watchTime).getDate()}}</span>
                                                </div>
                                                <div v-if="new Date(watch.watchTime).getMonth() !=month ">
                                                    <span style="font-size: 12px;color: #99a2aa;" >{{new Date(watch.watchTime).getMonth() +1}}-{{new Date(watch.watchTime).getDate()}}</span>
                                                </div>
                                            </div>
                                        </div>
                                </div>
                            </el-dropdown-item>                              
                        </el-dropdown-menu>
                    </template>           
                </el-dropdown>
            </li>
        </ul>
    </div>
    <div class="showLogin">
         <LoginView/>
    </div>

</template>
<style>
.showLogin{
  display: none;
}
.header {
    height: 64px;
    display: flex;
    align-items: center;
    max-width: 800px;
    min-width: 550px;
}
.log {
    height: 64px;
    min-width: 100px;
}
.search {
    display: flex;
    align-items: center;
    margin: 0 auto;
}
.log img {
    width: 100%;
    height: 100%;
}
.right,.left {
    display: flex;
    align-items: center;
    min-width:450px ;
}
.left .item {
    margin-right: 24px;
}
.userFunction,.watchHistory  {
    display: flex;
    align-items: center;
    width: 50px;
    margin-left:32px;
}
/* .watchHistory:hover{

} */
.user,.Eleme{
   border: 1px solid #f1f5f9;
   outline: none;
   border-radius: 70%;
   display: flex;
   justify-content: center;
   align-items: center;
   /* transition : all 0.5s; */
}
.promptMesg {
    background-color: #f1f5f9;
    box-shadow: 2px 2px 2px 2px #f1f5f9;
    width: 100%;
}
.watchHistory .el-dropdown-menu__item {
    width: 369px;
    height: 85px;
    display: flex;
    margin-top: 24px;
}
.alertMsg {
    font-size: 14px;
}
.movie {
    display: flex;
    align-items: center;
}
.movieImage {
    width: 120px;
    height: 100px;
    margin-right: 20px;
}
.movie .movieMsg .watcime {
    margin-top: 24px;
}

</style>