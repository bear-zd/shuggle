import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from "./router";


// 5. Create and mount the root instance.
const app = createApp(App)
// Make sure to _use_ the router instance to make the
// whole app router-aware.
app.use(router)

app.mount('#app')
