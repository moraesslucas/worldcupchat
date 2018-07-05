<template>
  <popper trigger="click" :options="{placement: 'top'}">
    <div class="popper">
      Popper Content
    </div>

    <button slot="reference">
      Reference Element
    </button>
  </popper>
</template>

<script>
  import Popper from 'vue-popperjs';
    
  export default {
    components: {
      'popper': Popper
    },
  }
</script> 

<style>
  @import 'vue-popperjs/dist/css/vue-popper.css';
</style>