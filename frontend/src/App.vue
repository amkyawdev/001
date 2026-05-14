<template>
  <div class="app">
    <header class="header">
      <div class="logo">
        <span class="logo-icon">&#x1F916;</span>
        <div>
          <h1>AI Chat Bot</h1>
          <span class="powered">Powered by Groq &middot; llama3-70b</span>
        </div>
      </div>
      <div class="status">
        <span class="dot"></span> Online
      </div>
    </header>
    <ChatWindow />
  </div>
</template>

<script>
import ChatWindow from './components/ChatWindow.vue'
export default {
  components: { ChatWindow }
}
</script>

<style scoped>
.app {
  width: 100%;
  max-width: 680px;
  height: 100vh;
  max-height: 820px;
  display: flex;
  flex-direction: column;
  background: #1a1a2e;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 24px 60px rgba(0,0,0,0.5);
}
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 24px;
  background: #16213e;
  border-bottom: 1px solid #1e293b;
}
.logo { display: flex; align-items: center; gap: 12px; }
.logo-icon { font-size: 2rem; line-height: 1; }
h1 { font-size: 1.1rem; font-weight: 700; color: #e2e8f0; letter-spacing: -0.02em; }
.powered { font-size: 0.72rem; color: #6366f1; font-weight: 500; }
.status { display: flex; align-items: center; gap: 6px; font-size: 0.8rem; color: #4ade80; font-weight: 500; }
.dot { width: 8px; height: 8px; border-radius: 50%; background: #4ade80; animation: pulse 2s infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
</style>
