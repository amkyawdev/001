<template>
  <div class="chat-wrap">
    <div class="messages" ref="messagesEl">
      <div v-for="(msg, idx) in messages" :key="idx" :class="['message', msg.role]">
        <span v-if="msg.role === 'bot'" class="avatar">&#x1F916;</span>
        <div class="bubble">{{ msg.text }}</div>
        <span v-if="msg.role === 'user'" class="avatar user-av">You</span>
      </div>
      <div v-if="loading" class="message bot">
        <span class="avatar">&#x1F916;</span>
        <div class="bubble typing"><span></span><span></span><span></span></div>
      </div>
    </div>

    <div class="input-area">
      <input
        v-model="userInput"
        @keyup.enter="sendMessage"
        :disabled="loading"
        placeholder="Type a message..."
        autocomplete="off"
      />
      <button @click="sendMessage" :disabled="loading || !userInput.trim()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <line x1="22" y1="2" x2="11" y2="13"></line>
          <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      userInput: '',
      loading: false,
      messages: [
        { role: 'bot', text: 'Hello! I am your AI assistant powered by Groq. How can I help you today?' }
      ]
    }
  },
  methods: {
    async sendMessage() {
      const text = this.userInput.trim()
      if (!text || this.loading) return
      this.messages.push({ role: 'user', text })
      this.userInput = ''
      this.loading = true
      this.$nextTick(() => this.scrollBottom())

      const history = this.messages.slice(0, -1).map(m => ({
        role: m.role === 'bot' ? 'assistant' : 'user',
        content: m.text
      }))

      try {
        const res = await axios.post('/api/chat', { message: text, history })
        this.messages.push({ role: 'bot', text: res.data.reply })
      } catch {
        this.messages.push({ role: 'bot', text: 'Sorry, something went wrong. Please try again.' })
      } finally {
        this.loading = false
        this.$nextTick(() => this.scrollBottom())
      }
    },
    scrollBottom() {
      const el = this.$refs.messagesEl
      if (el) el.scrollTop = el.scrollHeight
    }
  }
}
</script>

<style scoped>
.chat-wrap { display: flex; flex-direction: column; flex: 1; overflow: hidden; }
.messages { flex: 1; overflow-y: auto; padding: 20px 16px; display: flex; flex-direction: column; gap: 14px; background: #0f0f1a; }
.message { display: flex; align-items: flex-end; gap: 8px; }
.message.user { flex-direction: row-reverse; }
.avatar { font-size: 1.4rem; flex-shrink: 0; line-height: 1; }
.user-av { font-size: 0.7rem; font-weight: 700; color: #94a3b8; padding-bottom: 4px; }
.bubble { max-width: 72%; padding: 12px 16px; border-radius: 18px; font-size: 0.93rem; line-height: 1.55; word-wrap: break-word; white-space: pre-wrap; }
.bot .bubble { background: #1e293b; color: #e2e8f0; border-bottom-left-radius: 4px; }
.user .bubble { background: #6366f1; color: white; border-bottom-right-radius: 4px; }
.typing { display: flex; align-items: center; gap: 5px; padding: 14px 18px; }
.typing span { width: 7px; height: 7px; border-radius: 50%; background: #6366f1; animation: bounce 1.2s infinite; }
.typing span:nth-child(2) { animation-delay: 0.2s; }
.typing span:nth-child(3) { animation-delay: 0.4s; }
@keyframes bounce { 0%, 80%, 100% { transform: translateY(0); opacity: 0.5; } 40% { transform: translateY(-6px); opacity: 1; } }
.input-area { display: flex; align-items: center; gap: 10px; padding: 14px 16px; background: #16213e; border-top: 1px solid #1e293b; }
.input-area input { flex: 1; background: #0f0f1a; border: 1px solid #1e293b; border-radius: 12px; padding: 12px 16px; font-size: 0.95rem; color: #e2e8f0; outline: none; transition: border-color 0.2s; }
.input-area input:focus { border-color: #6366f1; }
.input-area input::placeholder { color: #475569; }
.input-area input:disabled { opacity: 0.5; }
.input-area button { background: #6366f1; color: white; border: none; border-radius: 12px; width: 46px; height: 46px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: background 0.2s, transform 0.1s; flex-shrink: 0; }
.input-area button:hover:not(:disabled) { background: #4f46e5; }
.input-area button:active:not(:disabled) { transform: scale(0.95); }
.input-area button:disabled { opacity: 0.4; cursor: not-allowed; }
</style>
