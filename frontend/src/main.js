import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import ElementPlus from 'element-plus'




const app = createApp(App)

app.use(router).use(ElementPlus)

app.mount('#app')
