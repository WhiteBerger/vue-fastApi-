<script setup>
import { userStore } from '../apis/users';
import { watchStore } from '../apis/watch';
const useUserStore = userStore();
const useWatchStore = watchStore();
const UnRegister =() => {
    let r = confirm("注销用户后，所有数据都删除，不可恢复，确认注销吗")
    if(r){
       useWatchStore.delete_all_by_user_id()
       useUserStore.unRegister()
    }
}
</script>

<template>
    <el-button @click="UnRegister">注销用户</el-button>
</template>