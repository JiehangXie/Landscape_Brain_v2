import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'

import Index from './components/Index.vue'
import Upload from './components/Upload.vue'

const routes = [
    { path: '/', component: Index },
    { path: '/upload', component: Upload}
]

const router = createRouter({
    history: createWebHistory(),
    routes // (缩写) 相当于 routes: routes
});


createApp(App).use(router).use(ElementPlus).mount('#app')
