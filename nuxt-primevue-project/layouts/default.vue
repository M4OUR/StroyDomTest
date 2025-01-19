<template>
  <Header />
  <main>
    <Body />
  </main>
  <Footer />
</template>

<script setup>
import Header from '~/components/Header.vue';
import Footer from '~/components/Footer.vue';
import Body from '~/components/Body.vue';
</script>

<style scoped>
main {
  min-height: 80vh;
}
</style>
