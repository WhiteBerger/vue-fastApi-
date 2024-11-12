<script setup>
import { reactive } from 'vue';
import { userStore } from '../apis/users';
import { useRouter } from 'vue-router';
import { RouterLink } from 'vue-router';

const router = useRouter();
const useUserStore = userStore();
const RegisterForm =reactive({
    name :"",
  useremail :"",
  password : "",
})

const Register =() => {
     useUserStore.createUser(RegisterForm).then(res =>{
        if(res.status == 200){
            alert("注册成功")
            router.push('/login')
        }
     }).catch(err =>{
        console.log(err)
        alert("邮件地址已存在")
     } )
}

</script>

<template>
    <div class="Register">
        <el-form class="RegisterForm"  label-position = "top">
            <el-form-item label="昵称:" >
                      <el-input v-model="RegisterForm.name"  />
              </el-form-item>
              <el-form-item label="电子邮箱:" >
                      <el-input v-model="RegisterForm.useremail" type="email" />
              </el-form-item>
              <el-form-item label="密码:">
                      <el-input  v-model="RegisterForm.password" type="password" show-password />
              </el-form-item>
              <el-form-item>
                      <el-button @click="Register" style="margin: 0 auto;" type="primary">注册</el-button>
              </el-form-item>
        </el-form>
    </div>
</template>

<style scoped>
.Register {
max-width: 420px;
height: 275px;
margin: 50px auto;
box-shadow: 2px 2px 2px 2px #a1a1aa;
}
.RegisterForm {
max-width: 320px;
margin: 0 auto;
}
.Register {
margin: 0 auto;
}
</style>