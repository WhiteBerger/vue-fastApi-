<script setup>
import { UserFilled } from '@element-plus/icons-vue';
import { computed, ref,onMounted } from 'vue';
import { userStore } from '../apis/users';
const useUserStore = userStore();

const avaterUrl = ref('')
onMounted(() =>{
    useUserStore.getUser()
})
const users = computed(()=>useUserStore.users)
function update(name) {
    useUserStore.update(name)
} 


</script>
<template>
        <div class="userform" v-for="user in users" :key="user.id">
            <h1>修改个人信息</h1>
           <div class="userInfo">
                <span>头像</span>
                <div class="borderPi">
                    <el-upload
                    class="avatar-uploader"
                    action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload"
                    > 
                         <el-avatar :size="50" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
                    </el-upload>
                </div>
           </div>
           <div class="userInfo">
                <span>昵称</span>
                <div class="borderPi">
                    <el-input type="text" v-model="user.name"/>
                </div>
           </div>
           <div class="userInfo">
                <span>邮箱</span>
                <div class="borderPi">
                    <el-input type="text" v-model="user.email"/>
                </div>
           </div>
           <div class="btn">
            <el-button type="primary" style="margin-bottom: 10px;" @click="update(user.name)">保存</el-button>
            <!-- <unRegister/> -->
           </div>
        </div>
</template>



<style>
.userform{
    display: flex;
    align-items: center;
    box-shadow: 3px 3px 3px #e2e8f0;
    max-width: 475px;
    min-width: 375px;
    margin: 50px auto;
    flex-direction: column;
}
.userInfo {
    width: 100%;
    margin-bottom: 20PX;
    border-bottom: 2px solid rgb(124, 130, 137);
    justify-content: space-between;
}
.borderPi .el-input .el-input__wrapper {
  background: none;
  box-shadow: none;
}
.btn {
    display: flex;
}
</style>