import { defineStore } from "pinia";
import { FASTAPI_BASE_URL } from "../constant";
import axios from "axios";


export const todoStore = defineStore("todos",{
    state : () => ({
        todos : [],
    }),

    actions : {
        async loadTodo() {
                try {
                        const response = await axios.get(`${FASTAPI_BASE_URL}/todos`, 
                        {headers: {
                            'Authorization': `Bearer ${localStorage.getItem('token')}`, // 在请求头中添加身份验证令牌
                            }}
                        );
                        return response;
                    }catch(error) {
                        console.log(error);    
                    } 
        },

        async deleTodo(name) {
             try {
                const response = await axios.delete(`${FASTAPI_BASE_URL}/todos`,
                    {
                        headers:{
                            'Authorization': `Bearer ${localStorage.getItem('token')}`,
                        }
                    });
                return response
             }catch(error){
                console.log(error);
             }
        }
    }
})

