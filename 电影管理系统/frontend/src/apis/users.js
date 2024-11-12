import { defineStore } from "pinia";
import axios from 'axios';
import { FASTAPI_BASE_URL } from "../constant";
export const userStore = defineStore("users",{
  state: () => ({
        users: [],
        isLoggedIn :false

      }),
      actions: {
            async login(data) {
              const userData = {username:data.useremail,password:data.password}
              try {
                const response = await axios.post(`${FASTAPI_BASE_URL}/login/access_token`,
                  userData,
                  { headers: { 'content-type': 'application/x-www-form-urlencoded' } }
                ); 
                //存储登录状态    
                localStorage.setItem('isLoggedIn',!this.isLoggedIn)
                this.isLoggedIn = !this.isLoggedIn
                //存储令牌
                localStorage.setItem('access_token',response.data.access_token)
                //存储用户邮箱
                localStorage.setItem('email',userData.username)
                this.getUser(userData.username)
              }catch(error) {
                 // console.log(error);
                 alert(error.response.data.detail)
              }
            },

            async createUser(SignForm) {
                    const userData = {
                                      name : SignForm.name ,
                                      email : SignForm.useremail ,
                                      password : SignForm.password
                                    };
                    try {
                          const response = await axios.post(`${FASTAPI_BASE_URL}/users`,userData);
                          return response
                        }catch(error) {
                        // console.log(error);
                        }
            },

            async getUser() {
                  let useremail=localStorage.getItem('email')
                  try {
                        const response = await axios.get(`${FASTAPI_BASE_URL}/users/${useremail}`);
                        if(this.users !=null){
                          this.users=[]
                          this.users.push(response.data)
                        }else(
                          this.users.push(response.data)
                        )
                      }catch(error){
                        console.log(error);
                      }
            },
          async update(data) {
              const username = {name : data}
              let token = localStorage.getItem('access_token')
              try {
                const response = await axios.put(`${FASTAPI_BASE_URL}/users/name`,username,
                  { headers: { 'Authorization': `Bearer ${token}` } }
                );     
                localStorage.getItem('email',username.name)
                this.getUser()
        
              }catch(error){
                console.log(error);
              }
          },
          async  logOut() {
              if( localStorage.getItem('isLoggedIn')==false) alert("请先登录");
              else {
                this.isLoggedIn = false
                alert("登出成功")
              }
            },
            async unRegister(){
                  try{
                      const response = await axios.delete(`${FASTAPI_BASE_URL}/user`,
                        { headers: { 'Authorization': `Bearer ${token}` } }
                      );
                      alert('注销成功')
                      console.log(response);
                  }catch(error){
                    console.log(error);
                  }
            }
      }
})