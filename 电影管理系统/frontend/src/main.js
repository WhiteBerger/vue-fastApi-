import { createApp } from 'vue'
import App from './App.vue'
import "./style.css"
//导入ElementPlus库
import ElementPlus, { ElIcon } from 'element-plus'
import 'element-plus/dist/index.css'
//导入路由
import router from './router/index.js'
//导入pinia
import { createPinia } from "pinia"
const app =createApp(App)

app.use(ElementPlus)
app.use(router)
app.use(createPinia())
app.mount('#app')
