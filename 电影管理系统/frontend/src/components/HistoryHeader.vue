<script setup>
import { Search } from '@element-plus/icons-vue';
import {reactive} from 'vue'

import { watchStore } from '../apis/watch';

const useWatchStore = watchStore();
const histroyForm =reactive({
    name : ""
}) 

const searchHistory =()=>{
   useWatchStore.searchHistory(histroyForm.name)
}

const deleteall =()=> {
    let r = confirm("数据删除后不可恢复，确定删除所有记录吗？")
    if(r){
        useWatchStore.delete_all_by_user_id()
    }
}
</script>

<template>
     <div class="history">
            <span style="display:flex;align-items: center;">历史记录</span>
        <div class="search">
            <el-input v-model="histroyForm.name" style="min-width: 275px; outline: none;border: none; "/>
                <el-button @click="searchHistory" type="primary">
                <el-icon style="vertical-align: middle">
                    <Search />
                </el-icon>
            </el-button>
        </div>
        <div class="deleteall">
            <el-button type="primary" @click="deleteall">清空历史记录</el-button>
        </div>
    </div>
</template>
<style>
.history {
    display:flex;
    align-items: center;
    max-width: 1160px;
    margin: 0 auto;
}
.history .log {
    display: flex;
    min-width: 175px;
}
.deleteall {
    margin-left: 32px;
}
</style>