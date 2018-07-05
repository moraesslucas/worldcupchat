<template>
  <div class="container app">
    <div class="row app-one">

      <div class="col-sm-4 side">
        <Sidebar v-model="username" v-bind:openchats="chats" v-on:change-chat="changeActiveChat"/>
      </div>


      <!-- New Message Sidebar End -->

      <!-- Conversation Start -->
        <!-- Heading End -->

        <!-- Message Box -->
        <BroadcastMessenger v-model="username" v-on:new-chat="openNewChat" v-bind:chat="meuchat" v-bind:room="room"/>
      <!-- Conversation End -->
    </div>
    <!-- App One End -->
  </div>

</template>

<script>
import Sidebar from './Sidebar.vue'
import BroadcastMessenger from './BroadcastMessenger.vue'
import Teste from './Teste.vue'

export default {
  name: 'hello',
  components: {
    Sidebar,
    BroadcastMessenger,
    Teste
  },
  data () {
    return {
      username: 'Fulaninho',
      chats: [],
      meuchat: 'Broadcast',
      room: 'Broadcast'
    }
  },
  methods: {
    openNewChat: function (payload) {
      var chat = {}
      if (payload.sender != this.username) {
        chat.username = payload.sender
      } else if (payload.content != this.username) {
        chat.username = payload.content
      } else {
        return
      }

      chat.room = payload.room

      if (this.chats.some(function(el){ return el.username === chat.username})) {
        console.log("já existe")
      } else {
        this.chats.push(chat)
      }
    },
    changeActiveChat: function (payload) {
      console.log(payload)
      this.meuchat = payload.username
      this.room = payload.room
    }
  }
}
</script>

<style scoped>
#hello {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
