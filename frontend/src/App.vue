<template>
  <div id="app">
    <img height="100px" src="./assets/flask-logo.png">
    <img height="100px" src="./assets/logo.png">
    <!-- <HelloWorld/> -->
    <Company/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import Company from './components/Company'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Company
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
