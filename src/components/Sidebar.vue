<template>
  <div>
    <div class="side-one">
      <!-- Heading -->
      <div class="row heading">
        <div class="col-sm-3 col-xs-3 heading-avatar">
          <div class="heading-avatar-icon">
            <img src="http://shurl.esy.es/y">
          </div>
        </div>
        <div class="col-sm-6 col-xs-6 heading-username">
          <input type="text" name="username" class="form-input" v-model="username">
        </div>
        <div class="col-sm-1 col-xs-1  heading-dot  pull-right">
          <i class="fa fa-ellipsis-v fa-2x  pull-right" aria-hidden="true"></i>
        </div>
      </div>
      <!-- Heading End -->
      <!-- sideBar -->
      <div class="row sideBar">

        <div class="row sideBar-body">
          <div class="col-sm-3 col-xs-3 sideBar-avatar">
            <div class="avatar-icon">
              <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsERE__yKbJ86IZGz8AhbogF8M6w7ru-29Kb0DTNtmJuXnxaulgg">
            </div>
          </div>
          <div class="col-sm-9 col-xs-9 sideBar-main">
            <div class="row">
              <div class="col-sm-12 col-xs-12 sideBar-name">
                <span class="name-meta">Broadcast
              </span>
              </div>
            </div>
          </div>
        </div>
        <div class="row sideBar-body">
          <div class="col-sm-3 col-xs-3 sideBar-avatar">
            <div class="avatar-icon">
              <img src="https://www.ibahia.com/fileadmin/user_upload/senac__logo.jpg">
            </div>
          </div>
          <div class="col-sm-9 col-xs-9 sideBar-main">
            <div class="row">
              <div class="col-sm-12 col-xs-12 sideBar-name">
                <span class="name-meta">Senac
              </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Sidebar End -->
    </div>

    <!-- Sidebar End -->
  </div>
</template>

<script>
export default {
  name: 'sidebar',
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
}
</script>

<style scoped>
</style>
