<template>
	<div class="col-xs-12 col-sm-8 conversation">
	  <!-- Heading -->
	  <div class="row heading">
	    <div class="col-sm-8 col-xs-7 heading-name">
	      <a class="heading-name-meta">{{current}}
	      </a>
	    </div>
	    <div class="col-sm-1 col-xs-1  heading-dot pull-right">
	      <i class="fa fa-ellipsis-v fa-2x  pull-right" aria-hidden="true"></i>
	    </div>
	  </div>
		<div class="row message" id="conversation">

			<div class="row message-body">
				<template v-for="message in messages">
					<template v-if="message.room == current || ((message.sender == current || message.sender == 'Server') && message.type == 'private')">
						<div :class="message.sender == username ? 'col-sm-12 message-main-sender' : 'col-sm-12 message-main-receiver'">
							<div :class="message.sender == username || message.sender == 'Server' ? 'sender' : 'receiver'">
								<div class="sender-name">
									<span v-if="message.type == 'join_event'" style="font-style: italic;">{{message.sender}} {{message.content}}</span>
									<span v-else v-confirm="{
										message:'Trocar com ' + message.sender + '?',
										okText: 'Trocar',
										cancelText: 'Fechar',
										ok: dialog => chatPrivado(message.sender)
									}">
	          				{{message.sender}}
	          			</span>
								</div>
								<div v-if="message.type == 'message' || message.type == 'private'" class="message-text">
									{{message.content}}
								</div>
							</div>
						</div>
					</template>
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

		data() {
			return {
				messages: [],
				websocket: new WebSocket('ws://127.0.0.1:8765/'),
        rooms: ['Broadcast']
			}
		},
		props: {
			value: String,
			chat: String,
			room: String
		},
		computed: {
			username: {
				get() {
					return this.value
				},
				set(value) {
					this.$emit('input', value)
				}
			},
			current: {
			  get () {
			    return this.chat
			  }
			},
			roomactive: {
				get () {
					return this.room
				}
			}
		},
		mounted: function () {
			var websocket = this.websocket
			var messages = this.messages
			var username = this.username
			var _this = this
			websocket._original_send_func = websocket.send

			websocket.send = function (data) {
				if (this.readyState === 1) {
					this._original_send_func(data)
				}
			}.bind(websocket)

			websocket.onmessage = function (event) {
				console.log("DATA")
				var data = JSON.parse(event.data)
				console.log(data)
				if (['message', 'join_event', 'private'].indexOf(data.type) >= 0) {
					messages.push(data)
				}

        if (data.type == 'exchange_success') {
          alert(data.content + '\nSuas figurinhas: ' + data.stickers)
        }

				if (['open_private', 'join_room'].indexOf(data.type) >= 0) {
					_this.emit(data)
				}

				return false
			}

			websocket.onopen = function (e) {
				websocket.send(JSON.stringify({sender: username, type: 'join_event', content: 'entrou na sala', room: _this.current}))
			}
		},
		methods: {
			sendMessage: function (text) {
        if (text.substring(0, 6) == "/trade") {
          var offer = text.split(" ")
          this.websocket.send(JSON.stringify({sender: this.username, type: 'exchange', mine: offer[1], his: offer[2], room: this.current}))
        } else if (text.substring(0, 5) == "/join") {
          var offer = text.split(" ")
          this.websocket.send(JSON.stringify({sender: this.username, type: 'join_room', content: offer[1], room: offer[1]}))
          this.rooms.push(offer[1])
        } else if (this.rooms.indexOf(this.current) >= 0) {
				  this.websocket.send(JSON.stringify({sender: this.username, type: 'message', content: text, room: this.current}))
        } else {
          this.websocket.send(JSON.stringify({sender: this.username, type: 'private', content: text, room: this.current}))
        }
			},
			chatPrivado: function (sender) {
				this.websocket.send(JSON.stringify({sender: this.username, type: 'open_private', content: sender}))
			},
			emit: function (payload) {
				this.$emit('new-chat', payload)
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
