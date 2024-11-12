<script setup>
import {computed, onMounted, reactive } from 'vue';
// import { computed,onMounted } from 'vue';
import { userStore } from '../apis/users';
import LogOut from './logOut.vue'
// import {EditPen} from '@element-plus/icons-vue'

const useUserStore = userStore();
// const user = reactive({
//      name: localStorage.getItem('name'),
//      email : localStorage.getItem('email')
// })
onMounted(()=>{
     useUserStore.getUser()
})
const users = computed(()=>useUserStore.users)
</script>

<template>
  <div class="userMesg">
 
       <div  style="margin: 0 auto;">
            <div class="userHead">
                <li v-for="user in users" :key="user.id">
                    <span>昵称:</span>
                    {{ user.name}}
               </li>
               <li v-for="user in users" :key="user.id">
                    <span>邮件地址:</span>
                    {{ user.email }}
               </li>
            </div>
       </div>
       <div>
            <LogOut/>
       </div>


  </div>
</template>


<style>
.userMesg {
      width: 275px;
}
.userHead {
     margin:  0 auto;
}
</style>