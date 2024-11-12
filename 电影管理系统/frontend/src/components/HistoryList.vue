<script setup>
import { onMounted,computed } from 'vue';
import { Delete } from '@element-plus/icons-vue';
// import { useRouter } from 'vue-router';

import {watchStore}  from '../apis/watch'
const useWatchStore = watchStore();
    onMounted(() => {
            useWatchStore.watchhistory();
    }
    )
const watchs = computed(() => useWatchStore.watchs)
function deleteByid(id) {
    useWatchStore.delete_by_id(id)
}
</script>

<template>
     <div class="historycontent">
        <ul class="ul_cont">
            <div class="historyList">
                <el-timeline >
                    <el-timeline-item v-for="watch in watchs" 
                    :key="watch.id"
                    :timestamp ="watch.watchTime"
                    class="historyItem" 
                    >
                            <div class="hisMovie">
                                <img :src="watch.movie_image">
                            </div>
                            <div class="history_movie_msg">
                                <div class="historyName">
                                    <p>{{ watch.movie_name }}</p>
                                </div>
                                <span class="delete" @click="deleteByid(watch.id)">
                                    <el-icon>
                                        <Delete />
                                    </el-icon>
                                </span>
                            </div>
                    </el-timeline-item>
                </el-timeline>
            </div>
        </ul>
    </div>
</template>
<style>
.historyList {
    min-width: 980px;
    margin: 0 auto;
    margin-left: 197px;
}
.historyItem,.el-timeline-item__content {
    display: flex;
    align-items: center;
}
.hisMovie {
    width: 160px;
    height: 100px;
    margin: 30px;
}
.historyName:hover p {
    color:#00a1d6 ;
}
.history_movie_msg {
    width: 600px;
    justify-content: space-between;
}
.history_movie_msg,.history_movie_msg .delete{
    display: flex;
    align-items: center;
    cursor: pointer;
}

</style>