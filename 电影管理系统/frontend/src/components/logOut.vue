<script setup>
import { userStore } from "../apis/users";
import { useRouter } from "vue-router";
const userData = userStore();
const router = useRouter();

const LogOut = () => {
  userData.logOut();
  localStorage.removeItem('isLoggedIn')
  localStorage.removeItem('access_token')
  router.go(0)
};
</script>
<template>
  <el-button @click="LogOut" style="width: 100%;">退出登录</el-button>
</template>