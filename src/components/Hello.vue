<template>
  <div class="container app">
    <div class="row app-one">

      <div class="col-sm-4 side">
        <Sidebar v-model="username"/>
      </div>


      <!-- New Message Sidebar End -->

      <!-- Conversation Start -->
      <div class="col-xs-12 col-sm-8 conversation">
        <!-- Heading -->
        <div class="row heading">
          <div class="col-sm-2 col-md-1 col-xs-3 heading-avatar">
            <div class="heading-avatar-icon">
              <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsERE__yKbJ86IZGz8AhbogF8M6w7ru-29Kb0DTNtmJuXnxaulgg">
            </div>
          </div>
          <div class="col-sm-8 col-xs-7 heading-name">
            <a class="heading-name-meta">Broadcast
            </a>
            <span class="heading-online">Online</span>
          </div>
          <div class="col-sm-1 col-xs-1  heading-dot pull-right">
            <i class="fa fa-ellipsis-v fa-2x  pull-right" aria-hidden="true"></i>
          </div>
        </div>
        <!-- Heading End -->

        <!-- Message Box -->
        <BroadcastMessenger v-model="username"/>
      </div>
      <!-- Conversation End -->
    </div>
    <!-- App One End -->
  </div>

</template>

<script>
import Sidebar from './Sidebar.vue'
import BroadcastMessenger from './BroadcastMessenger.vue'

export default {
  name: 'hello',
  components: {
    Sidebar,
    BroadcastMessenger
  },
  data () {
    return {
      username: 'Fulaninho'
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
