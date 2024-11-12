<script setup>
import { onMounted ,computed} from 'vue';
import { useRouter } from "vue-router";
import {animeStore}  from '../apis/animes'
import { watchStore } from '../apis/watch';

const useWatchStore = watchStore()
const useanimeStore = animeStore();
const router = useRouter()
onMounted(() => {
            useanimeStore.loadAnime()
})
const animes = computed(()=>useanimeStore.animes)

function addHistiry(item){
    sessionStorage.setItem('name',item.name)
    useWatchStore.addWatch(item)
    useanimeStore.animeVideo()
    router.push('/watch')
}

</script>

<template>
    <div class="content">
        <ul class="ul_cont">
            <div class="ItemList">
                <li class="Item" v-for="anime in animes" :key="anime.id" >
                    <el-container>
                        <el-header   type="button" @click="addHistiry(anime)">
                                <img  :src="anime.image" />
                        </el-header>
                        <el-main>
                            <span style="cursor: pointer;" type="button" @click="addHistiry(anime)">{{ anime.name }}</span>
                        </el-main>
                    </el-container>
                </li>
            </div>
        </ul>
    </div>
</template>

<style>
li {
    list-style: none;
}
.animeList {
    width: 1200px;
    display: flex;
    flex-wrap: wrap;
    margin-left: 24px;
}
.animeItem {
    margin-right: 24px;
    margin-bottom: 60px;
    /* box-shadow: 2px 2px 2px 2px #e2e8f0; */
    width: 160px;
}
</style>