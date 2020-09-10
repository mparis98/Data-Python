<template>
<div id="app">
    <img id="logo" src="./assets/logo.png">
    <Company />
</div>
</template>

<script>
import Company from './components/Company'

export default {
    name: 'App',
    components: {
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
}

#logo {
    position: fixed;
    top: 20px;
    left: 20px;
    height: 60px;
    z-index: 99;
    -webkit-font-smoothing: antialiased;
    -moz-font-smoothing: antialiased;
}
</style>
