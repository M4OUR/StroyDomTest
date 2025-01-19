<template>
  <header>
    <p class="resume-link">
      Скачать моё резюме: <a href="/resume.pdf" target="_blank" class="resume-link__button">Резюме</a>
    </p>
  </header>
</template>

<script setup>
defineProps();
</script>

<style scoped>
header {
  background-color: #333;
  color: white;
  padding: 20px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.resume-link {
  font-size: 16px;
  margin-right: 20px;
}

.resume-link__button {
  color: #4CAF50;
  text-decoration: none;
  font-weight: bold;
}

.resume-link__button:hover {
  text-decoration: underline;
}

nav ul {
  list-style: none;
  display: flex;
  gap: 15px;
}

nav ul li a {
  color: white;
  text-decoration: none;
}

nav ul li a:hover {
  text-decoration: underline;
}
</style>
