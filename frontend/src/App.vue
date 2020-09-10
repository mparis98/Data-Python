<template>
<div id="app">
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
</style>
