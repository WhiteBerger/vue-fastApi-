<script setup>
import { reactive } from 'vue';
import { userStore } from '../apis/users';
import { useRouter } from 'vue-router';
import { RouterLink } from 'vue-router';
import {UserFilled} from '@element-plus/icons-vue'
const router = useRouter()
const loginForm =reactive({
  useremail :"",
  password : "",
})
const useUserStore = userStore()
const login =() => {
  useUserStore.login(loginForm).then(res =>{
    if( useUserStore.isLoggedIn ){
      
      }
  })
}
</script>
<template>
      <div class="login">
         <div class="head">
              <el-icon :size ="30">
                      <UserFilled/>
              </el-icon>
          </div>
          <el-form class="loginForm"  label-position = "top">
                <el-form-item label="电子邮箱:" >
                        <el-input v-model="loginForm.useremail" type="email"/>
                </el-form-item>
                <el-form-item label="密码:">
                        <el-input  v-model="loginForm.password" type="password" show-password />
                </el-form-item>
                <el-form-item>
                        <el-button @click="login" style="margin: 0 auto;" type="primary">登录</el-button>
                </el-form-item>
                <el-form-item>
                  <div class="Register">
                      
                            <i>还没有有账号?</i>
                            <RouterLink to="/register">
                              <span style="text-decoration: underline; color:#a3a3a3;">
                                点击注册
                              </span>
                            </RouterLink>
                  </div>
                </el-form-item>
          </el-form>
      </div>
</template>

<style scoped>
.login {
  min-width: 475px;
  max-width: 475px;
  margin: 50px auto;
  box-shadow: 3px 3px 3px 3px #9ca3af;
}

.loginForm {
  width: 100%;
}
.head {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 38px;
  line-height: 38px;
}
.Register {
  margin: 0 auto;
}
</style>