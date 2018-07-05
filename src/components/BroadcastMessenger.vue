<template>
  <div>
    <div class="row message" id="conversation">

      <div class="row message-body">
        <template v-for="message in messages">
          <div :class="message.sender == username ? 'col-sm-12 message-main-sender' : 'col-sm-12 message-main-receiver'">
            <div :class="message.sender == username ? 'sender' : 'receiver'">
              <div class="sender-name">
               {{message.sender}}
              </div>
              <div class="message-text">
               {{message.message}}
              </div>
              <span class="message-time pull-right">
                
              </span>
            </div>
          </div>
        </template>
      </div>
    </div>
    <input type="hidden" :name="username" @username-change="username = $event">
    <div class="row reply">
      <div class="col-sm-9 col-xs-9 reply-main">
        <textarea class="form-control" rows="1" id="comment" v-model="comment"></textarea>
      </div>
      <div class="col-sm-1 col-xs-1 reply-send" v-on:click="sendMessage(comment)">
        <i class="fa fa-send fa-2x" aria-hidden="true"></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'broadcast-messenger',
  data () {
    return {
      messages: [],
      websocket: new WebSocket("ws://127.0.0.1:8765/"),
    }
  },
  props: {
    value: String,
  },
  computed: {
    username: {
      get () {
        return this.value
      },
      set (value) {
        this.$emit('input', value)
      },
    },
  },
  mounted: function() {
    var websocket = this.websocket;
    var messages = this.messages;
    var username = this.username;
    websocket._original_send_func = websocket.send;

    websocket.send = function(data) {
       if(this.readyState == 1)
         this._original_send_func(data);
       }.bind(websocket);
    
    websocket.onmessage = function (event) {
        var data = JSON.parse(event.data);
        console.log(data);
        console.log(messages);
        messages.push(data)
        return false;
    };

    websocket.onopen = function (e) {
      websocket.send(JSON.stringify({sender: username, message: 'Testando mensagem'}));
    }
  },
  methods: {
    sendMessage: function(text) {
        this.websocket.send(JSON.stringify({sender: this.username, message: text}));
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
