import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import './style.css';

const app = createApp(App);

app.use(createPinia());
app.use(router);

// Global error handler (Hands-On 10 pattern): catches unhandled
// component errors, logs them, and could show a fallback UI banner.
app.config.errorHandler = (err, instance, info) => {
  console.error('Global Vue error:', err, info);
};

app.mount('#app');
